import pandas as pd
import numpy as np

df_books = pd.read_csv('pandas/bestsellers-with-categories.csv',sep=',',header=0)

print(df_books.head(2))

mayor_a_2016 =  df_books["Year"] > 2016

# hacen lo mismo
print( df_books[mayor_a_2016] )
print( df_books[df_books["Year"] > 2016] )

only_fiction =  df_books["Genre"] == 'Fiction'

print(df_books[only_fiction])
print(df_books[df_books["Genre"] == 'Fiction'])


print(df_books[only_fiction & ~mayor_a_2016])
