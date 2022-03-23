# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Utilizar comprensión de listas para filtrar

    accesos = [10, 50, 7, 5, 15, 25, 3, 4, 13]

    # La lista accesso contiene los números de ID de personal
    # que ingresaron por ese molinete

    # 1)
    # Generar una lista por comprensión de la lista "accesos"
    # una lista que solo contenga (filtrado) los ID de personal
    # entre 1 al 10 inclusive, se desea separar del grupo de accesos
    # los ID entre el 1 y 10.
    # De la lista resultante informar cuantas personas/personal
    # comprendido en dicho rango pasó por ese molinete

    # personal_1_10 = [.....]
    
    personal_1_10 = [id for id in accesos if id <= 10]
    contador_molinete = len(personal_1_10)
    print(f'{personal_1_10} Pasaron {contador_molinete} personas del personal\n')
    
    # 2)
    # Generar una lista por comprensión de la listas "accesos"
    # cuyo ID de personal esté dentro de los ID válidos para ingresar
    # por ese molinete:
    id_validos = [3, 4, 7, 8, 15]
    # Debe generar una nueva lista basada en "accesos" filtrada por los ID
    # aprobados en "id_validos".
    # TIP: Utilizar el operador "in" para chequear si un ID de accesos está
    # dentro de "id_validos"

    personal_valido = [id for id in accesos if id in id_validos]

    print(personal_valido)
    
    print("terminamos")