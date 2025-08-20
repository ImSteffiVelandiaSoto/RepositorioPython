import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
df_iris = sns.load_dataset("iris")

# Gráfico scatter: longitud vs ancho del sépalo, coloreado por especie
plt.figure(figsize=(8,6))
for especie, grupo in df_iris.groupby("species"):
    plt.scatter(grupo["sepal_length"], grupo["sepal_width"], label=especie)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Iris: Sepal Length vs Width")
plt.legend()
plt.grid(True)
plt.show()
