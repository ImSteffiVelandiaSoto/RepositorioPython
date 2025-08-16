import pandas as pd 

#se lee el archivo de manera Local
df_local=pd.read_csv("temporal.csv")

#impresion de las 15 primeras filas.
print(df_local.head(2))


#impresión del DF
print(df_local)
