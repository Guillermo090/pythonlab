import pandas as pd
import numpy as np



df_clientes = pd.read_excel('pandas/respaldos_clientes.xlsx')

# print(df_clientes.head(2))

# all_ruts =  df_clientes.groupby("RUT CLIENTE").count()


print(df_clientes.head(2))
for idx, row in df_clientes.iterrows():
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print(row[5])
    print(row[6])
    print(row[7])
    print(row[8])
    print(row[9])
