import math
import matplotlib.pyplot as plt

def caida_libre(altura, gravedad,metrica):
    mundos = {"Tierra" : 9.8, "Luna":1.62,"Saturno":10.44,"Neptuno":11.15,"Jupiter":24.79}
    altura_lista = []
    tiempo_lista = []
    tiempo_final = math.sqrt(2*altura/gravedad)
    contador_decimal = 0
    index = 0
    lugar = ""

    while contador_decimal != tiempo_final:
        tiempo_lista.append(round(contador_decimal,2))
        posicion = altura - (grave/2)*tiempo_lista[index]**2
        altura_lista.append(posicion)

        if contador_decimal >= tiempo_final-0.01:
            break

        contador_decimal += 0.01
        index += 1

    for key,value in mundos.items():
        if gravedad == value:
            lugar = key



    # Fig es la "figura" resultante del grafico de ax
    # ax es el unico grafico
    fig, ax = plt.subplots()
    ax.plot(tiempo_lista, altura_lista, label="Altura")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Altura ("+metrica+")")
    ax.set_title("Caída libre de un objeto en " + lugar )
    ax.legend()

    return fig



def datos_tabla(altura, gravedad):
    tiempo_final = math.sqrt(2*altura/gravedad)
    velocidad_final = math.sqrt(2 * gravedad * altura)
    tabla_tiempo = []
    tabla_altura = []
    tabla_velocidad = []


    altura_dividida = altura / 24
    altura_sumada = 0
    for i in range(0,25):
        tabla_altura.append(round(altura_sumada,2))

        altura_sumada += altura_dividida

    tabla_altura.reverse()


    tiempo_divido = tiempo_final / 24
    tiempo_sumado = 0
    for j in range(0,25):
        tabla_tiempo.append(round(tiempo_sumado,2))
        tiempo_sumado += tiempo_divido


    velocidad_dividida = velocidad_final / 24
    velocidad_sumada = 0
    for k in range(0,25):
        tabla_velocidad.append(round(velocidad_sumada,2))
        velocidad_sumada += velocidad_dividida


    return tabla_altura,tabla_tiempo, tabla_velocidad

