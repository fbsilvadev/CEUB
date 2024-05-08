from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

# dados do cliente
def coletar_dados_cliente():
    print("Por favor, forneca as seguintes informacoes:")
    idade = int(input("Idade: "))
    renda_mensal = float(input("Renda Mensal (em R$): "))
    historico_credito = input("Historico de Credito (Bom/Ruim): ").lower()
    historico_emprego = input("Historico de Emprego (Estavel/Instavel): ").lower()
    
    return idade, renda_mensal, historico_credito, historico_emprego

# Carregar os dados de treinamento
data = pd.read_csv('dados_de_treinamento.csv')

# Separar os dados em features (caracter�sticas) e target (alvo)
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
    historico_credito_bin = 1 if historico_credito == 'bom' else 0
    historico_emprego_bin = 1 if historico_emprego == 'estavel' else 0
    # Preparar os dados do cliente para previsao
    dados_cliente = [[idade, renda_mensal, historico_credito_bin, historico_emprego_bin]]
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
