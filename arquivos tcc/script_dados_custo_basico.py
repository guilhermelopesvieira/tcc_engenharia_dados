import pandas as pd
import numpy as np
import sqlite3


conn = sqlite3.connect('seu_banco_de_dados.db')


query = "SELECT cd_prod, ds_prod, desc, vlr, dt_base FROM dados_custo_basico"
df = pd.read_sql_query(query, conn)


print(df)


conn.close()
