import pandas as pd
from datetime import datetime

## Abre uma planilha onde lê os dados dos clientes contidos na primeira página da mesma.
df_clients = pd.read_excel('dados/client_data_test.xlsx', sheet_name='Página1')

## Renomeando as colunas para um formato padronizado: titulos das colunas em 
#  minusculo e sem espaços.
columns_renamed=[]
for column in df_clients:
    column_title=column.lower()
    column_title=column_title.replace(' ','_')
    columns_renamed.append(column_title)
df_clients.columns = columns_renamed

## Agora será pego somente a coluna 'data_de_nascimento' para fazer o tratamento
#  da idade a seguir.
date_birth = df_clients['Data_Nascimento']

## O código a seguir irá fazer o calculo baseado na data atual para determinar a
#  idade de cada cliente e armazenar na coluna 'idade'.
today = datetime.today()
df_clients['idade'] = (today - df_clients['data_de_nascimento']).dt.days//365

## Pra finalizar, salvando a tabela atualizada em um novo arquivo e mantendo o 
#  mesmo formato (xlsx).
df_clients.to_excel('dados/client_data_att.xlsx')

