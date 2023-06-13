from tkinter import *
import time
import tkinter
tk = Tk()

canvas = Canvas(tk, bg="white",width=(900),height=(500)) # resolucion
canvas.pack() 

platform = canvas.create_rectangle(400,400,500,410) #Plataforma

def ball():  #objeto de la bola
    xspeed = 2 # velocidad horizontal
    yspeed = 2 # vertical
    ball = canvas.create_oval(430,10,470,50) #dibujar bola
    while True:
        canvas.move(ball, xspeed, yspeed)
        pos = canvas.coords(ball)
        if pos[2] >=900 or pos[0] <0:
            xspeed = -xspeed
        tk.update()
        time.sleep(0.01)


def board(): #esquinas
    board_right()
    board_left()


def board_right(event): #esquina derechas
    xspeed = 5
    yspeed = 0
    canvas.move(platform,xspeed,yspeed)
    tk.update
    time.sleep(0.01)

def board_left(event): #esquina izquierda
    xspeed = 5
    yspeed = 0
    canvas.move(platform,-xspeed,yspeed)
    tk.update()
    time.sleep(0.01)


canvas.bind_all("<Right>",board_right)
canvas.bind_all("<Left>",board_left)
ball()
tk.mainloop() #lop mian
