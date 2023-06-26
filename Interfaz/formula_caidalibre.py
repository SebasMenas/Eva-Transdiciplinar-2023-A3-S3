import math
import matplotlib.pyplot as plt

def caida_libre(altura, gravedad):
    altura_lista = []
    tiempo_lista = []
    tiempo_final = math.sqrt(2*altura/gravedad)
    contador_decimal = 0
    index = 0

    while contador_decimal != tiempo_final:
        tiempo_lista.append(round(contador_decimal,2))
        posicion = altura - 4.9*tiempo_lista[index]**2
        altura_lista.append(posicion)

        if contador_decimal >= tiempo_final-0.01:
            break

        contador_decimal += 0.01
        index += 1

    # Fig es la "figura" resultante del grafico de ax
    # ax es el unico grafico
    fig, ax = plt.subplots()
    ax.plot(tiempo_lista, altura_lista, label="Altura")
    ax.set_xlabel("Tiempo (s)")
    ax.set_ylabel("Altura (m)")
    ax.set_title("Caída libre de un objeto")
    ax.legend()

    return fig
