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


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# dados do cliente
def coletar_dados_cliente():
    print("Por favor, forneca as seguintes informacoes:")
    idade = int(input("Idade: "))
    renda_mensal = float(input("Renda Mensal (em R$): "))
    historico_credito = int(input("Historico de Credito (0 - Ruim. 1 - Bom): ")) 
    historico_emprego = int(input("Historico de Emprego (0 - Ruim. 1 - Bom): "))
    
    return idade, renda_mensal, historico_credito, historico_emprego

# Carregar os dados de treinamento
data = pd.read_csv('dados_de_treinamento_num.csv')

# Separar os dados em features (caracteristicas) e target (alvo)
X = data.drop('Aprovado', axis=1) # Features
y = data['Aprovado'] # Target

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo de arvore de decisao
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Funcao para prever se o emprestimo sera aprovado ou nao para um cliente especifico
def aprovar_emprestimo(idade, renda_mensal, historico_credito, historico_emprego):
    # Converter historico de credito e emprego em variaveis
    #historico_credito_bin = 1 if historico_credito == 'bom' else 0
    #historico_emprego_bin = 1 if historico_emprego == 'estavel' else 0
    # Preparar os dados do cliente para previsao
    dados_cliente = [[idade, renda_mensal, historico_credito, historico_emprego]]
    # Fazer a previsao
    previsao = model.predict(dados_cliente)
    if previsao[0] == 1:
        return "Emprestimo Aprovado"
    else:
        return "Emprestimo Negado"

# Coletar os dados do cliente
idade, renda_mensal, historico_credito, historico_emprego = coletar_dados_cliente()

# Fazer a
resultado = aprovar_emprestimo(idade, renda_mensal, historico_credito, historico_emprego)
print("Resultado da analise de credito:", resultado)
