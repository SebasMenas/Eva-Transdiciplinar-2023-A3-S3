import math
import  matplotlib.pyplot as plt
altura = 1000
tiempo  = 0
Posicion = 1
Velocidad = 0
alturaLista = []
tiempoLista = []
TiempoFinal  = math.sqrt(2*altura/9.8)
print(round(TiempoFinal,2))
TiempoFinalEntero = int(TiempoFinal) + 1

contadorDecimal = 0

while contadorDecimal != TiempoFinal:
    tiempoLista.append(contadorDecimal)
    if contadorDecimal >= TiempoFinal-0.01:
        break
    contadorDecimal += 0.01

IOK = True
index = 0
while IOK:
    if index >= len(tiempoLista):
        IOK = False
    else:
        AlturaFormula = altura - 4.9*tiempoLista[index]**2

        alturaLista.append(AlturaFormula)
        print(AlturaFormula)
    index += 1


print(tiempoLista)
print(alturaLista)


plt.xlabel("Tiempo")
plt.ylabel("Altura")
plt.plot(tiempoLista,alturaLista)
plt.show()



