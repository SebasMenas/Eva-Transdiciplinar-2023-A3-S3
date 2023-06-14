import tkinter 
import time
from tkinter import *

tk = Tk()
Res = [400,600] #Resolucion
panta = Canvas(tk, width= Res[0], height= Res[1]) #pantalla principal (aun falta escalarla)
panta.pack() # se llama a esta funcion para hacer los diferentes cambios
grav,_suelo = (9.8),500,    #Gravedad(9,8 (m/s)^2), Nivel del suelo referente a la pantalla
panta.create_line(0,500,400,500) #linea del suelo

def obj_fall(PosInicial,tiempodereproduccion):
    global grav, pY,_suelo  #llamar a globales
    _y  = _suelo-PosInicial #donde empezara a caer (esto esta en Metros)
    _V  = 0                 #velocidad
    ball = panta.create_oval(70,10,70+40,10+40,fill= "RED") #dibujar pelota
    _on = True
    while _on:
        panta.move(ball, 0, _V)            #para que la bola se mueva
        _V += grav                         #aumentar la velocidad con la aceleracion
        _y += _V                           #aumentar la posicion del objeto
        print(_y)
        if _y + _V >= _suelo:              #si la posicion con la velocidad llegan a superar la distancia del suelo
            _y  = _suelo                   #dejar el objeto en el suelo
            _V  = 0                        #la velocidad es 0 para
            panta.moveto(ball, 70, _y-40)  #dibujar que cayo al suelo  
            _on = False                    #terminar while
        time.sleep(VPS)                    #tiempo en que reproduce todo
        tk.update()                        
            
obj_fall(600,0.0375)
tk.mainloop()