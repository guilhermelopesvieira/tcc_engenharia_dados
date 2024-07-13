import pandas as pd
import numpy as np


base_dados_custo_insumo_1 = pd.read_csv('C:\\Users\\TCC\\base_dados_custo_insumo_1.csv')
base_dados_custo_insumo_2 = pd.read_csv('C:\\Users\\TCC\\base_dados_custo_insumo_2.csv')
base_dados_custo_insumo_3 = pd.read_csv('C:\\Users\\TCC\\base_dados_custo_insumo_3.csv')


todas_tabelas = pd.concat([base_dados_custo_insumo_1, base_dados_custo_insumo_2, base_dados_custo_insumo_3])


resultado_filtrado = todas_tabelas[todas_tabelas['localidade'] == 330]


print(resultado_filtrado.head())
