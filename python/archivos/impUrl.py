import pandas as pd
#crear variable con la URL
url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

#definir el nombre de las columnas
col_names=["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

df_iris = pd.read_csv(url, names=col_names)

print(df_iris.head(8))

print(df_iris)



