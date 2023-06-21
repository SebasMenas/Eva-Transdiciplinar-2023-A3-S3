import math
import matplotlib.pyplot as plt

gravedad = 9.80


def Grafico(tiempo,altura):
    altura_lista = []
    tiempo_lista = []
    contador_decimal = 0
    index = 0

    while contador_decimal != tiempo:
        tiempo_lista.append(round(contador_decimal,2))
        posicion = altura - 4.9*tiempo_lista[index]**2
        altura_lista.append(posicion)

        if contador_decimal >= tiempo-0.01:
            break

        contador_decimal += 0.01
        index += 1

    plt.plot(tiempo_lista,altura_lista)
    plt.xlabel("tiempo")
    plt.ylabel("altura")
    plt.show()

def Altura_Tiempo(user_tiempo):
    user_altura = round((gravedad * user_tiempo**2) / 2,2)
    return user_altura

def Altura_Velocidad(user_velocidad):
    user_altura = round(user_velocidad**2/(2*gravedad),2)
    return user_altura

def Velocidad_Final(user_altura):
    user_velocidad = round(math.sqrt(2 * 9.80 * user_altura),2)
    return user_velocidad

def Tiempo(user_altura,user_velocidad):
    user_tiempo = round(2 * user_altura / user_velocidad,1)

    return user_tiempo

exit = False
while not exit:
    print("1-tiempo, 2-altura, 3-velocidad incial ")
    user_input = int(input("Opcion: "))
    if user_input == 1:
        user_tiempo = int(input(("tiempo: ")))
        user_altura_final = Altura_Tiempo(user_tiempo)
        user_velocidad_final = Velocidad_Final(user_altura_final)
        print("tiempo", user_tiempo)
        print("altura", user_altura_final)
        print("velocidad final", user_velocidad_final)
        Grafico(user_tiempo,user_altura_final)

    elif user_input == 2:
        user_altura = int(input("altura: "))
        user_velocidad_final = Velocidad_Final(user_altura)
        user_tiempo_final = Tiempo(user_altura,user_velocidad_final)
        print("tiempo ", user_tiempo_final)
        print("altura ", user_altura)
        print("velocidad final ", user_velocidad_final)
        Grafico(user_tiempo_final,user_altura)


    elif user_input == 3:
        user_velocidad = int(input("velocidad: "))
        user_altura_final = Altura_Velocidad(user_velocidad)
        user_tiempo_final = Tiempo(user_altura_final,user_velocidad)
        print("tiempo", user_tiempo_final)
        print("altura", user_altura_final)
        print("velocidad final ", user_velocidad)
        Grafico(user_tiempo_final,user_altura_final)







