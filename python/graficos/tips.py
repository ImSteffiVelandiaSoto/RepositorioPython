import seaborn as sns
import matplotlib.pyplot as plt

df_tips = sns.load_dataset("tips")
#Diagrama de cajas
plt.figure(figsize=(8,6))
sns.boxplot(x="day", y="total_bill", data=df_tips)
plt.xlabel("Day of Week")
plt.ylabel("Total Bill ($)")
plt.title("distribucion de propinas por dia de la semana")
plt.show()