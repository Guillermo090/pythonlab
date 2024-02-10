
import pandas as pd
import numpy as np

dict = {
    "Col1":[1,2,3,np.nan],
    "Col2":[4,np.nan,6,7],
    "Col3":["a","b","c",None],
}

df = pd.DataFrame(dict)
print(df)

# revisar nulos
print(df.isnull())

# pasa valores nulos a visualizacion binaria    
print(df.isnull() * 1 )

# llena nulos con valor especifico
print(df.fillna("Missing"))

# llena nulos con media
# print(df.fillna(df.mean()))


# llena nulos con media
print(df.interpolate())

# otra forma de manejar nulos
print(df.dropna())