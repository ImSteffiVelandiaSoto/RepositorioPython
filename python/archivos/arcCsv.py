import pandas as pd
#exporta un CSV
# Crear un DataFrame de ejemplo
data = {'Nombre': ['Ana', 'Luis', 'Sofía'],
        'Edad': [25, 30, 22],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}
df = pd.DataFrame(data)

# Exportar el DataFrame a un archivo CSV
df.to_csv('datos_personas.csv', index=False)

print("El DataFrame se ha exportado a 'datos_personas.csv'.")