import matplotlib.pyplot as plt
import datetime
import pygame as py
import sys

screen = py.display.set_mode((400,800))
g = -9.8

def Create_Sprite():
    sprites = [] 
    sprites.append(py.image.load('sphere.png'))
    sprites.append(py.image.load('tree.png'))
    sprites.append(py.image.load('mouse.png'))
    return sprites


def Background():
    screen.blit(sprites[1],(000,000))


def Mouse():
    screen.blit(sprites[2],(eMx-10,eMy-10))
    return

def Sphere():
    screen.blit(sprites[0],(eSphereX,eSphereY))
    
sprites = Create_Sprite()
run = True
py.display.set_caption("Caida Libre")
eMx = 0
eMy = 0
eSphereX = 200
eSphereY = 630


while run:
    py.init()
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            print("click")
        if event.type == py.MOUSEMOTION:
            eMx, eMy = event.pos 
            if eMx >= 400:
                eMx = 400
            if eMy >= 640:
                eMy = 630

    Background()
    Mouse()
    Sphere()
    print(eMx,eMy)
    py.display.flip()


    