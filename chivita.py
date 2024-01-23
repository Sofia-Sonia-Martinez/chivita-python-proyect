import random

cont = 0
n = 10
todos_animales = ["el lobo", "el perro", "el gato", "el toro", "el tiburon"] * 20  # Repite la lista 20 veces para tener 100 animales

llamar_a = {}

def elemento_seleccionado(lista):
    # Elige un elemento de la lista y luego elimínalo para evitar repeticiones
    seleccionado = random.choice(lista)
    lista.remove(seleccionado)
    return seleccionado

print("Sal de ahi chivita chivita, sal de ahi de ese lugar")
cont += 1
actualmente = "la chiva"

for _ in range(n):
    todos_animales = ["el lobo", "el perro", "el gato", "el toro", "el tiburon"] * 20
    
    prox = elemento_seleccionado(todos_animales)
    llamar_a[actualmente] = prox
    print("Hay que llamar a " + prox + " para que saque a " + actualmente)
    cont += 1
    actualmente = prox
    remover = []
    inspeccionar = "la chiva"
    
    while inspeccionar in llamar_a:
        remover.insert(0, llamar_a[inspeccionar] + " no quiere sacar a " + inspeccionar)
        cont += 1
        inspeccionar = llamar_a[inspeccionar]
    
    for i in remover:
        print(i)
    
    print("La chiva no quiere salir de ahi. Sal de ahi chivita chivita, sal de ahi de ese lugar")
    cont += 1
    print(cont)
