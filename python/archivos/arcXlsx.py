import pandas as pd
import openpyxl
#import XLS

# Asegúrate de tener openpyxl instalado:
# pip install openpyxl

# Crear un DataFrame de ejemplo
data = {'Producto': ['Laptop', 'Mouse', 'Teclado'],
        'Precio': [1200, 25, 75],
        'Stock': [15, 50, 30]}
df = pd.DataFrame(data)

# Exportar el DataFrame a un archivo de Excel
df.to_excel('inventario_productos.xlsx', index=False, sheet_name='Productos')

print("El DataFrame se ha exportado a 'inventario_productos.xlsx'.")