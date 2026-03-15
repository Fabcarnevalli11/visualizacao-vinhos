# visualizacao-vinhos
# Visualização de Dados - Wine Quality

## Descrição do Projeto
Este projeto tem como objetivo explorar e visualizar o dataset **Wine Quality**, que contém informações físico-químicas de vinhos tintos e suas respectivas avaliações de qualidade.

A análise foi realizada utilizando Python no Google Colab, com foco em análise exploratória de dados e identificação de padrões entre as variáveis do conjunto de dados.

## Dataset

O dataset utilizado foi o **Wine Quality Dataset**, disponível no UCI Machine Learning Repository.

Ele contém variáveis químicas do vinho, como:

- fixed acidity
- volatile acidity
- citric acid
- residual sugar
- chlorides
- sulphates
- alcohol

A variável **quality** representa a qualidade do vinho avaliada por especialistas.

## Análise Exploratória

Durante a análise exploratória foram realizados:

- verificação da estrutura do dataset
- análise da distribuição da variável qualidade
- análise da relação entre teor alcoólico e qualidade
- análise da correlação entre variáveis

## Visualizações

O projeto inclui visualizações como:

- gráfico de distribuição da qualidade dos vinhos
- gráfico de dispersão entre teor alcoólico e qualidade
- matriz de correlação entre variáveis

Para explorar os dados de forma eficiente, foram utilizados diferentes tipos de gráficos, cada um escolhido de acordo com o tipo de informação que se desejava analisar.

### Histograma – Distribuição da qualidade dos vinhos

O histograma foi utilizado para analisar a distribuição da variável "quality". Esse tipo de gráfico é adequado para visualizar a frequência de valores em uma variável numérica, permitindo identificar concentrações, padrões e possíveis assimetrias nos dados.

### Gráfico de Dispersão – Relação entre teor alcoólico e qualidade

O gráfico de dispersão foi utilizado para analisar a relação entre duas variáveis numéricas: teor alcoólico e qualidade do vinho. Esse tipo de visualização permite identificar possíveis correlações ou tendências entre variáveis, mostrando como uma variável pode influenciar ou se relacionar com outra.

### Mapa de Calor de Correlação – Relação entre variáveis

A matriz de correlação foi representada por meio de um mapa de calor (heatmap), que permite visualizar rapidamente o grau de correlação entre todas as variáveis do dataset. Esse tipo de gráfico facilita a identificação de relações positivas ou negativas entre variáveis, auxiliando na compreensão da estrutura dos dados.

## Tecnologias Utilizadas

- Python
- Pandas
- Plotly
- Streamlit (para construção do dashboard)

- ## Conclusão

A análise exploratória do dataset Wine Quality permitiu identificar padrões importantes entre as variáveis físico-químicas dos vinhos e sua avaliação de qualidade.

Observou-se que a maioria dos vinhos apresenta qualidade entre 5 e 6, indicando uma concentração na faixa intermediária de avaliação. Além disso, a análise da relação entre teor alcoólico e qualidade sugere uma tendência de que vinhos com maior teor alcoólico tendem a receber avaliações mais altas.

A matriz de correlação também permitiu identificar relações entre diferentes variáveis do dataset, contribuindo para uma melhor compreensão dos fatores que podem influenciar a qualidade do vinho.

- ## Como executar o projeto

1. Instalar as bibliotecas necessárias:

pip install streamlit pandas plotly

2. Executar o dashboard:

streamlit run app.py

## Autor

Fabrício Ferreira Carnevalli  
Disciplina: Visualização de Dados  
UniFil - Centro Universitário Filadélfia
