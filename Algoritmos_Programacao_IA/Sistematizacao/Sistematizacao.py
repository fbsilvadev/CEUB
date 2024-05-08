#
##SISTEMATIZACAO
#
##Algoritmos e Programacao para Inteligencia Artificial
#
##Aluno: Fernando Batista da Silva
##Matricula: 82400212
#
##Professor: Dr. Leonardo Reboucas de Carvalho
#
##Data: 08/05/2024
#
##Descricao: Este programa tem como objetivo realizar a construcao de um sistema de analise de credito. 
# O sistema deve concluir se aprova um eventual emprestimo ou nao. 
# Para isso, o sistema deve solicitar ao usuario as seguintes informacoes: 
#   idade, 
#   renda mensal, 
#   valor do emprestimo 
#   quantidade de parcelas. 
# O sistema deve entao calcular o valor da parcela (valor do emprestimo dividido pela quantidade de parcelas) e verificar se a parcela somado a outra dividas e menor ou igual a 30% da renda mensal. 
# Se for, o emprestimo e aprovado. Caso contrario, o emprestimo e negado. 
# O sistema deve exibir uma mensagem indicando se o emprestimo foi aprovado ou negado.
# O sistema deve ser implementado em Python e deve ser organizado em funcoes, implementando a arvore de decisso em anexo.


import pandas as pd #To work with dataset
import numpy as np #Math library
from sklearn import tree, metrics
import seaborn as sns #Graph library that use matplot in background
import matplotlib.pyplot as plt #to plot some parameters in seaborn

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# referencia https://github.com/Erikfernandoms/ArvoreDecisao/tree/main/FEI-CC7711-ArvoreDecisao-main
# referencia https://github.com/tiagob85/ArvoreDecisaoPython

#
# DATASET: https://www.kaggle.com/datasets/laotse/credit-risk-dataset
#

# Carregando o conjunto de dados
dados = pd.read_csv('dados_credito.csv')

# Pré-processamento de dados
# ... (tratamento de dados ausentes, outliers, etc.)

# Separação em conjuntos de treinamento e teste
X = dados[['renda', 'score_credito', 'historico_pagamentos']]
y = dados['aprovado']

# Treinamento da árvore de decisão
modelo = DecisionTreeClassifier()
modelo.fit(X, y)

# Função para análise de crédito individual
def analisar_credito(renda, score_credito, historico_pagamentos):
  novo_cliente = pd.DataFrame([[renda, score_credito, historico_pagamentos]], columns=X.columns)
  predicao = modelo.predict(novo_cliente)

  if predicao[0] == 1:
    # Cliente aprovado
    taxa_juros = 0.1  # Taxa de juros estimada
    valor_maximo = 10000  # Valor máximo do empréstimo estimado
    resultado = "Crédito aprovado!"
  else:
    # Cliente reprovado
    taxa_juros = 0
    valor_maximo = 0
    resultado = "Crédito não aprovado."

  return resultado, taxa_juros, valor_maximo

# Exemplo de uso
renda_cliente = 5000
score_cliente = 700
historico_cliente = "Bom"

resultado, taxa_juros, valor_maximo = analisar_credito(renda_cliente, score_cliente, historico_cliente)

print(resultado)
print(f"Taxa de juros: {taxa_juros:.2f}%")
print(f"Valor máximo do empréstimo: R$ {valor_maximo:.2f}")
