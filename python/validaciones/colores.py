print("Este programa mezcla colores")
color1 = int(input("Seleccione 1 para rojo, 2 para azul y 3 para verde"))
color2 = int(input("Seleccione 1 para rojo, 2 para azul y 3 para verde"))
if color1 == 1:
    if color2 == 1:
        print("El color resultante es Rojo")
    elif color2 ==2:
        print("El color resultante es Morado")
    elif color2 ==3 :
        print("El color resultante es Cafe")
    else:
        print("Revise su selección de colores color 2")
elif color1 == 2:
    if color2 == 1:
        print("El color resultante es Morado")
    elif color2 ==2:
        print("El color resultante es Azul")
    elif color2 ==3 :
        print("El color resultante es Cyan")
    else:
        print("Revise su selección de colores color 2")
elif color1 ==3:
    if color2 == 1:
        print("El color resultante es Cafe")
    elif color2 ==2:
        print("El color resultante es Cyan")
    elif color2 ==3 :
        print("El color resultante es verde")
    else:
        print("Revise su selección de colores")
else:
    print("Revise su selección de colores color 1")