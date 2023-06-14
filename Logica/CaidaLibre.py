import math




def caida_libre(altura):
    altura_lista = []
    tiempo_lista = []
    tiempo_final = math.sqrt(2*altura/9.8)
    contador_decimal = 0
    index = 0
    print(tiempo_final)
    while contador_decimal != tiempo_final:
        tiempo_lista.append(round(contador_decimal,2))
        posicion = altura - 4.9*tiempo_lista[index]**2
        altura_lista.append(posicion)

        if contador_decimal >= tiempo_final:
            break

        contador_decimal += 0.01
        index += 1


    print(altura_lista)
    print(tiempo_lista)

caida_libre(25)
