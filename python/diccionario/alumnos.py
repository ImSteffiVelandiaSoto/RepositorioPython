estudiantes = {
    "Ana": 4.5,
    "Carlos":3.8,
    "Camilo":4.9
}
#Crear funciones agregar estudiante nuevo
def agregar(diccionario, nombre, nota):
    diccionario[nombre]=nota
    print(f"Estudiante {nombre} agregado con la nota {nota} con exito")
#Funcion para buscar la nota
def buscar(diccionario, nombre):
    return diccionario.get(nombre, "Estudiante no fue encontrado")
def mostrar(diccionario):
    for nombre, nota in diccionario.items():
        print(f" el estudiante: {nombre} tiene una nota de: {nota}")

agregar(estudiantes, "Juan", 4.0)
print("Nota de Ana: ", buscar(estudiantes, "Ana"))
mostrar(estudiantes)