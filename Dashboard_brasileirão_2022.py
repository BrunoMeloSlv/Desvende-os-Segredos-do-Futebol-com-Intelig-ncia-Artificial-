#Selecione o folder
#.\footstats\Scripts\activate
#streamlit run footstats_st.py

import streamlit as st
import pandas as pd #pandas==2.0.2
import plotly.express as px #plotly==5.15.0
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
from factor_analyzer.factor_analyzer import calculate_kmo
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances

st.set_page_config(layout = 'wide')


st.title('Dashboard Brasileirão 2022 ⚽')


url = 'https://raw.githubusercontent.com/BrunoMeloSlv/dashboard_vendas/main/dados_footstat_2022.csv'
dados = pd.read_csv(url, sep=';')



st.sidebar.title('Filtros')



filtro_equipe = st.sidebar.multiselect('Equipe', dados['Equipe'].unique())
if filtro_equipe:
    dados = dados[dados['Equipe'].isin(filtro_equipe)]

filtro_jogador = st.sidebar.multiselect('Jogador', dados['Jogador'].unique())
if filtro_jogador:
    dados = dados[dados['Jogador'].isin(filtro_jogador)]



#### Tabelas

#Jogador

jogos =  dados[['Equipe','Jogador','Jogos']].reset_index().sort_values('Jogos', ascending=False)
Passe =  dados[['Equipe','Jogador','Passe certo']].reset_index().sort_values('Passe certo', ascending=False)
Finalização =  dados[['Equipe','Jogador','Finalização certa']].reset_index().sort_values('Finalização certa', ascending=False)
Desarme =  dados[['Equipe','Jogador','Desarme certo']].reset_index().sort_values('Desarme certo', ascending=False)
Cruzamento =  dados[['Equipe','Jogador','Cruzamento certo']].reset_index().sort_values('Cruzamento certo', ascending=False)
Interceptação =  dados[['Equipe','Jogador','Interceptação certa']].reset_index().sort_values('Interceptação certa', ascending=False)
Dribles =  dados[['Equipe','Jogador','Dribles']].reset_index().sort_values('Dribles', ascending=False)
Virada  =  dados[['Equipe','Jogador','Virada de jogo certa']].reset_index().sort_values('Virada de jogo certa', ascending=False)
Gols =  dados[['Equipe','Jogador','Gols']].reset_index().sort_values('Gols', ascending=False)
Assistência_gol =  dados[['Equipe','Jogador','Assistência gol']].reset_index().sort_values('Assistência gol', ascending=False)
Assistência_finalização =  dados[['Equipe','Jogador','Assistência finalização']].reset_index().sort_values('Assistência finalização', ascending=False)
Defesa =  dados[['Equipe','Jogador','Defesa']].reset_index().sort_values('Defesa', ascending=False)
Defesa_difícil =  dados[['Equipe','Jogador','Defesa difícil']].reset_index().sort_values('Defesa difícil', ascending=False)
Rebatida =  dados[['Equipe','Jogador','Rebatida']].reset_index().sort_values('Rebatida', ascending=False)
Falta_cometida =  dados[['Equipe','Jogador','Falta cometida']].reset_index().sort_values('Falta cometida', ascending=False)
Falta_recebida =  dados[['Equipe','Jogador','Falta recebida']].reset_index().sort_values('Falta recebida', ascending=False)
Impedimentos =  dados[['Equipe','Jogador','Impedimentos']].reset_index().sort_values('Impedimentos', ascending=False)
Pênaltis_sofridos =  dados[['Equipe','Jogador','Pênaltis sofridos']].reset_index().sort_values('Pênaltis sofridos', ascending=False)
Pênaltis_cometidos =  dados[['Equipe','Jogador','Pênaltis cometidos']].reset_index().sort_values('Pênaltis cometidos', ascending=False)
Perda_da_posse =  dados[['Equipe','Jogador','Perda da posse de bola']].reset_index().sort_values('Perda da posse de bola', ascending=False)
Cartão_vermelho =  dados[['Equipe','Jogador','Cartão vermelho']].reset_index().sort_values('Cartão vermelho', ascending=False)
Cartão_amarelo =  dados[['Equipe','Jogador','Cartão amarelo']].reset_index().sort_values('Cartão amarelo', ascending=False)

# Times

time_passes = pd.DataFrame(dados.groupby('Equipe')['Passe certo'].sum()).reset_index().sort_values('Passe certo', ascending=False)
time_Finalização = pd.DataFrame(dados.groupby('Equipe')['Finalização certa'].sum()).reset_index().sort_values('Finalização certa', ascending=False)
time_desarmes = pd.DataFrame(dados.groupby('Equipe')['Desarme certo'].sum()).reset_index().sort_values('Desarme certo', ascending=False)
time_Cruzamento = pd.DataFrame(dados.groupby('Equipe')['Cruzamento certo'].sum()).reset_index().sort_values('Cruzamento certo', ascending=False)
time_Interceptação = pd.DataFrame(dados.groupby('Equipe')['Interceptação certa'].sum()).reset_index().sort_values('Interceptação certa', ascending=False)
time_Dribles = pd.DataFrame(dados.groupby('Equipe')['Dribles'].sum()).reset_index().sort_values('Dribles', ascending=False)
time_Virada = pd.DataFrame(dados.groupby('Equipe')['Virada de jogo certa'].sum()).reset_index().sort_values('Virada de jogo certa', ascending=False)
time_Gols = pd.DataFrame(dados.groupby('Equipe')['Gols'].sum()).reset_index().sort_values('Gols', ascending=False)
time_Assistência_gol = pd.DataFrame(dados.groupby('Equipe')['Assistência gol'].sum()).reset_index().sort_values('Assistência gol', ascending=False)
time_Assistência_finalização = pd.DataFrame(dados.groupby('Equipe')['Assistência finalização'].sum()).reset_index().sort_values('Assistência finalização', ascending=False)
time_Defesa = pd.DataFrame(dados.groupby('Equipe')['Defesa'].sum()).reset_index().sort_values('Defesa', ascending=False)
time_Defesa_difícil = pd.DataFrame(dados.groupby('Equipe')['Defesa difícil'].sum()).reset_index().sort_values('Defesa difícil', ascending=False)
time_Rebatida = pd.DataFrame(dados.groupby('Equipe')['Rebatida'].sum()).reset_index().sort_values('Rebatida', ascending=False)
time_Falta_cometida = pd.DataFrame(dados.groupby('Equipe')['Falta cometida'].sum()).reset_index().sort_values('Falta cometida', ascending=False)
time_Falta_recebida = pd.DataFrame(dados.groupby('Equipe')['Falta recebida'].sum()).reset_index().sort_values('Falta recebida', ascending=False)
time_Impedimentos = pd.DataFrame(dados.groupby('Equipe')['Impedimentos'].sum()).reset_index().sort_values('Impedimentos', ascending=False)
time_Pênaltis_sofridos = pd.DataFrame(dados.groupby('Equipe')['Pênaltis sofridos'].sum()).reset_index().sort_values('Pênaltis sofridos', ascending=False)
time_Pênaltis_cometidos = pd.DataFrame(dados.groupby('Equipe')['Pênaltis cometidos'].sum()).reset_index().sort_values('Pênaltis cometidos', ascending=False)
time_Cartão_vermelho = pd.DataFrame(dados.groupby('Equipe')['Cartão vermelho'].sum()).reset_index().sort_values('Cartão vermelho', ascending=False)
time_Cartão_amarelo = pd.DataFrame(dados.groupby('Equipe')['Cartão amarelo'].sum()).reset_index().sort_values('Cartão amarelo', ascending=False)

dados_agrupados = pd.merge(time_Finalização, time_Gols, left_on = 'Equipe', right_on = 'Equipe')


### Gráficos

### Jogador

fig_Jogos = px.bar(jogos.head(),
                             x = 'Jogador',
                             y = 'Jogos',
                             text_auto= True,
                             title= 'Top Nº de Jogos')
fig_Jogos.update_layout(yaxis_title = 'Jogos')

fig_Passe = px.bar(Passe.head(),
                             x = 'Jogador',
                             y = 'Passe certo',
                             text_auto= True,
                             title= 'Top Nº de Passes certos')
fig_Passe.update_layout(yaxis_title = 'Passes certos')

fig_Finalização = px.bar(Finalização.head(),
                             x = 'Jogador',
                             y = 'Finalização certa',
                             text_auto= True,
                             title= 'Top Nº de Finalizações certas')
fig_Finalização.update_layout(yaxis_title = 'Finalizações certas')

fig_Desarme = px.bar(Desarme.head(),
                             x = 'Jogador',
                             y = 'Desarme certo',
                             text_auto= True,
                             title= 'Top Nº de Desarmes certos')
fig_Desarme.update_layout(yaxis_title = 'Desarmes certos')

fig_Cruzamento = px.bar(Cruzamento.head(),
                             x = 'Jogador',
                             y = 'Cruzamento certo',
                             text_auto= True,
                             title= 'Top Nº de Cruzamentos certos')
fig_Cruzamento.update_layout(yaxis_title = 'Cruzamentos certos')

fig_Interceptação = px.bar(Interceptação.head(),
                             x = 'Jogador',
                             y = 'Interceptação certa',
                             text_auto= True,
                             title= 'Top Nº de Interceptações certas')
fig_Interceptação.update_layout(yaxis_title = 'Interceptações certas')

fig_Dribles = px.bar(Dribles.head(),
                             x = 'Jogador',
                             y = 'Dribles',
                             text_auto= True,
                             title= 'Top Nº de Dribles certos')
fig_Dribles.update_layout(yaxis_title = 'Dribles certos')

fig_Virada = px.bar(Virada.head(),
                             x = 'Jogador',
                             y = 'Virada de jogo certa',
                             text_auto= True,
                             title= 'Top Nº de Viradas de jogo certas')
fig_Virada.update_layout(yaxis_title = 'Viradas de jogo')

fig_Gols = px.bar(Gols.head(),
                             x = 'Jogador',
                             y = 'Gols',
                             text_auto= True,
                             title= 'Top Nº de Gols')
fig_Gols.update_layout(yaxis_title = 'Gols')

fig_Assistências_Gols = px.bar(Assistência_gol.head(),
                             x = 'Jogador',
                             y = 'Assistência gol',
                             text_auto= True,
                             title= 'Top Nº de Assistências para gol')
fig_Assistências_Gols.update_layout(yaxis_title = 'Assistências')

fig_Assistência_finalização = px.bar(Assistência_finalização.head(),
                             x = 'Jogador',
                             y = 'Assistência finalização',
                             text_auto= True,
                             title= 'Top Nº de Assistências para finalização')
fig_Assistência_finalização.update_layout(yaxis_title = 'Assistência finalização')

fig_Defesa_difícil = px.bar(Defesa_difícil.head(),
                             x = 'Jogador',
                             y = 'Defesa difícil',
                             text_auto= True,
                             title= 'Top Nº de Defesas difíceis')
fig_Defesa_difícil.update_layout(yaxis_title = 'Defesas')

fig_Defesa = px.bar(Defesa.head(),
                             x = 'Jogador',
                             y = 'Defesa',
                             text_auto= True,
                             title= 'Top Nº de Defesas')
fig_Defesa.update_layout(yaxis_title = 'Defesa')

fig_Rebatida = px.bar(Rebatida.head(),
                             x = 'Jogador',
                             y = 'Rebatida',
                             text_auto= True,
                             title= 'Top Nº de Rebatidas')
fig_Rebatida.update_layout(yaxis_title = 'Rebatida')

fig_Falta_cometida = px.bar(Falta_cometida.head(),
                             x = 'Jogador',
                             y = 'Falta cometida',
                             text_auto= True,
                             title= 'Top Nº de Faltas cometidas')
fig_Falta_cometida.update_layout(yaxis_title = 'Faltas')

fig_Falta_recebida = px.bar(Falta_recebida.head(),
                             x = 'Jogador',
                             y = 'Falta recebida',
                             text_auto= True,
                             title= 'Top Nº de Faltas recebidas')
fig_Falta_recebida.update_layout(yaxis_title = 'Faltas')

fig_Impedimentos = px.bar(Impedimentos.head(),
                             x = 'Jogador',
                             y = 'Impedimentos',
                             text_auto= True,
                             title= 'Top Nº de Impedimentos')
fig_Impedimentos.update_layout(yaxis_title = 'Impedimentos')

fig_Pênaltis_sofridos = px.bar(Pênaltis_sofridos.head(),
                             x = 'Jogador',
                             y = 'Pênaltis sofridos',
                             text_auto= True,
                             title= 'Top Nº de Pênaltis sofridos')
fig_Pênaltis_sofridos.update_layout(yaxis_title = 'Pênaltis')

fig_Pênaltis_cometidos = px.bar(Pênaltis_cometidos.head(),
                             x = 'Jogador',
                             y = 'Pênaltis cometidos',
                             text_auto= True,
                             title= 'Top Nº de Pênaltis cometidos')
fig_Pênaltis_cometidos.update_layout(yaxis_title = 'Pênaltis')

fig_Perda_da_posse = px.bar(Perda_da_posse.head(),
                             x = 'Jogador',
                             y = 'Perda da posse de bola',
                             text_auto= True,
                             title= 'Top Nº de Perda da posse de bola')
fig_Perda_da_posse.update_layout(yaxis_title = 'Perda de Posse')

fig_Cartão_vermelho = px.bar(Cartão_vermelho.head(),
                             x = 'Jogador',
                             y = 'Cartão vermelho',
                             text_auto= True,
                             title= 'Top Nº de Cartões vermelhos')
fig_Cartão_vermelho.update_layout(yaxis_title = 'Cartões vermelhos')

fig_Cartão_amarelo = px.bar(Cartão_amarelo.head(),
                             x = 'Jogador',
                             y = 'Cartão amarelo',
                             text_auto= True,
                             title= 'Top Nº de Cartões amarelos')
fig_Cartão_amarelo.update_layout(yaxis_title = 'Cartões amarelos')

## Times

fig_teste =  px.scatter(data_frame = dados_agrupados, x = 'Finalização certa', y = 'Gols', text = 'Equipe', size = 'Gols')
fig_teste.update_layout(yaxis_title = 'Finalização x Gols')

fig_time_passes = px.bar(time_passes.head(),
                             x = 'Equipe',
                             y = 'Passe certo',
                             text_auto= True,
                             title= 'Top Nº de Passes certos')
fig_time_passes.update_layout(yaxis_title = 'Passes certos')


fig_time_Finalização = px.bar(time_Finalização.head(),
                             x = 'Equipe',
                             y = 'Finalização certa',
                             text_auto= True,
                             title= 'Top Nº de Finalizações certas')
fig_time_Finalização.update_layout(yaxis_title = 'Finalizações')

fig_time_Desarme = px.bar(time_desarmes.head(),
                             x = 'Equipe',
                             y = 'Desarme certo',
                             text_auto= True,
                             title= 'Top Nº de Desarmes certos')
fig_time_Desarme.update_layout(yaxis_title = 'Desarmes certos')

fig_time_Cruzamento = px.bar(time_Cruzamento.head(),
                             x = 'Equipe',
                             y = 'Cruzamento certo',
                             text_auto= True,
                             title= 'Top Nº de Cruzamentos certos')
fig_time_Cruzamento.update_layout(yaxis_title = 'Cruzamentos certos')

fig_time_Interceptação = px.bar(time_Interceptação.head(),
                             x = 'Equipe',
                             y = 'Interceptação certa',
                             text_auto= True,
                             title= 'Top Nº de Interceptações certas')
fig_time_Interceptação.update_layout(yaxis_title = 'Interceptações certas')

fig_time_Dribles = px.bar(time_Dribles.head(),
                             x = 'Equipe',
                             y = 'Dribles',
                             text_auto= True,
                             title= 'Top Nº de Dribles certos')
fig_time_Dribles.update_layout(yaxis_title = 'Dribles certos')

fig_time_Virada = px.bar(time_Virada.head(),
                             x = 'Equipe',
                             y = 'Virada de jogo certa',
                             text_auto= True,
                             title= 'Top Nº de Viradas de jogo certas')
fig_time_Virada.update_layout(yaxis_title = 'Viradas de jogo')

fig_time_Gols = px.bar(time_Gols.head(),
                             x = 'Equipe',
                             y = 'Gols',
                             text_auto= True,
                             title= 'Top Nº de Gols')
fig_time_Gols.update_layout(yaxis_title = 'Gols')

fig_time_Assistência_gol = px.bar(time_Assistência_gol.head(),
                             x = 'Equipe',
                             y = 'Assistência gol',
                             text_auto= True,
                             title= 'Top Nº de Assistências para gol')
fig_time_Assistência_gol.update_layout(yaxis_title = 'Assistências')

fig_time_Assistência_finalização = px.bar(time_Assistência_finalização.head(),
                             x = 'Equipe',
                             y = 'Assistência finalização',
                             text_auto= True,
                             title= 'Top Nº de Assistências para finalização')
fig_time_Assistência_finalização.update_layout(yaxis_title = 'Assistência finalização')

fig_time_Defesa_difícil = px.bar(time_Defesa_difícil.head(),
                             x = 'Equipe',
                             y = 'Defesa difícil',
                             text_auto= True,
                             title= 'Top Nº de Defesas difíceis')
fig_time_Defesa_difícil.update_layout(yaxis_title = 'Defesas')

fig_time_Defesa = px.bar(time_Defesa.head(),
                             x = 'Equipe',
                             y = 'Defesa',
                             text_auto= True,
                             title= 'Top Nº de Defesas')
fig_time_Defesa.update_layout(yaxis_title = 'Defesa')

fig_time_Rebatida = px.bar(time_Rebatida.head(),
                             x = 'Equipe',
                             y = 'Rebatida',
                             text_auto= True,
                             title= 'Top Nº de Rebatidas')
fig_time_Rebatida.update_layout(yaxis_title = 'Rebatida')

fig_time_Falta_cometida = px.bar(time_Falta_cometida.head(),
                             x = 'Equipe',
                             y = 'Falta cometida',
                             text_auto= True,
                             title= 'Top Nº de Faltas cometidas')
fig_time_Falta_cometida.update_layout(yaxis_title = 'Faltas')

fig_time_Falta_recebida = px.bar(time_Falta_recebida.head(),
                             x = 'Equipe',
                             y = 'Falta recebida',
                             text_auto= True,
                             title= 'Top Nº de Faltas recebidas')
fig_time_Falta_recebida.update_layout(yaxis_title = 'Faltas')

fig_time_Impedimentos = px.bar(time_Impedimentos.head(),
                             x = 'Equipe',
                             y = 'Impedimentos',
                             text_auto= True,
                             title= 'Top Nº de Impedimentos')
fig_time_Impedimentos.update_layout(yaxis_title = 'Impedimentos')

fig_time_Pênaltis_sofridos = px.bar(time_Pênaltis_sofridos.head(),
                             x = 'Equipe',
                             y = 'Pênaltis sofridos',
                             text_auto= True,
                             title= 'Top Nº de Pênaltis sofridos')
fig_time_Pênaltis_sofridos.update_layout(yaxis_title = 'Pênaltis')

fig_time_Pênaltis_cometidos = px.bar(time_Pênaltis_cometidos.head(),
                             x = 'Equipe',
                             y = 'Pênaltis cometidos',
                             text_auto= True,
                             title= 'Top Nº de Pênaltis cometidos')
fig_time_Pênaltis_cometidos.update_layout(yaxis_title = 'Pênaltis')

fig_time_Cartão_vermelho = px.bar(time_Cartão_vermelho.head(),
                             x = 'Equipe',
                             y = 'Cartão vermelho',
                             text_auto= True,
                             title= 'Top Nº de Cartões vermelhos')
fig_time_Cartão_vermelho.update_layout(yaxis_title = 'Cartões vermelhos')

fig_time_Cartão_amarelo = px.bar(time_Cartão_amarelo.head(),
                             x = 'Equipe',
                             y = 'Cartão amarelo',
                             text_auto= True,
                             title= 'Top Nº de Cartões amarelos')
fig_time_Cartão_amarelo.update_layout(yaxis_title = 'Cartões amarelos')

##### TCC


def top10_(jogador, clube):

    df = dados

    df_cluster2 = dados.copy()
    df_cluster2 = df_cluster2[df_cluster2['Jogos'] != 0]

    df_cluster_a_padronizar = df_cluster2.copy()
    df_cluster_a_padronizar.drop(columns = ['Equipe','Jogador'], inplace = True)

    sc_X = StandardScaler (with_mean = True , with_std = True )
    df_cluster_padronizado = sc_X.fit_transform (df_cluster_a_padronizar)
    #Converter para o formato de tabela - StandardScaler 
    df_cluster_padronizado = pd.DataFrame (data = df_cluster_padronizado, columns = df_cluster_a_padronizar.columns)
    
    pca = PCA(n_components = 4,  random_state= 1224)
    df_cluster_pca_atacante = pca.fit_transform(df_cluster_padronizado)
    projection = pd.DataFrame( data = df_cluster_pca_atacante)
    kmeans_pca = KMeans(n_clusters= 13, verbose= True, random_state= 1224)
    kmeans_pca.fit(projection)
    projection['cluster_pca'] = kmeans_pca.predict(projection)
    projection['Jogador'] = df['Jogador']
    projection['Equipe'] = df['Equipe']
    projection['jogador/time'] = (projection['Jogador'] + '/' + projection['Equipe']) 

    nome_jogador = jogador + '/' + clube

    cluster = list(projection[projection['jogador/time']== nome_jogador]['cluster_pca'])[0]

    jogador_recomendado = projection[projection['cluster_pca']==cluster][[0,1,2,3,'Jogador','Equipe']] #,5,6,7,8,9,10
    a_jogador = list(projection[projection['jogador/time']== nome_jogador][0])[0]
    b_jogador = list(projection[projection['jogador/time']== nome_jogador][1])[0]
    c_jogador = list(projection[projection['jogador/time']== nome_jogador][2])[0]
    d_jogador = list(projection[projection['jogador/time']== nome_jogador][3])[0]
    distancias = euclidean_distances(jogador_recomendado[[0,1,2,3]], [[a_jogador, b_jogador,c_jogador,d_jogador]]) #,5,6,7,8,9,10 ,e_jogador,f_jogador,g_jogador,h_jogador,i_jogador,j_jogador,k_jogador
    jogador_recomendado['Jogador'] = projection['Jogador']
    jogador_recomendado['distancias'] = distancias
    tabela = jogador_recomendado.sort_values('distancias').head(11)
    dados_jogador = df_cluster2[df_cluster2['Jogador'].isin(tabela['Jogador']) & df_cluster2['Equipe'].isin(tabela['Equipe'])]
    recomendado = pd.merge(tabela, dados_jogador, on=['Equipe','Jogador'], how='inner')

    recomendado = recomendado[list(df_cluster2.columns)]
    recomendado.drop(0, axis= 0, inplace= True)

    jogador_equipe = recomendado[['Jogador','Equipe']]

    positivos  = recomendado[['Jogos', 'Passe certo', 'Finalização certa', 'Desarme certo', 'Cruzamento certo', 'Interceptação certa', 'Dribles', 'Virada de jogo certa', 'Gols', 'Assistência gol', 'Assistência finalização', 
                              'Defesa', 'Rebatida', 'Falta recebida']]


    negativos = recomendado[['Falta cometida', 'Perda da posse de bola']]

    colunas = recomendado[list(positivos.columns)]

    def ahp_positivos(tabela):
        table = []
        for i in colunas:
            a = tabela[i] / sum(tabela[i])
            table.append(a)
        table = pd.DataFrame(table).T
        return table

    positivos = ahp_positivos(positivos)

    def numeros_negativos(tabela):
        table = []
        for i in negativos:
            a = 1 / tabela[i]
            table.append(a)
        table = pd.DataFrame(table).T
        tab_final = []
        for i in table.columns:
            b = table[i] / sum(table[i])
            tab_final.append(b)
        tab_final = pd.DataFrame(tab_final).T
        return tab_final

    negativos = numeros_negativos(negativos)

    tabela_ahp = pd.concat([positivos,negativos], axis=1)

    medias = pd.DataFrame(tabela_ahp.mean(),columns=['media'])
    desvio = pd.DataFrame(tabela_ahp.std(),columns=['desvio'])
    fator_ahp = pd.concat([medias,desvio], axis=1)
    fator_ahp['desvio'] = fator_ahp['desvio'].fillna(np.mean(fator_ahp['desvio']))
    fator_ahp['desvio/media'] = fator_ahp['desvio'] / fator_ahp['media']
    fator_ahp['fator_gaussiano'] = fator_ahp['desvio/media'] / sum(fator_ahp['desvio/media'])
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

    resultado_ahp = matriz_de_decisao(tabela_ahp,fator)

    soma = resultado_ahp.sum(axis=1)
    soma = pd.DataFrame(soma, columns = ['soma'])

    melhores_escolhas = pd.concat([soma,jogador_equipe], axis=1)
    melhores_escolhas = melhores_escolhas.sort_values(by = 'soma', ascending= False)

    return melhores_escolhas

def main():

  # Título da aplicação
  st.title("Top 10 Jogadores Similares")

  # Seleção do jogador
  jogador = st.selectbox("Selecione o Jogador:", dados['Jogador'].unique())

  # Seleção do clube
  clube = st.selectbox("Selecione o Clube:", dados['Equipe'].unique())

  # Se o usuário selecionou um jogador e um clube, executa a função `top10_`
  if (jogador != '') & (clube != ''):
    resultado = top10_(jogador, clube)
    st.dataframe(resultado)

if __name__ == "__main__":
  main()



## Visualização
aba1, aba2= st.tabs(['Jogador', 'Times'])
with aba1:
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_Jogos,use_container_width= True)
        st.plotly_chart(fig_Finalização,use_container_width= True)
        st.plotly_chart(fig_Cruzamento,use_container_width= True)
        st.plotly_chart(fig_Dribles,use_container_width= True)
        st.plotly_chart(fig_Gols,use_container_width= True)
        st.plotly_chart(fig_Assistência_finalização,use_container_width= True)
        st.plotly_chart(fig_Defesa,use_container_width= True)
        st.plotly_chart(fig_Falta_cometida,use_container_width= True)
        st.plotly_chart(fig_Impedimentos,use_container_width= True)
        st.plotly_chart(fig_Pênaltis_cometidos,use_container_width= True)
        st.plotly_chart(fig_Cartão_vermelho,use_container_width= True)

    with col2:
        st.plotly_chart(fig_Passe,use_container_width= True)
        st.plotly_chart(fig_Desarme,use_container_width= True)
        st.plotly_chart(fig_Interceptação,use_container_width= True)
        st.plotly_chart(fig_Virada,use_container_width= True)
        st.plotly_chart(fig_Assistências_Gols,use_container_width= True)
        st.plotly_chart(fig_Defesa_difícil,use_container_width= True)
        st.plotly_chart(fig_Rebatida,use_container_width= True)
        st.plotly_chart(fig_Falta_recebida,use_container_width= True)
        st.plotly_chart(fig_Pênaltis_sofridos,use_container_width= True)
        st.plotly_chart(fig_Perda_da_posse,use_container_width= True)
        st.plotly_chart(fig_Cartão_amarelo,use_container_width= True)

with aba2:
    col1, col2 = st.columns(2)
    with col1:
       st.plotly_chart(fig_time_passes,use_container_width= True)
       st.plotly_chart(fig_time_Desarme,use_container_width= True)
       st.plotly_chart(fig_time_Interceptação,use_container_width= True)
       st.plotly_chart(fig_time_Assistência_gol,use_container_width= True)
       st.plotly_chart(fig_time_Defesa_difícil,use_container_width= True)
       st.plotly_chart(fig_time_Rebatida,use_container_width= True)
       st.plotly_chart(fig_time_Falta_recebida,use_container_width= True)
       st.plotly_chart(fig_time_Impedimentos,use_container_width= True)
       st.plotly_chart(fig_time_Pênaltis_cometidos,use_container_width= True)
       st.plotly_chart(fig_time_Cartão_amarelo,use_container_width= True)
       st.plotly_chart(fig_teste,use_container_width= True)
       
    with col2:
        st.plotly_chart(fig_time_Finalização,use_container_width= True)
        st.plotly_chart(fig_time_Cruzamento,use_container_width= True)
        st.plotly_chart(fig_time_Dribles,use_container_width= True)
        st.plotly_chart(fig_time_Gols,use_container_width= True)
        st.plotly_chart(fig_time_Assistência_finalização,use_container_width= True)
        st.plotly_chart(fig_time_Defesa,use_container_width= True)
        st.plotly_chart(fig_time_Falta_cometida,use_container_width= True)
        st.plotly_chart(fig_time_Impedimentos,use_container_width= True)
        st.plotly_chart(fig_time_Pênaltis_sofridos,use_container_width= True)
        st.plotly_chart(fig_time_Cartão_vermelho,use_container_width= True)


