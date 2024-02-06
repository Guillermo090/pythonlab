import pandas as pd
import numpy as np

df_books = pd.read_csv('pandas/bestsellers-with-categories.csv',sep=',',header=0)

# print(  df_books.head(3) )



# drop columns
df_books.drop('Genre',axis=1,inplace=True)
df_books.drop('Year',axis=1,inplace=True)

# print(  df_books.head(3) )


# drop rows
df_books_two = pd.read_csv('pandas/bestsellers-with-categories.csv',sep=',',header=0)
print( df_books_two.drop([0,1,2],axis=0).head(3) )
print( df_books_two.drop(range(0,10),axis=0).head(3) )


# add columns
df_books_two['Nueva_Columna'] = np.nan
print(df_books_two)

print(df_books_two.head(2))
print(df_books_two.shape[0])

data = np.arange(0,df_books.shape[0])
df_books_two['Rango'] = data
print(df_books_two)

# add rows
df_books_three = pd.read_csv('pandas/bestsellers-with-categories.csv',sep=',',header=0)
df_books_three.shape[0]
print(df_books_three.head(3))
print(df_books_three.shape[0])
df_books_three = pd.concat([df_books_three,df_books_three])
print(df_books_three.head(3))
print(df_books_three.shape)
