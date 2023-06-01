# código de geração do gráfico 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

filename = "gasolina.csv"
df_gasolina = pd.read_csv(filename)

with sn.axes_style('whitegrid'):

  grafico = sn.lineplot(data=df_gasolina, x="venda", y="dia", palette="pastel")
  grafico.set(title='Evolução do preço da gasolina por dia', xlabel='Preço', ylabel='Dia');

plt.savefig('gasolina.png')