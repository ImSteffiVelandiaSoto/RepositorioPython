import seaborn as sns
import matplotlib.pyplot as plt

df_tips = sns.load_dataset("tips")
#Diagrama de cajas

plt.figure(figsize=(8,6))

sns.boxplot(x="day", y="total_bill", data=df_tips)
plt.xlabel("Dia de la semana")
plt.ylabel("Total de la cuenta")
plt.title("distribucion de propinas por dia de la semana")
plt.show()