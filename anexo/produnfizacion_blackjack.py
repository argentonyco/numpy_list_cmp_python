# Numpy [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Black jack! [o algo parecido :)]

El objetivo es realizar una aproximación al juego de black jack,
el objetivo es generar una lista de 2 números aleatorios
entre 1 al 10 inclusive, y mostrar los "números" al usuario.

El usuario debe indicar al sistema si desea sacar más
números para sumarlo a la lista o no sacar más

A medida que el usuario vaya sacando números aleatorios que se suman
a su lista se debe ir mostrando en pantalla la suma total
de los números hasta el momento.

Cuando el usuario no desee sacar más números o cuando el usuario
haya superado los 21 (como la suma de todos) se termina la jugada
y se presenta el resultado en pantalla

BONUS Track: Realizar las modificaciones necesarias para que jueguen
dos jugadores y compitan para ver quien sacá la suma de números
más cercanos a 21 sin pasarse!
'''
import random

def tirada(cantidad_cartas):
    cartas = [random.randrange(1, 11) for i in range(cantidad_cartas)]
    return cartas

def jugador(jugador_num):
    input(f'Enter para la primer tirada "JUGADOR {jugador_num}"\n')
    lista_cartas = []
    
    lista_cartas = tirada(2)
    
    print(f'{lista_cartas} = {sum(lista_cartas)}')
        
    while sum(lista_cartas) <= 21:
        user_si_no = input('¿Desea otra carta? 1-SI 2-NO ')
        if user_si_no == '1':
            for i in range(1):
                cartas = random.randrange(1, 11) 
                lista_cartas.append(cartas)
                print(f'{lista_cartas} = {sum(lista_cartas)}')       
        else:
            print(f'"JUGADOR {jugador_num}" {lista_cartas} suman {sum(lista_cartas)}')            
            break
    else:
        print(f'"JUGADOR {jugador_num}" {lista_cartas} = {sum(lista_cartas)} PERDIO')
    return sum(lista_cartas)

if __name__ == '__main__':
    print("Ahora sí! buena suerte :)\n")
    # A partir de aquí escriba el código que resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
    
    puntaje_jugador_1 = jugador(1)
    
    puntaje_jugador_2 = jugador(2)
    
    if puntaje_jugador_1 > puntaje_jugador_2 and puntaje_jugador_1 <= 21:
        print(f'"JUGADOR 1" es el ganador.')
    elif puntaje_jugador_2 <= 21:
        print(f'"JUGADOR 2" es el ganador.')
    elif puntaje_jugador_1 > 21 and puntaje_jugador_2 > 21:
        print(f'"JUGADOR 1" y "JUGADOR 2" perdieron.')
    else:
        print(f'"JUGADOR 1" es el ganador.')
         
    print("terminamos")