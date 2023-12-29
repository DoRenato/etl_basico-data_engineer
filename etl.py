import pandas as pd
from datetime import datetime

# abre uma planilha onde lê os dados dos clientes na primeira página.
data_clients = pd.read_excel('client_data_test.xlsx', sheet_name='Página1')

# renomeia a coluna para um formato mais comum
data_clients.rename(columns={'Data de Nascimento': 'Data_Nascimento'}, inplace=True)

# pega somente uma coluna específica
date_birth = data_clients['Data_Nascimento']

# irá fazer o calculo baseado na data atual para determinar a idade de cada cliente e armazenar
# na coluna 'Idade'.
today = datetime.today()
data_clients['Idade'] = (today - data_clients['Data_Nascimento']).dt.days//365