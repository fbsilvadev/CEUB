import pandas as pd
import numpy as np

# Amostras
num_amostras = 1000

# Gerar dados 
idades = np.random.randint(18, 70, size=num_amostras)
rendas_mensais = np.random.uniform(1000, 10000, size=num_amostras)
historicos_credito = np.random.choice([0, 1], size=num_amostras)
historicos_emprego = np.random.choice([0, 1], size=num_amostras)
aprovados = np.random.choice([0, 1], size=num_amostras)

# Criar DataFrame
dados = pd.DataFrame({
    'Idade': idades,
    'Renda Mensal': rendas_mensais,
    'Historico de Credito': historicos_credito,
    'Historico de Emprego': historicos_emprego,
    'Aprovado': aprovados
})

# Salvar os dados em um arquivo CSV
dados.to_csv('dados_de_treinamento_num.csv', index=False)
