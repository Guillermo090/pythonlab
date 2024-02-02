import pandas as pd


# data = pd.read_csv("pandas/bestsellers-with-categories.csv",sep=',',header=0,names=['Nombres', 'Autor', 'Ranking de Usuario', 'Reviews', 'Precio', 'Año', 'Genero'] )
# print(data)

# print(data.columns)


data_json = pd.read_json('pandas/hp_characters_data_raw.json',typ='Series')
print(data_json)