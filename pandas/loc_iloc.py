import pandas as pd

df_books = pd.read_csv('pandas/bestsellers-with-categories.csv',sep=',',header=0)
# print(df_books[0:4])
print(df_books[['Name','Author']])

# Loc 

print(df_books.loc[0:4,['Name','Author']])

# validator en loc
print( df_books.loc[:, ['Author']] == 'JJ Smith' )


# iloc

print( df_books.iloc[:, 0:4] )

# al indice 1 de la columna 4 lo multiplica por -1
print( df_books.iloc[1,3] * -1 )

# rango de datos
print( df_books.iloc[:2,2:] )


