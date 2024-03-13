# Desvende os Segredos do Futebol com Inteligência Artificial!

#### Links:
##### Instagram: https://www.instagram.com/brunomelods/
##### Youtube: https://www.youtube.com/channel/UCn89B2mZDj4mq6iP5wueHMA
##### Linkedin: https://www.linkedin.com/in/bruno-melo-223817125/
##### Vídeo explicando toda metodologia: https://www.youtube.com/watch?v=bZSOfVIRqNo&t=1s
##### App: https://skby9wg9tzx3n6t9uljxqt.streamlit.app/

## Método AHP (Analytic Hierarchy Process – Gaussiano) na Determinação da Contratação de um Jogador de Futebol

### Resumo:

O estudo aborda uma pesquisa que utiliza o método AHP, um processo analítico 
hierárquico, com uma abordagem gaussiana, para auxiliar na tomada de decisões 
relacionadas à contratação de jogadores de futebol. Esse TCC investiga como essa 
metodologia pode ser aplicada de maneira eficaz no contexto do futebol, considerando 
diversas variáveis e critérios relevantes para avaliar o desempenho de jogadores e determinar 
quais deles são os mais adequados para uma equipe. O estudo visa aprimorar o processo de 
seleção de jogadores e contribuir para uma gestão mais eficiente de recursos em clubes de 
futebol, promovendo uma abordagem mais científica e precisa na contratação de talentos 
esportivos. Ele emprega uma abordagem estatística que começa com a Análise de 
Componentes Principais (PCA) com o objetivo de reduzir a complexidade dos dados, 
reduzindo 22 variáveis para apenas 4, as quais representam 70,28% da informação total. Em 
seguida, é realizada uma análise de clusters para agrupar jogadores com estatísticas 
semelhantes, resultando em 13 clusters identificados pelo método Elbow. Após a conclusão 
das etapas de redução de dimensionalidade e agrupamento, o foco se volta para a tomada 
de decisão em relação aos jogadores que apresentam maior similaridade. Para determinar a 
melhor escolha entre esses jogadores, é aplicado o método AHP Gaussiano. Como exemplo, 
ao analisar o jogador Dudu do Palmeiras, observou-se que, com base na metodologia e nos 
dados utilizados, Carlos de Pena do Internacional emerge como o substituto mais indicado, 
devido à maior proximidade identificada.

Palavras-chave: Ciência de Dados; Futebol; Análise de Dados no Futebol; AHP Gaussiano; 
Análise de Cluster;

## AHP Method (Analytic Hierarchy Process - Gaussian) in Determining the Hiring of a Soccer Player

### Abstract:

The study addresses research that employs the Analytic Hierarchy Process (AHP), a 
hierarchical analytical method, with a Gaussian approach, to assist in decision-making related 
to the recruitment of soccer players. This thesis investigates how this methodology can be 
effectively applied in the context of soccer, considering various variables and relevant criteria 
to evaluate player performance and determine which ones are most suitable for a team. The 
study aims to enhance the player selection process and contribute to more efficient resource 
management in football clubs, promoting a more scientific and precise approach to recruiting 
sports talent. It employs a statistical approach that begins with Principal Component Analysis 
(PCA) to reduce data complexity, reducing 22 variables to just 4, which represent 70.28% of 
the total information. Subsequently, cluster analysis is conducted to group players with similar 
statistics, resulting in 13 clusters identified by the Elbow method. After completing the steps of 
dimensionality reduction and clustering, the focus shifts to decision-making regarding players 
with greater similarity. To determine the best choice among these players, the Gaussian AHP 
method is applied. For example, when analyzing the Palmeiras player Dudu, it was observed 
that, based on the methodology and data used, Carlos de Pena from Internacional emerges 
as the most suitable substitute due to the higher proximity identified.

Keywords: Data Science; Soccer; Data Analysis in Soccer; Gaussian AHP; Cluster 
Analysis

#### Introdução

A preocupação em atribuir sentido ao mundo é a maior excitação cientifica estudada 
pelo meio acadêmico e na era da informação, onde é disseminada mais informações do que 
podemos consumir em que é possível encontrar dados sobre os mais diversos temas somente 
pesquisando na internet. Seria uma afronta não pesquisar sobre os temas mais relevantes do 
mundo e o futebol é o esporte mais disseminado do planeta.
O futebol é o esporte que faz o telespectador sentir todos os sentimentos conhecidos 
pela humanidade em cerca de noventa minutos, o público fica em uma espécie de transe 
durante aquele momento. Um jogo de futebol é um jogo de passagem para frente e movimento 
para frente. O ataque é o eterno tema do futebol. Ganhar um gol é a essência de um jogo de 
futebol (WU, 2022).

E plausível entender que uma pessoa seja balizada pelo seu achismo para que em 
uma conversa com os amigos demonstre sua visão do jogo que ele assistiu. Porém quando 
falamos de um clube de futebol, comparando com uma empresa, não pode ser admitido que 
as decisões sejam baseadas em achismo de forma amadora como se um torcedor em uma 
mesa de bar julga o seu time, o Nelson Rodrigues diz: “Em futebol, o pior cego é o que só vê 
a bola”.

Essa citação do dramaturgo e cronista Nelson Rodrigues é lugar-comum na produção 
dos estudos sociais sobre o futebol. A máxima do escritor, porém, serve de lembrança sobre 
como tal prática cultural e esportiva coloca muito mais em jogo do que uma mera esfera de 
borracha e couro. Nessa perspectiva, não é de se estranhar como, desde os primeiros estudos 
nacionais sobre o futebol, seus autores buscaram, partindo do esporte como objeto de 
investigação, responder a questões centrais da realidade brasileira (RIBEIRO,2022).
Apesar de ser o esporte mais popular do país, o futebol sofre com problemas 
estruturais. Profissionais de marketing pouco sabem sobre os fatores que determinam 
variáveis de desempenho. Pesquisas existentes são desenvolvidas segundo uma lógica 
estritamente econômica, atribuindo importância a uma variável dependente apenas, o público 
total das partidas (ALMEIDA, COELHO, OLIVEIRA, CAMARGO, & SAVIOLI, 2020).
A estatística por sua vez vem contribuir provando estudos através de testes elaborados 
com amostras e hipóteses pelos acadêmicos. Estudos na área de Educação Matemática têm 
evidenciado a pertinência de o ensino de Estatística ser baseado no desenvolvimento de 
pesquisas, visando proporcionar aos alunos criticidade na análise e interpretação de dados 
para tomada de decisões (BARRETO, MENDONÇA, FARIAS, & OLIVEIRA, 2022).
Nesse prisma, os sistemas educativos são direcionados a redefinir seus objetivos e 
funções a fim de que os futuros profissionais tenham os conhecimentos, as habilidades, as 
atitudes e os valores pautados em uma aprendizagem permanente e crítica que permeie a 
busca, a organização, a interpretação, a avaliação e o uso da informação para que 
compreendam fenômenos, empoderem suas atitudes e tomem decisões no contexto do 
mundo do trabalho.

No contexto atual parece racional tomar atitudes baseado em dados na tentativa de 
minimizar os erros e no futebol não pode ser diferente (SANTOS,Camila & SANTOS, Vanessa 
2022).

No estudo em questão foi utilizado uma pesquisa operacional, é uma metodologia que 
iniciou com o objetivo de auxiliar tomadas de decisões militares durante a segunda guerra 
mundial. Em razão da Guerra havia a necessidade de alocar eficientemente os escassos 
recursos para diversas operações militares (BARROSO,2021).

Ainda segundo (Barroso,2021), a Pesquisa Operacional (P.O) está relacionada com 
tudo ao nosso redor e na nossa vida, seja na tomada de decisão, seja no setor logístico, seja 
em uma área de produção de uma empresa, ela está relacionada a todas as áreas de vastos 
conhecimentos.

O propósito desta pesquisa consistiu em identificar o jogador mais adequado, cujo 
perfil atendesse aos critérios estabelecidos, por meio da aplicação do método AHP 
Gaussiano. Nesse sentido, um diretor esportivo pode definir o perfil de jogador que deseja 
recrutar para a sua equipe e, por meio deste algoritmo, obter uma lista das 10 opções mais 
alinhadas com o perfil desejado. Com a assistência da técnica de pesquisa operacional, é 
então possível estabelecer um ranking das alternativas mais vantajosas a serem 
consideradas.

#### Material e Métodos

Foi utilizada outras duas técnicas a análise de componentes principais (PCA) que tem 
por objetivo descobrir o modo como as variáveis covariam. Ou melhor, é um método que se 
baseia em criação de fatores não correlacionados.
Antes de ser utilizado os métodos propostos aqui, para a PCA e K-means, os dados 
foram padronizados baseados na Z scorre, logo cada variável terá média tendendo a 0 e 
desvio padrão a 1.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/695ac472-07eb-42a1-82b0-3f23afd84d5a)

A PCA assim como o método de clustering está dentro dos modelos não 
supervisionados de Machine Learning (ML), ou seja, ela não tem caráter preditivo e por este 
motivo ela não trabalha com novos dados fora das observações atuais, visto que encontrou 
novas observações o método deve ser gerado novamente.

A análise utiliza-se da existência de correlação das variáveis originais para uma 
posterior criação de fatores. Neste momento foi a Correlação de Pearson (r) que verifica a 
relação linear entre duas variáveis métricas e que pode variar (-1; +1), quando utilizada em 
outras metodologias os valores mais extremos significam uma relação perfeita negativa ou 
positiva a depender do sinal indicado. 

Aqui os valores extremos irão indicar a extração de um único fator devido a existência 
de relação entre as varáveis. Enquanto mais próximo ao zero propicia a extração de fatores 
diferente indicando inexistência de relação entre as variáveis.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/9259f472-7e34-4e71-9c7a-61baa67033f1)

Para verificar que os dados estão aptos para a análise fatorial, deve-se investigar a 
adequação global da análise fatorial e para isso foi utilizado a estatística de Kaiser-MeyerOlkin (KMO) e o teste de esfericidade de Bartlett.

Para o KMO, indica a proporção de variância que foi atribuída a um fator comum de 
todas as variáveis em análise. E uma estatística que varia entre 0 e 1, o valor mais próximo 
ao 1 indica que análise fatorial pode ser adequada e as variáveis compartilham alta variância. 
Deste modo espera-se um valor maior que 0,8 para ser considerar que indica o 
prosseguimento do modelo proposto.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/9ffec0eb-e142-4703-b613-699253bc422d)

O teste de esfericidade de Bartlett utiliza-se de comparação entre a matriz, entre a 
matriz identidade e a matriz de correlação de mesma dimensão, para que a análise seja 
aplicável espera-se as matrizes sejam diferentes.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/bcb6487b-bb04-49f6-b2a8-e9db5f49c9ca)

Após os testes foi escolhido os k fatores, de forma mais didática, foi escolhido o 
número de fatores que participa do modelo. Através do critério de Kaiser ou critério da raiz 
latente, em que foi calculado os autovalores (indica o percentual da variância compartilhada 
pelas variáveis originais para formação de cada vetor), ele indica que foi considerado os 
fatores que obtiverem autovalores maior que 1.

E a análise de clusters, mas especificamente a Kmeans é uma técnica de divisão de 
grupos em que cada grupo é o mais homogêneo em suas características, aproximando os
jogadores com as estatísticas mais próximas em um grupo chamado de cluster e através do 
método de Elbow foi identificado o número de clusters.

Os dados utilizados foram retirados do Footstats, site que reúne estatísticas sobre o 
futebol, através de uma api desenvolvida no software python e foi consumida pelo mesmo 
software com o objetivo de realizar as análises estatísticas necessárias para alcançar o 
resultado da metodologia AHP-Gaussiano, uma análise multicritério, através de uma função 
criada pelo autor. 

Foi utilizado para a definição de pesos, medindo a importância dos fatores e subfatores 
que determinam a tomada de decisão no momento de escolher o melhor jogador para contrata 
em uma determinada posição de um time de futebol.

#### Resultados e Discussão

Para iniciar, os dados foram importados para o python e o dataframe contém as 
seguintes variáveis de estudo 'Equipe', 'Jogador', 'Jogos', 'Passe certo', 'Finalização certa', 
'Desarme certo', 'Cruzamento certo', 'Interceptação certa', 'Dribles', 'Virada de jogo certa', 
'Gols', 'Assistência gol', 'Assistência finalização', 'Defesa', 'Defesa difícil', 'Rebatida', 'Falta 
cometida', 'Falta recebida', 'Impedimentos', 'Pênaltis sofridos', 'Pênaltis cometidos', 'Perda 
da posse de bola', 'Cartão amarelo', 'Cartão vermelho'.

O primeiro passo para implementar o PCA, do objetivo proposto em materiais e 
métodos, foi a padronização dos dados através do StandardScaler que está dentro do pacote 
sklearn.preprocessing. 

Com ele os dados de cada variável serão padronizados com média e desvio padrão 
tendendo a 0 e 1 respectivamente. Esse passo foi escolhido porque eles têm proporções 
diferentes, apesar de todas as variáveis deterem o mesmo intervalo de 0 a +∞, existe uma 
proporção totalmente distinta a exemplo que não é esperado que um jogador faça mais que 
34 gols (recorde do Washington pelo Ahthletico-PR em 2004), entretanto o número de passes 
pode passar de 1000.

Feito isso, pode seguir o fluxo proposto e ir para o primeiro teste, KMO para verificar a 
proporção da variância. Lembrando que ele pode variar de 0 a 1 e que é esperado um valor 
maior que 0.8 para que possa ser considerado bom.

𝑘𝑚𝑜_𝑚𝑜𝑑𝑒𝑙 ∶ 0.8910774388918477

Visto que o resultado foi superior ao proposto, pode-se considerar um valor bom e seguir 
para o próximo teste. Utilizando o teste de esfericidade de Bartlett, para determinar se as 
matrizes, correlação e identidade, são iguais.

𝐻0: 𝑀𝑎𝑡𝑟𝑖𝑧 𝑑𝑒 𝐶𝑜𝑟𝑟𝑒𝑙𝑎çã𝑜 = 𝑀𝑎𝑡𝑟𝑖𝑧 𝐼𝑑𝑒𝑛𝑡𝑖𝑑𝑎𝑑e
𝐻1: 𝑀𝑎𝑡𝑟𝑖𝑧 𝑑𝑒 𝐶𝑜𝑟𝑟𝑒𝑙𝑎çã𝑜 ≠ 𝑀𝑎𝑡𝑟𝑖𝑧 𝐼𝑑𝑒𝑛𝑡𝑖𝑑𝑎𝑑𝑒

Realizando o cálculo com o auxílio do calculate_bartlett_sphericity do pacote 
factor_analyzer.factor_analyze, encontrou o valor abaixo.

𝐵𝑎𝑟𝑡𝑙𝑒𝑡𝑡 𝑠𝑡𝑎𝑡𝑖𝑠𝑡𝑖𝑐: 14917.011388460467
𝑝 − 𝑣𝑎𝑙𝑢𝑒 ∶ 0.0

Percebe-se que o valor da estatística de Bartlett é superior a área de aceitação e com 
um p-value tendendo a 0, não há evidências para aceitar H0, logo a matriz de correlação 
estatisticamente é diferente da matriz identidade.

O próximo passo é definir o número de k foi utilizado na análise de componentes 
principais. Utilizando o FactorAnalyzer do pacote FactorAnalyzer, foi feito o fit e testado na 
base de dados padronizada. Com isso encontrou o seguinte resultado.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/7fd202cd-8476-4316-8999-2b8313e82e3a)

Encontrando um total de 4 fatores, utilizando do método de Kaiser em que somente 
valores foi considerado fatores cujo autovalor seja superior a 1, deste modo somente 4 são 
maiores que 1(9.0711773, 3.12519854, 1.8768273, 1.38845768). Com ajuda do próximo 
quadro, observa-se o autovalor dessas variáveis, a variância e a variância acumulada.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/52069d69-440e-4fa9-9bbf-8bed239064dd)

Como é possível observar no quadro acima, a variância acumulada dos quatro fatores 
selecionados tem um total de 0,7028 ou 70,28%, isso é o mesmo que dizer que esses 
fatores representam mais que setenta porcento dos dados. Também podemos verificar 
esses dados no gráfico abaixo.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/703bbd1e-3ff7-4380-a57e-7fc33a92dfa6)

Neste momento pode ser verificado o quanto os fatores de forma individual impactam, 
cada variável através das cargas fatoriais, pois ela representa a correlação de Pearson entre 
os fatores e as variáveis originais. Ou seja, quanto maior a carga fatorial, mais importante 
aquele fator é para variável.

No próximo quadro é possível perceber que o fator 1, em 18 de 21 variáveis, ele detém 
a maior influência positiva dentre todos os fatores. E plausível visto que ele tem a maior 
variância dentre os quatros. Prestando atenção de forma mais atenta pode perceber que o 
fator 2 tem uma variância positiva mais alta em índices referente a defesa a exemplo da defesa 
e rebatida. O fator 3 ele vai influenciar positivamente quando tratar-se de goleiro, visto que os 
maiores fatores dele é defesa e defesa difícil, apesar que ele e o fator 4 quase não influenciam 
os dados.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/a957c771-88c2-42ae-9f69-99e6a393cc80)

Também é possível analisar as comunalidades, elas demostram como a variância total compartilhada, utilizando somente os 4 fatores escolhido pelo método de Kaiser, para cada variável em todos as variáveis. 
No quadro subsequente é possível perceber que 14 variáveis passam dos 70% de variância total compartilhada, mostrando que é um bom resultado diante dos dados expostos. Os três menores Cartão vermelho, Pênaltis sofridos e Pênaltis cometidos, são dados que tem pouca influência de decisão visto que são dados muito próximo entre os jogadores analisados aqui.

O cartão vermelho como exemplo dessas variáveis, teve no máximo 2 cartões atribuído a um mesmo jogador durante o brasileirão de 2022, 80% dos jogadores não receberam nenhum cartão vermelho, 82 receberam 1 ao longo das 38 rodadas e somente 10 receberam 2 cartões. Então essas variáveis mais na frente forçou uma tomada de decisão para perceber se é possível trabalhar com elas ou se ao menos elas influenciam ao ponto de permanecerem nos dados.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/b1379732-d80f-407f-a913-6fea55055e13)

Para finalizar a etapa da análise de componentes principais pode ser verificado a correlação de Pearson entre os fatores, lembrando que tais fatores são ortogonais entre si e espera-se que não haja correlação entre eles. Pode ser observado no quadro abaixo que eles não detêm correlação entre si e posteriormente pode ser observado um gráfico que enfatiza o valor absorvido pelos fatore e a comparação de como é afetada as variáveis diante dos dois maiores fatores.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/c2f6c3cd-2557-4c5e-a8e1-191d3b3789aa)

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/5a9334f2-182f-4b51-934e-9e2b63cb0479)

Para seguir a análise proposta inicialmente, nesse momento inicia-se a análise de cluster, mais precisamente a K-means ou K-médias. Ela é uma técnica de agrupamento para dividir os dados em diferentes grupos, mas que sejam o mais homogêneo possível dentro do grupo.

Ou seja, o objetivo da análise de agrupamentos é reunir dados pertencentes, sendo redundante, a um determinado grupo de acordo com uma medida de distância, logo os dados internos a um grupo terão as distancias mais próximas e quando comparado a outros grupos uma distância maior. Descrevendo assim associações e padrões entre variáveis.

No conjunto de dados estudado é dizer que procuraremos os jogadores com as características mais próximas para formar grupos. Deste modo tem-se uma análise estatística aprofundada das semelhanças dos jogadores contidos no banco de dados com as variáveis estudadas.

Neste estudo foi utilizada a distância euclidiana p-dimensional, como pode ser observada na fórmula abaixo, a metodologia aplicada corresponde a distância entre o ponto “a” e o ponto “b” em uma linha reta.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/e0a714f9-a20c-4f89-b43d-422a23dc7f8f)

É sabido que o número de fatores utilizados serão quatro, após o cálculo da PCA que é uma redução de dimensionalidade, passando de 22 variáveis para 4 com representação maior que 70% da variância que todas juntas teriam. Na análise de cluster foi utilizada a redução de dimensionalidade.

Entretanto, dessa vez foi utilizado o método de Elbow também conhecido como método cotovelo, é uma análise gráfica que tem como objetivo analisar a variância dos dados em relação a quantidade de clusters para o modelo. Ou seja, ele é utilizado para decidir o número ‘k’ de clusters.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/04ae12c0-67aa-4813-849c-771d3027e04d)

A análise gráfica consiste em perceber quando “a dobra do cotovelo” chega ao ponto que a diferença de ganho não seja relevante, em um mundo perfeito é imaginar que é quando faz-se um ângulo próximo a 90°. Olhando o gráfico outra pessoa pode escolher um ponto diferente, mas nesse momento foi escolhido o número 13 de clusters.

O próximo passo é analisar se a variabilidade dentro do grupo é menor que a variabilidade entre os grupos, para isso é utilizado o teste F para análise de variância.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/45a7e89e-df1c-4afb-bfe0-85347cc631b7)

Isso para k-1 em graus de liberdade, visto que existem 13 clusters, graus de liberdades é igual a 12 para o numerador, enquanto para o denominador é n-k, sendo n o número de observações. Logo, 746 – 13, tem-se 733 de graus de liberdade para o denominador.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/9c078dd9-462d-4c9e-993b-c064e58511d9)

Analisando as 4 variáveis através do teste F, como observado na tabela 6, verifica-se como já imaginado que o fator 1 é o que tem um teste F maior e isso indica que ele é o que mais colabora na formação dos grupos. Também é possível observar que todos detém um p-valor muito menor do que o proposto de 0,05.

Além disso observa-se que a variabilidade dentro dos grupos é muito menor que a entre grupos, demonstrando variáveis dentro dos grupos de forma homogênea e fora do grupo heterogênea, assim como é esperado.

Para melhorar a visualização dos grupos formados dentro do banco de dados estudados foi plotado um gráfico, como o visto abaixo, nele estão contidas as 3 maiores variáveis no que concerne a ganho de variância, deste modo podendo observar como se comportam as variáveis e seus respectivos grupos.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/36140675-7c97-4de9-9dd2-b18d86ffd8ec)

Antes de partir para a parte final do processo, em que visa a tomada de decisão, pode-se pegar um exemplo para entender tudo que aconteceu até aqui. O campeão brasileiro de 2022 foi a Sociedade Esportiva Palmeiras, sendo o clube um bom exemplo para este experimento. Dentro da equipe tiveram vários destaques, eles dominaram a seleção do campeonato e inclusive a revelação do campeonato foi do clube.

Para esse experimento inicial foi selecionado um dos grandes destaques do time na temporada de 2022, Eduardo Pereira Rodrigues ou simplesmente Dudu como é conhecido. 

Ele foi escolhido pelos números que ele teve no ano de estudo, atuou em todos 38 compromissos do seu time durante aquela temporada, quase 800 passes certos, 37 dribles certos e 30 finalizações no alvo, esses são alguns dos números dele nesse campeonato.

Rodando o modelo construído até aqui para encontrar os 10 jogadores mais próximos aos seus números obtidos durante o campeonato, foi possível chegar nos seguintes nomes que podem ser vistos na tabela 7.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/b3796b9e-5f29-44e0-9272-87d760ebcad5)

Feito toda a parte de machine learning não supervisionado proposto, parte-se para o AHP Gaussiano e começa-se a trabalhar com método de decisão multicritério dentro da pesquisa operacional.
E sabido os 10 jogadores mais próximos para o exemplo colocado até aqui, mudando o objetivo a partir desse, até então era procurar os jogadores mais parecido com o perfil desejado e nesse momento a pergunta passa a ser, supondo que se quer contratar alguém com o perfil imputado, “Qual o melhor jogador para contratar?”. 

Em suma é decidir qual a melhor decisão a ser tomada diante das 10 que foram expostas através do método de análise de clusters (Kmeans) e PCA. Visto que nesse momento começa-se a ser construído o modelo de decisão. Para iniciar a metodologia é preciso separar os valores considerados positivos quanto maior ele seja e os valores negativos.

Como valores positivos foram considerados os: 'Jogos', 'Passe certo', 'Finalização certa', 'Desarme certo', 'Cruzamento certo', 'Interceptação certa', 'Dribles', 'Virada de jogo certa', 'Gols', 'Assistência gol', 'Assistência finalização', 'Defesa', 'Rebatida', 'Falta recebida'. Para cada variável considerada positiva é realizado o seguinte cálculo.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/9033fd6f-0374-408f-b0af-9ed9ff423be9)

De forma mais simples, o que está sendo feito na última fórmula é a proporção de importância do jogador “l”(linha) dentro da variável “c”(coluna). Exemplo do número de jogos do Dudu, 38 jogos divididos pela soma da coluna de jogos e assim conseguirá o resultado de representatividade do jogador dentro da variável jogos.

Para os valores negativos foram considerados: 'Falta cometida', 'Perda da posse de bola', 'Cartão amarelo'. Cartões vermelhos, após análise, não entrou nos quesitos para definir uma escolha, já que a maioria dos jogadores estavam zerados nesse quesito. O cálculo referente aos valores considerados negativos pode ser observado abaixo.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/45d0b572-1dbe-4c23-868c-1694c80c1e94)

Para um melhor entendimento pode-se observar o passo-a-passo a seguir, no primeiro momento utilizando o número de jogos que é um fato positivo e comparando antes de utilizar processo de normalização do método AHP Gaussiano e depois, na tabela 8.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/953148e0-53ee-4186-b4be-63d0c5cfffdc)

Como pode ser visto acima, normalização do método aplicado quando somado é igual a 1 porque se observar com mais detalhe a fórmula, trazendo para o estudo, ela calcula o quanto o número de jogos daquele jogador representa diante de todos. Ou seja, é a quantidade jogos do jogador x dividido pela soma de todos os jogos. 

Quando se parte para os valores considerados negativos, a estratégia é diferente e por esse motivo o cálculo tem duas etapas. A primeira consiste em inverter a tendencia, visto que da forma que é calculado os valores positivos quanto maior significa melhor, então par cálculo dos valores negativos divide o 1 pela quantidade de observações dentro da variável de cada jogador. 

No momento que foi apelidado de “depois” e dividir, o que tem maior valor negativo obterá um menor percentual, visto que quanto maior o denominador na divisão pelo número 1 como numerador, menor foi o valor para encontrar o percentual de importância para a variável em questão. Para ficar mais claro pode ser observado na tabela a seguir.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/6f023563-af06-4b2b-8212-3a1b110b6bbc)

Talvez ainda não tenha ficado tão claro o cálculo, mas pode se pegar o número 9 de exemplo, fazendo 1/53 resultará no menor valor e quando utilizar o segundo passo que corresponde ao mesmo aplicado as variáveis positivas ele apresentará a menor significância do grupo de jogadores. 

Seguindo o script da metodologia do AHP-Gaussiano, nesse momento encontra-se os pesos de cada variável. Para isso calcula-se a média e o desvio padrão de cada variável e divide o desvio pela média.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/69568271-0388-4d2c-bc71-793bbf4900e3)

Como pode ser observado na próxima tabela, os fatores gaussianos das variáveis ficaram muito próximos entre si, mostrando que uma variável não tem um peso maior que a outra. Ou seja, não foi necessariamente porque o jogador “A” fez mais gols que ele foi considerado uma melhor opção.

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/cff21b95-a024-48d1-86aa-8e7413ba08ab)

Este é o momento que objetivou todo o trabalho feito até aqui, determinar qual a melhor opção a ser tomada diante dos jogadores mais próximos ao perfil de desejo. Até o momento foi construída toda a base para que agora possa ser verificado o que a metodologia proposta até aqui pode oferecer de fato para o mercado e na tabela 11 pode ser visto o resultado. 

![image](https://github.com/BrunoMeloSlv/Desvende-os-Segredos-do-Futebol-com-Intelig-ncia-Artificial-/assets/91537585/f74b1fda-2624-4ee3-9514-8afbd354e8a9)

Logo, pode-se afirmar que com a aplicação da metodologia e a função criada em python nesse estudo, o jogador Carlos de Pena do Internacional é o mais próximo das características do Dudu do Palmeiras, utilizando os dados do Brasileirão de 2022, ou seja, dentre os 10 escolhidos a melhor opção é o jogador do Internacional.

#### Considerações Finais

O estudo se utilizou de vários métodos estatísticos, desde padronização, passando pela diminuição dos componentes com a PCA, análise de cluster e finalizando com a AHP-Gaussiano. E factível que existam variações de opiniões por metodologia ou até mesmo dados utilizados, mas diante do proposto mostrou-se um método eficaz e confiável durante a confecção do modelo, ele foi testado com alguns métodos estatístico para verificar a confiabilidade.

A PCA por exemplo determinou que 70,28% podem ser explicados por 4 componentes, diminuindo em 5 vezes o número de variáveis a princípio escolhidas. Nesse momento deve surgir questionamento quanto as variáveis, poderiam ser usados ‘n’ outras opções. Porém é ressaltado a ideia de ceteris-paribus.

O estudo poderia ser dividido por posição a exemplo e isso determinaria uma outra visão e possibilidades dentro do estudo. Visto que as características exigidas para um zagueiro são diferentes das de um atacante, ou seja, não pode ser exigido o mesmo número de finalizações por exemplo.

Esse estudo soa como o início de uma ideia, ele pode ter várias vertentes e não somente no esporte. Imaginando que a vida é baseada em decisões e desde uma decisão de compra de um detergente a escolha de um perfil de jogador podem passar pelos mesmos métodos aplicados aqui. 

Logo é possível imaginar que este estudo pode ser transformado em um algoritmo que solicita ao usuário o dataframe e que todo passo-a-passo seja calculado de forma automática e apresente somente o resultado das melhores escolhas estatisticamente para o usuário final, diante dos dados expostos. 

#### Agradecimentos
 
	Dedico esse TCC ao meu amigo Luiz Leonardo e minha parceira de vida Bianca Melo. 

#### Referências

	Almeida, M., Coelho, R., Oliveira, D., Camargo, A., & Savioli, P. (2020). Sales-based Brand Equity as a Performance Driver in ‘The Country of Soccer’. Revista de Administração Contemporânea, pp. v. 24, n. 2, art. 2, pp. 134-150.
Barreto, M., Mendonça, M., Farias, G., & Oliveira, R. (Dezembro de 2022). Compreensão Estatística de Professores em Formação Inicial. Bolema, pp. v. 36, n. 74, p. 1115-1134.
Barroso, D. J. (2021). MÉTODO AHP (ANALYTIC HIERARCHY PROCESS - GAUSSIANO) NA DETERMINAÇÃO DE AQUISIÇÃO DE UM APARELHO CELULAR. Revista Eletrônica Ciência & Tecnologia Futura, pp. v2 n1 pg 1-12.
Ribeiro, R. R. (set/dez de 2022). A geopolítica do pós-Segunda Guerra vista a partir do futebol. Varia Historia, Belo Horizonte, pp. vol. 38, n. 78, p. 1007-1012.
Santos, C., & Santos, V. (Abril/Junho de 2022). Competência em Informação (CoInfo) como fator social de compreensão e inclusão ao mundo do trabalho sob as perspectivas de Guy Le Boterf e Christine Bruce: notas introdutórias,reflexões necessárias. Perspectivas em Ciência da Informação, pp. v.27, n. 2, p. 268-296.
Wu, J. (Novembro/Dezembro de 2022). INTERLEAVED TACTICAL TRAINING OF BIG FOOTBALL TEAMS. Revista Brasileira de Medicina do Esporte, pp. Vol. 28, No 6.
