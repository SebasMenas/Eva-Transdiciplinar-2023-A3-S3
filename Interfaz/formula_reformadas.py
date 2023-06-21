import math
import matplotlib.pyplot as plt

gravedad = 9.80


def Altura_Tiempo(user_tiempo):
    user_altura = round((gravedad * user_tiempo**2) / 2,2)
    print(user_altura)
    return user_altura

def Altura_Velocidad(user_velocidad):
    user_altura = round(user_velocidad**2/(2*gravedad),2)
    return user_altura

def Velocidad_Final(user_altura):
    user_velocidad = round(math.sqrt(2 * 9.80 * user_altura),2)
    return user_velocidad

def Tiempo(user_altura,user_velocidad):
    user_tiempo = round(2 * user_altura / user_velocidad,2)
    return user_tiempo

exit = True
while not exit:
    print("1-tiempo, 2-altura, 3-velocidad incial ")
    user_input = int(input("Opcion: "))
    if user_input == 1:
        user_tiempo = int(input(("tiempo: ")))
        user_altura_final = Altura_Tiempo(user_tiempo)
        user_velocidad_final = Velocidad_Final(user_altura_final)
        print("altura", user_altura_final)
        print("velocidad final", user_velocidad_final)

    elif user_input == 2:
        user_altura = int(input("altura: "))
        user_velocidad_final = Velocidad_Final(user_altura)
        user_tiempo_final = Tiempo(user_altura,user_velocidad_final)
        print("velocidad final ", user_velocidad_final)
        print("tiempo", user_tiempo_final)
    elif user_input == 3:
        user_velocidad = int(input("velocidad: "))
        user_altura_final = Altura_Velocidad(user_velocidad)
        user_tiempo_final = Tiempo(user_altura_final,user_velocidad)
        print("altura", user_altura_final)
        print("tiempo", user_tiempo_final)






