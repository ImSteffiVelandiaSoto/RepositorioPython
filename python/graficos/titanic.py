import seaborn as sns
import matplotlib.pyplot as plt

# Cargar dataset titanic
titanic = sns.load_dataset("titanic")

plt.figure(figsize=(8,6))
sns.barplot(x="pclass", y="survived", hue="sex", data=titanic)
plt.xlabel("Clase del pasajero")
plt.ylabel("Proporción de sobrevivientes")
plt.title("Supervivencia en el Titanic por clase y sexo")
plt.show()
