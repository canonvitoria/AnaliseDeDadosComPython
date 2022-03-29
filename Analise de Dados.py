#Importar a base de dados
import pandas as pd

tabela = pd.read_csv(r"D:\telecom_users.csv")

#Visualizar a base de Dados
tabela = tabela.drop("Unnamed: 0", axis=1)
print(tabela)

#Tratamento de Dados
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")
tabela = tabela.dropna(how="all", axis=1)
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

#Analise Inicial / Analise Global
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

#Analise detalhada (buscar a causa/a solução dos cancelamentos)
import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="Churn")
    grafico.show()


