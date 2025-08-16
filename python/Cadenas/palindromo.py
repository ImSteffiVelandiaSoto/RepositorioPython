def palindromo(cadena):
    # quitamos espacios
    cadenaSin =cadena.replace(" ","")
    print(cadenaSin)
    #pasar a minuscula
    cadenaMin = cadenaSin.lower()
    print(cadenaMin)
    print(f"La cadena original es {cadenaMin}")
    print(f"La cadena al reves es {cadenaMin[::-1]}")
    if cadenaMin == cadenaMin[::-1]:
        print("El texto es palindromo")
    else:
        print("El texto no es palindromo")

    




texto = input("Escriba la frase o palabra a evaluar: ")
palindromo(texto)
