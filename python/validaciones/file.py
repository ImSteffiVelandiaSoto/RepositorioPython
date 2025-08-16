numero = int(input("Digite un número positivo"))
print(numero)
if numero<0:
    print(f"Por favor digite un numero positivo, usted digito {numero}") 
    numero=int(input("Por favor digite un numero y revise que sea positivo"))
    if numero<0:
        print(f"Por favor digite un numero positivo, usted digito {numero}") 
        numero=int(input("Por favor digite un numero y revise que sea positivo"))
print("Finalizo el programa ...")

