# Selecione o folder
# .\footstats\Scripts\activate
# streamlit run footstats_st.py

import streamlit as st
import pandas as pd #pandas==2.0.2
import plotly.express as px #plotly==5.15.0
import openpyxl as op
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.pyplot as plt


# Configuração da página
st.set_page_config(layout='wide')

wb = op.load_workbook('dados_multinomial.xlsx')
ws = wb['Sheet1']
dados_multinomial = pd.DataFrame(ws.values)
dados_multinomial.columns = dados_multinomial.iloc[0]
dados_multinomial = dados_multinomial[1:]


### Historico Brasileiraõ
hist = pd.read_csv('brasileirao.csv')

hist.rename(
    columns={
        'place':'Posição',
        'acronym':'Sigla',
        'team':'Time',
        'points':'Pontos',
        'played':'Jogos',
        'won':'Vitórias',
        'draw':'Empates',
        'loss':'Derrotas',
        'goals_for':'Gols Pró',
        'goals_against':'Gols Contra',
        'goals_diff':'Saldo de Gols'
    }, inplace=True
)



##  footstats
wb1 = op.load_workbook('footstats.xlsx')
ws1 = wb1['Sheet1']
dados_footstats = pd.DataFrame(ws1.values)
dados_footstats.columns = dados_footstats.iloc[0]
dados_footstats = dados_footstats[1:]

colunas = dados_footstats.copy()
colunas.drop(columns=['Equipe','Jogador'], inplace= True)
# Loop através de todas as colunas do DataFrame
for column in colunas.columns:
    # Tente converter os valores da coluna para numéricos
    try:
        dados_footstats[column] = pd.to_numeric(dados_footstats[column])
    # Se ocorrer um erro, imprima uma mensagem de aviso
    except Exception as e:
        print(f"Erro ao converter a coluna {column}: {e}")

tabela = pd.read_html('https://fbref.com/en/comps/24/Serie-A-Stats')
tabela_brasileirao = tabela[0]

tabela_brasileirao.rename(
    columns={
        'Rk':'Posição',
        'Squad':'Time',
        'MP':'Jogos',
        'W':'Vitórias',
        'D':'Empates',
        'L':'Derrotas',
        'GF':'Gols Pró',
        'GA':'Gols Contra',
        'GD':'Saldo de Gols',
        'Pts':'Pontos',
        'Pts/MP':'Pontos por partida'
    }, inplace=True
)

df = tabela_brasileirao.iloc[:, 0:14]

colunas = list(df.columns)
colunas.insert(2, colunas.pop(colunas.index('Pontos')))
df = df[colunas]

df['Aproveitamento'] = ((df['Pontos'] / (df['Jogos'] * 3)) * 100).round(2)

col = ['mandante', 'visitante', 'vencedor', 'Temporada',0,1,2,]
df_prev = dados_multinomial[col]
#col_prob = ['mandante', 'visitante',0,1,2,'Temporada']
#df_prob = dados_multinomial[col_prob]



### AHP

def top10_(jogador, clube):
    df = dados_footstats

    df_cluster2 = dados_footstats.copy()
    df_cluster2 = df_cluster2[df_cluster2['Jogos'] != 0]

    df_cluster_a_padronizar = df_cluster2.copy()
    df_cluster_a_padronizar.drop(columns=['Equipe', 'Jogador'], inplace=True)

    # Converter nomes das colunas para strings
    df_cluster_a_padronizar.columns = df_cluster_a_padronizar.columns.astype(str)

    sc_X = StandardScaler(with_mean=True, with_std=True)
    df_cluster_padronizado = sc_X.fit_transform(df_cluster_a_padronizar)

    # Converter para o formato de tabela - StandardScaler 
    df_cluster_padronizado = pd.DataFrame(data=df_cluster_padronizado, columns=df_cluster_a_padronizar.columns)
    
    pca = PCA(n_components=4, random_state=1224)
    df_cluster_pca_atacante = pca.fit_transform(df_cluster_padronizado)
    projection = pd.DataFrame(data=df_cluster_pca_atacante)
    kmeans_pca = KMeans(n_clusters=13, verbose=True, random_state=1224)
    kmeans_pca.fit(projection)
    projection['cluster_pca'] = kmeans_pca.predict(projection)
    projection['Jogador'] = df['Jogador']
    projection['Equipe'] = df['Equipe']
    projection['jogador/time'] = (projection['Jogador'] + '/' + projection['Equipe']) 

    nome_jogador = jogador + '/' + clube

    cluster = list(projection[projection['jogador/time'] == nome_jogador]['cluster_pca'])[0]

    jogador_recomendado = projection[projection['cluster_pca'] == cluster][[0, 1, 2, 3, 'Jogador', 'Equipe']]
    a_jogador = list(projection[projection['jogador/time'] == nome_jogador][0])[0]
    b_jogador = list(projection[projection['jogador/time'] == nome_jogador][1])[0]
    c_jogador = list(projection[projection['jogador/time'] == nome_jogador][2])[0]
    d_jogador = list(projection[projection['jogador/time'] == nome_jogador][3])[0]
    distancias = euclidean_distances(jogador_recomendado[[0, 1, 2, 3]], [[a_jogador, b_jogador, c_jogador, d_jogador]])
    jogador_recomendado['distancias'] = distancias
    tabela = jogador_recomendado.sort_values('distancias').head(11)
    dados_jogador = df_cluster2[df_cluster2['Jogador'].isin(tabela['Jogador']) & df_cluster2['Equipe'].isin(tabela['Equipe'])]
    recomendado = pd.merge(tabela, dados_jogador, on=['Equipe', 'Jogador'], how='inner')

    recomendado = recomendado[list(df_cluster2.columns)]
    recomendado.drop(0, axis=0, inplace=True)

    jogador_equipe = recomendado[['Jogador', 'Equipe']]

    positivos  = recomendado[['Jogos', 'Passe certo', 'Finalização certa', 'Cruzamento certo', 'Interceptação certa', 'Dribles', 'Virada de jogo certa', 'Gols', 'Assistência gol', 'Assistência finalização', 
                               'Rebatida', 'Falta recebida', 'Lançamento certo']]

    negativos = recomendado[['Falta cometida', 'Perda da posse de bola', 'Finalização errada', 'Cruzamento errado',
                             'Passe errado', 'Lançamento errado', 'Interceptação errada', 'Drible errado', 'Virada de jogo errada']]

    colunas = recomendado[list(positivos.columns)]

    # Converter colunas de positivos para numéricas
    positivos = positivos.apply(pd.to_numeric, errors='coerce')

    def ahp_positivos(tabela):
        table = []
        for i in tabela.columns:
            a = tabela[i] / tabela[i].sum()
            table.append(a)
        table = pd.DataFrame(table).T
        return table

    positivos = ahp_positivos(positivos)

    # Converter colunas de negativos para numéricas
    negativos = negativos.apply(pd.to_numeric, errors='coerce')

    def numeros_negativos(tabela):
        table = []
        for i in tabela.columns:
            a = 1 / tabela[i]
            table.append(a)
        table = pd.DataFrame(table).T
        tab_final = []
        for i in table.columns:
            b = table[i] / table[i].sum()
            tab_final.append(b)
        tab_final = pd.DataFrame(tab_final).T
        return tab_final

    negativos = numeros_negativos(negativos)

    tabela_ahp = pd.concat([positivos, negativos], axis=1)

    medias = pd.DataFrame(tabela_ahp.mean(), columns=['media'])
    desvio = pd.DataFrame(tabela_ahp.std(), columns=['desvio'])
    fator_ahp = pd.concat([medias, desvio], axis=1)
    fator_ahp['desvio'] = fator_ahp['desvio'].fillna(np.mean(fator_ahp['desvio']))
    fator_ahp['desvio/media'] = fator_ahp['desvio'] / fator_ahp['media']
    fator_ahp['fator_gaussiano'] = fator_ahp['desvio/media'] / fator_ahp['desvio/media'].sum()
    fator = fator_ahp['fator_gaussiano']
    fator = pd.DataFrame(fator).T
    colunas_para_calculo = fator.columns

    def matriz_de_decisao(tabela, fator):
        table = []
        for i in colunas_para_calculo:
            a = tabela[i] * fator[i][0]
            table.append(a)
        table = pd.DataFrame(table).T
        return table

    resultado_ahp = matriz_de_decisao(tabela_ahp, fator)

    soma = resultado_ahp.sum(axis=1)
    soma = pd.DataFrame(soma, columns=['soma'])

    melhores_escolhas = pd.concat([soma, jogador_equipe], axis=1)
    melhores_escolhas = melhores_escolhas.sort_values(by='soma', ascending=False)
    melhores_escolhas = melhores_escolhas.reset_index(drop=True)

    return melhores_escolhas

# Função para aplicar estilos personalizados
def aplicar_estilos(df):
    # Definir estilos de cor de fundo e fonte para diferentes posições
    def estilos_linhas(s):
        if s.name < 4:  # Top 4
            return ['background-color: #023047; color: white'] * len(s)
        elif s.name == 4 or s.name == 5:  # 5º e 6º lugar
            return ['background-color: #dad7cd; color: black'] * len(s)
        elif s.name >= len(df) - 4:  # Últimos 4 lugares
            return ['background-color: #c1121f; color: white'] * len(s)
        else:
            return [''] * len(s)
    
    styled_df = df.style.apply(estilos_linhas, axis=1)
    return styled_df

# Função para filtrar dados por clube
def filtrar_dados_por_clube(dados_footstats, clube_selecionado):
    if clube_selecionado == "Todos":
        return dados_footstats
    else:
        return dados_footstats[dados_footstats['Equipe'] == clube_selecionado]
    
    

# Títulos e criação das abas
st.title('Dashboard Brasileirão 2024 ⚽')

# Criar abas
abas = st.tabs(["Classificação","Probabilidade", "Dados Jogadores","Top 10 Jogadores Semelhantes","Histórico"])

# Primeira aba: Classificação
with abas[0]:
    st.header("Classificação do Campeonato de Futebol")
    
    # Exibir tabela de classificação com estilos personalizados e sem índice
    st.markdown(aplicar_estilos(df).hide(axis='index').to_html(), unsafe_allow_html=True)

# Segunda aba: Probabilidade
with abas[1]:
    st.header("Histórico de Confrontos")

    # Filtros por time mandante e visitante
    mandante = st.selectbox('Selecione o time mandante:', df_prev['mandante'].unique())
    visitante = st.selectbox('Selecione o time visitante:', df_prev['visitante'].unique())

    # Filtrar histórico de confrontos
    df_filtrado_historico = df_prev[(df_prev['mandante'] == mandante) & (df_prev['visitante'] == visitante)]
    df_filtrado_prob = df_prev[(df_prev['mandante'] == mandante) & (df_prev['visitante'] == visitante)]
    df_filtrado_prob_max = df_filtrado_prob[df_filtrado_prob['Temporada'] == max(df_filtrado_prob['Temporada'])]

    df_filtrado_historico = df_filtrado_historico.drop(columns=[0,1,2])

    # Layout de colunas para histórico e probabilidades
    col1, col2 = st.columns(2)


    # Exibir tabela de histórico filtrada e sem índice
    with col1:
        st.write('Histórico de Confrontos Filtrado:')
        st.markdown(df_filtrado_historico.style.hide(axis='index').to_html(), unsafe_allow_html=True)

    with col2:
        st.write('Valores de Probabilidade:')
        if not df_filtrado_prob.empty:
            empate = df_filtrado_prob[0].values[0] * 100
            vitoria_mandante = df_filtrado_prob[1].values[0] * 100
            vitoria_visitante = df_filtrado_prob[2].values[0] * 100

            st.write(f"Empate: {empate:.2f}%")
            st.write(f"Vitória do {mandante}: {vitoria_mandante:.2f}%")
            st.write(f"Vitória do {visitante}: {vitoria_visitante:.2f}%")
        else:
            st.write('Não há dados suficientes em df_prob para mostrar os valores das colunas 0, 1 e 2.')

with abas[2]:
    st.header("Dados dos Jogadores")
    
    # Adiciona um seletor de clube
    clubes = ["Todos"] + dados_footstats['Equipe'].unique().tolist()
    clube_selecionado = st.selectbox("Selecione o clube", clubes)
    
    # Filtra os dados com base na seleção do clube
    df_filtrado = filtrar_dados_por_clube(dados_footstats, clube_selecionado)
    
    col1, col2 = st.columns(2)
    with col1:
    ### Gráficos

        # Plotar gráficos personalizados
        top_Jogos = df_filtrado.nlargest(5, 'Jogos')
        fig_Jogos = px.bar(top_Jogos, x='Jogador', y='Jogos', text_auto=True, title='Top Nº de Jogos')
        fig_Jogos.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Jogos.update_layout(yaxis_title='Jogos', xaxis_title='Jogadores')  # Adicionar rótulos

        top_Passe_certo = df_filtrado.nlargest(5, 'Passe certo')
        fig_Passe = px.bar(top_Passe_certo, x='Jogador', y='Passe certo', text_auto=True, title='Top Nº de Passes certos')
        fig_Passe.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Passe.update_layout(yaxis_title='Passes certos', xaxis_title='Jogadores')  # Adicionar rótulos

        top_Passe_errado = df_filtrado.nlargest(5, 'Passe errado')
        fig_passeerrado= px.bar(top_Passe_errado, x='Jogador', y='Passe errado', text_auto=True, title='Top Nº de Passes errados')
        fig_passeerrado.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_passeerrado.update_layout(yaxis_title='Passe errados', xaxis_title='Jogadores')  # Adicionar rótulos

        top_Finalizacao_certa = df_filtrado.nlargest(5, 'Finalização certa')
        fig_Finalizacao_certa= px.bar(top_Finalizacao_certa, x='Jogador', y='Finalização certa', text_auto=True, title='Top Nº de Finalizações certas')
        fig_Finalizacao_certa.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Finalizacao_certa.update_layout(yaxis_title='Finalização certa', xaxis_title='Jogadores')  # Adicionar rótulos

        top_Finalizacao_errada = df_filtrado.nlargest(5, 'Finalização errada')
        fig_Finalizacao_errada= px.bar(top_Finalizacao_errada, x='Jogador', y='Finalização errada', text_auto=True, title='Top Nº de Finalizações errados')
        fig_Finalizacao_errada.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Finalizacao_errada.update_layout(yaxis_title='Finalização errada', xaxis_title='Jogadores')  # Adicionar rótulos

        top_Cruzamento_certo = df_filtrado.nlargest(5, 'Cruzamento certo')
        fig_Cruzamento_certo = px.bar(top_Cruzamento_certo, x='Jogador', y='Cruzamento certo', text_auto=True, title='Top Nº de Cruzamentos certos')
        fig_Cruzamento_certo.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Cruzamento_certo.update_layout(yaxis_title='Cruzamento certo', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Cruzamentos errados
        top_Cruzamentos_errados = df_filtrado.nlargest(5, 'Cruzamento errado')
        fig_Cruzamentos_errados = px.bar(top_Cruzamentos_errados, x='Jogador', y='Cruzamento errado', text_auto=True, title='Top Nº de Cruzamentos errados')
        fig_Cruzamentos_errados.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Cruzamentos_errados.update_layout(yaxis_title='Cruzamento errado', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Dribles certos
        top_Drible_certo = df_filtrado.nlargest(5, 'Dribles')
        fig_Drible_certo = px.bar(top_Drible_certo, x='Jogador', y='Dribles', text_auto=True, title='Top Nº de Dribles Certos')
        fig_Drible_certo.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Drible_certo.update_layout(yaxis_title='Dribles', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Dribles errados
        top_Drible_errado = df_filtrado.nlargest(5, 'Drible errado')
        fig_Drible_errado = px.bar(top_Drible_errado, x='Jogador', y='Drible errado', text_auto=True, title='Top Nº de Dribles errados')
        fig_Drible_errado.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Drible_errado.update_layout(yaxis_title='Drible errado', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Viradas de jogo certas
        top_Virada_certa = df_filtrado.nlargest(5, 'Virada de jogo certa')
        fig_Virada_certa = px.bar(top_Virada_certa, x='Jogador', y='Virada de jogo certa', text_auto=True, title='Top Nº de Viradas de jogo certas')
        fig_Virada_certa.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Virada_certa.update_layout(yaxis_title='Viradas de jogo certas', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Viradas de jogo erradas
        top_Virada_errada = df_filtrado.nlargest(5, 'Virada de jogo errada')
        fig_Virada_errada = px.bar(top_Virada_errada, x='Jogador', y='Virada de jogo errada', text_auto=True, title='Top Nº de Viradas de jogo erradas')
        fig_Virada_errada.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Virada_errada.update_layout(yaxis_title='Virada de jogo errada', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Gols
        top_Gols = df_filtrado.nlargest(5, 'Gols')
        fig_Gols = px.bar(top_Gols, x='Jogador', y='Gols', text_auto=True, title='Top Nº de Gols')
        fig_Gols.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Gols.update_layout(yaxis_title='Gols', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Assistência gol
        top_Assistência_gol = df_filtrado.nlargest(5, 'Assistência gol')
        fig_Assistência_gol = px.bar(top_Assistência_gol, x='Jogador', y='Assistência gol', text_auto=True, title='Top Nº de Assistência gol')
        fig_Assistência_gol.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Assistência_gol.update_layout(yaxis_title='Assistência gol', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Assistência finalização
        top_Assistência_finalização = df_filtrado.nlargest(5, 'Assistência finalização')
        fig_Assistência_finalização = px.bar(top_Assistência_finalização, x='Jogador', y='Assistência finalização', text_auto=True, title='Top Nº de Assistência finalização')
        fig_Assistência_finalização.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Assistência_finalização.update_layout(yaxis_title='Assistência finalização', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Defesas
        top_Defesas = df_filtrado.nlargest(5, 'Defesa')
        fig_Defesas = px.bar(top_Defesas, x='Jogador', y='Defesa', text_auto=True, title='Top Nº de Defesas')
        fig_Defesas.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Defesas.update_layout(yaxis_title='Defesa', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Defesa difícil
        top_Defesa_difícil = df_filtrado.nlargest(5, 'Defesa difícil')
        fig_Defesa_difícil = px.bar(top_Defesa_difícil, x='Jogador', y='Defesa difícil', text_auto=True, title='Top Nº de Defesa difícil')
        fig_Defesa_difícil.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Defesa_difícil.update_layout(yaxis_title='Defesa difícil', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Faltas cometidas
        top_Falta_cometida = df_filtrado.nlargest(5, 'Falta cometida')
        fig_Falta_cometida = px.bar(top_Falta_cometida, x='Jogador', y='Falta cometida', text_auto=True, title='Top Nº de Faltas cometidas')
        fig_Falta_cometida.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Falta_cometida.update_layout(yaxis_title='Falta cometida', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Faltas recebidas
        top_Falta_recebida = df_filtrado.nlargest(5, 'Falta recebida')
        fig_Falta_recebida = px.bar(top_Falta_recebida, x='Jogador', y='Falta recebida', text_auto=True, title='Top Nº de Faltas recebidas')
        fig_Falta_recebida.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Falta_recebida.update_layout(yaxis_title='Falta recebida', xaxis_title='Jogadores')  # Adicionar rótulos

    
        # Para o gráfico de Cartões Vermelhos
        top_Cartão_vermelho = df_filtrado.nlargest(5, 'Cartão vermelho')
        fig_Cartão_vermelho = px.bar(top_Cartão_vermelho, x='Jogador', y='Cartão vermelho', text_auto=True, title='Top Nº de Cartões Vermelhos')
        fig_Cartão_vermelho.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Cartão_vermelho.update_layout(yaxis_title='Cartão vermelho', xaxis_title='Jogadores')  # Adicionar rótulos

        # Para o gráfico de Cartões Amarelos
        top_Cartão_amarelo = df_filtrado.nlargest(5, 'Cartão amarelo')
        fig_Cartão_amarelo = px.bar(top_Cartão_amarelo, x='Jogador', y='Cartão amarelo', text_auto=True, title='Top Nº de Cartões Amarelos')
        fig_Cartão_amarelo.update_traces(marker_color='#023047')  # Adicionar cor personalizada
        fig_Cartão_amarelo.update_layout(yaxis_title='Cartão amarelo', xaxis_title='Jogadores')  # Adicionar rótulos

        st.plotly_chart(fig_Jogos,use_container_width= True)
        st.plotly_chart(fig_passeerrado,use_container_width= True)
        st.plotly_chart(fig_Finalizacao_errada,use_container_width= True)
        st.plotly_chart(fig_Cruzamentos_errados,use_container_width= True)
        st.plotly_chart(fig_Drible_errado,use_container_width= True)
        st.plotly_chart(fig_Virada_errada,use_container_width= True)
        st.plotly_chart(fig_Assistência_gol,use_container_width= True)
        st.plotly_chart(fig_Defesas,use_container_width= True)
        st.plotly_chart(fig_Falta_cometida,use_container_width= True)
        st.plotly_chart(fig_Assistência_gol,use_container_width= True)
        st.plotly_chart(fig_Cartão_vermelho,use_container_width= True)

    with col2:
        st.plotly_chart(fig_Passe,use_container_width= True)
        st.plotly_chart(fig_Finalizacao_certa,use_container_width= True)
        st.plotly_chart(fig_Cruzamento_certo,use_container_width= True)
        st.plotly_chart(fig_Drible_certo,use_container_width= True)
        st.plotly_chart(fig_Virada_certa,use_container_width= True)
        st.plotly_chart(fig_Gols,use_container_width= True)
        st.plotly_chart(fig_Assistência_finalização,use_container_width= True)
        st.plotly_chart(fig_Defesa_difícil,use_container_width= True)
        st.plotly_chart(fig_Falta_recebida,use_container_width= True)
        st.plotly_chart(fig_Assistência_finalização,use_container_width= True)
        st.plotly_chart(fig_Cartão_amarelo,use_container_width= True)

with abas[3]:
    st.header("Top 10 Jogadores Similares")

    
    # Criar um filtro para o clube
    clube = st.selectbox("Selecione o Clube:", dados_footstats['Equipe'].unique())

# Filtrar os dados pelo clube selecionado
    dados_clube = dados_footstats[dados_footstats['Equipe'] == clube]

# Agora, criar um seletor de jogador baseado no filtro do clube
    jogador = st.selectbox("Selecione o Jogador:", dados_clube['Jogador'].unique())
    

    # Se o usuário selecionou um jogador e um clube, executa a função `top10_`
    if (jogador != '') & (clube != ''):
        resultado = top10_(jogador, clube)
    st.dataframe(resultado)

with abas[4]:

   # Filtrar os dados onde 'Posição' é igual a 1
    times_campeoes = hist[hist['Posição'] == 1]

    # Contar a quantidade de vezes que cada time ficou na posição 1
    contagem_times = times_campeoes['Time'].value_counts().reset_index()
    contagem_times.columns = ['Time', 'Quantidade']

    # Ordenar os times pelo número de vezes que ficaram na posição 1
    contagem_times = contagem_times.sort_values(by='Quantidade', ascending=False)

    # Criar o gráfico com o Plotly
    fig = px.bar(contagem_times, x='Time', y='Quantidade', text='Quantidade', title='Times Campeões',
                labels={'Time': 'Time', 'Quantidade': 'Quantidade'})

    # Personalizar cores
    fig.update_traces(marker_color='#023047')

    # Adicionar rótulos
    fig.update_layout(yaxis_title='Quantidade', xaxis_title='Time')

    # Criar um filtro para temporada
    temp = st.selectbox("Selecione a Temporada:", hist['season'].unique())

    # Filtrar os dados pela temporada selecionada e remover a coluna 'season'
    hist_filtrado = hist[hist['season'] == temp].drop(columns=['season']).reset_index(drop=True)

    # Função para calcular o percentual
    def calcular_percentual(df):
        total_jogos = df['Vitórias'].sum() + df['Empates'].sum() + df['Derrotas'].sum()
        df['Percentual_vitórias'] = df['Vitórias'] / total_jogos
        df['Percentual_empates'] = df['Empates'] / total_jogos
        df['Percentual_derrotas'] = df['Derrotas'] / total_jogos
        return df

    # Exibir os gráficos
    

    # Exibir a tabela completa
    st.table(hist_filtrado)
    st.plotly_chart(fig)

    # Filtrar os dados pelo clube selecionado
    clube_selecionado = st.selectbox("Selecione o Clube:", hist['Time'].unique())

    # Filtrar os dados pelo clube selecionado
    dados_clube = hist[hist['Time'] == clube_selecionado]

    # Gráfico de linha para mostrar a posição do clube ao longo das temporadas
    fig_posicao = px.line(dados_clube, x='season', y='Posição', title=f'Posição do {clube_selecionado} ao Longo das Temporadas')

    # Calcular o número e percentual de vitórias, empates e derrotas
    dados_clube_agrupados = dados_clube.groupby('season').agg({'Vitórias':'sum', 'Empates':'sum', 'Derrotas':'sum'})
    dados_clube_agrupados = calcular_percentual(dados_clube_agrupados)

    # Gráfico de barra para mostrar o número de vitórias, empates e derrotas
    fig_resultados = px.bar(dados_clube_agrupados, x=dados_clube_agrupados.index, y=['Vitórias', 'Empates', 'Derrotas'], 
                            title=f'Número de Vitórias, Empates e Derrotas do {clube_selecionado} por Temporada')

    # Gráfico de linha para mostrar o percentual de vitórias, empates e derrotas
    fig_percentual = px.line(dados_clube_agrupados, x=dados_clube_agrupados.index, y=['Percentual_vitórias', 'Percentual_empates', 'Percentual_derrotas'], 
                            title=f'Percentual de Vitórias, Empates e Derrotas do {clube_selecionado} por Temporada')

    # Gráfico de barras para mostrar a quantidade de gols pró e gols contra
    fig_gols = px.bar(dados_clube, x='season', y=['Gols Pró', 'Gols Contra'], 
                    title=f'Quantidade de Gols Pró e Contra do {clube_selecionado} por Temporada')
    
    # Organizar os gráficos em duas colunas
    col1, col2 = st.columns(2)

    # Exibir os gráficos na primeira coluna
    col1.plotly_chart(fig_posicao)
    col1.plotly_chart(fig_resultados)

    # Exibir os gráficos na segunda coluna
    col2.plotly_chart(fig_percentual)
    col2.plotly_chart(fig_gols)






