# pip install pandas openpyxl plotly nbformat

import pandas as pd

# dados = pd.read_excel("fakerdata.xlsx")
dados = pd.read_excel("vendas.xlsx")

# imprime as 5 primeiras linhas do arquivo
# print(dados.head()) 

# imprime as 10 linhas do arquivo
# print(dados.head(10)) 

# imprime as últimas 5 linhas do arquivo
# print(dados.tail()) 

# imprime aquantidade de linhas e colunas da planilha 
# print(dados.shape)

# imprime o tipo de cada coluna
# print(dados.info())

# imprime coluna
# print(dados.cidade)
# print(dados.estado)
# print(dados.local_consumo)

# Usado para quando o nome tiver algum caracter especial
# print(dados["cidade"])
# print(dados[["cidade", "estado"]])

# Estatística
# print(dados.describe())
# print(dados["preco"].describe())

# contagem de vendas por loja ou cidade
# print(dados["loja"].value_counts())
# print(dados["cidade"].value_counts())
# print(dados["forma_pagamento"].value_counts())

# Agrupando valores - Faturamento por loja
# print(dados.groupby("loja")["preco"].sum().to_frame())
# print(dados.groupby("forma_pagamento")["preco"].sum())


# print(dados.groupby(["estado", "cidade", "loja", "forma_pagamento"])["preco"].sum())

# exportando para o EXCEL
# dados_agrupados = dados.groupby(["estado", "cidade", "loja", "forma_pagamento"])["preco"].sum()

# dados_agrupados.to_excel("dados-consolidados.xlsx")

