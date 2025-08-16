import pandas as pd 
# 1 crear el diccionario
datos={
    "Nombres":["Ana", "Jaime", "Luis", "Camilo"],
    "Edades":[23 , 23, 35, 85, 52],
    "Ciudad":["Medellin", "Bogotá", "Cali", "Medellin"],
    "Salario":[2500000,3000000, 4500000, 1500000]
}

#2 convertirlo a un Dataframe
dFrame= pd.DataFrame(datos)
dFrame= pd.DataFrame(datos)

#3 imprmir datos
print("Dataframe")
print(dFrame)

#4 filtrar empleados con sueldo> 3000000
print("Empleados con salario superior a $3.000.000")
print(dFrame["Salario"]>3000000)

#5 promedio de sueldos
print("Promedio total de sueldos")
promedioSueldo= dFrame["Salario"].mean()
print(f"promedio: {promedioSueldo}")

#6 promedio de sueldos por cidad
print("Promedio total de sueldos agrupado por ciudad")
print(dFrame.groupby("Ciudad")["Salario"].mean())

#7 ordenar por edad
print("Datos ordenados por edad")
print(dFrame.sort_values(by="Nombres"))