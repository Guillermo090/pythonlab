"""
Pandas trabaja dos objetos principales
1.- Pandas Series muy parecido a un arreglo de numpy 
2.- Pandas Dataframe es un objeto hecho de arrays. Filas y Columnas tienen indices en las columnas se pueden asignar

Se puede hacer : Slicing, Operaciones aritmeticas, Distintos tipos de datos, Tamaño variable
"""

import pandas as pd

psg_players =   pd.Series(["Navas","Mbappe","Neymar","Messi"],
                  index=[1,7,10,30]
                )

print(psg_players)

dict_psg = {1:"Navas",7:"Mbappe",10:"Neymar",30:"Messi"}
print( pd.Series(dict_psg))

dict_psg_df = {
    "Jugador" : ["Navas","Mbappe","Neymar","Messi"],
    "Altura" : [183.0, 170.0, 170.0, 165.0],
    "Goles" : [2, 200, 200, 200]
}

psg_dataframe = pd.DataFrame(dict_psg_df, index=[1, 7, 10, 30])
print(psg_dataframe)
print(psg_dataframe.columns)
print(psg_dataframe.index)