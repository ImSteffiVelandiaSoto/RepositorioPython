import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el dataset
df_iris = sns.load_dataset("iris")

# Gráfico scatter: longitud vs ancho del sépalo, coloreado por especie
plt.figure(figsize=(8,6))
for especie, grupo in df_iris.groupby("species"):
    plt.scatter(grupo["petal_length"], grupo["petal_width"], label=especie)
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Iris: Petal Length vs Width")
plt.legend()
plt.grid(True)
plt.show()
