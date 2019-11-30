#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
from tkinter import *
from functools import partial

#----------------------------------
# procedure mouve : deplace un objet du canevas par rapport au centre de la figure
# preconditions : cnvs : canevas
#		lng, haut : dimensions de la forme graphique
# 		event : evenement souris capté
# post-condition : canevas redessine
def mouve(cnvs, lng, haut, event):
	x=event.x
	y=event.y
	cnvs.coords(CURRENT,x-lng/2,y-haut/2,x+lng/2,y+haut/2)
	cnvs.update()

fen = Tk() # Creation de la fenetre principale
canvas = Canvas(fen, width=500, height=500, background='white') # Creation du canevas

# Rectangle : définition du point de reference
(xc0,yc0) = (75, 10)
# dimensions du rectangle
(lngC, hautC) = (250, 100)
# dessin du rectangle
rect = canvas.create_rectangle(xc0, yc0, xc0 + lngC, yc0 + hautC, fill='grey')
# fonction partielle avec les dimensions du rectangle
bougeCarre = partial(mouve, canvas, lngC, hautC)
# attachement du comportement sur mouvement de la souris, bouton 1 appuye
canvas.tag_bind(rect, '<B1-Motion>', bougeCarre) 

# cercle : définition du point de reference 
(xr0,yr0) = (200,200)
# dimensions du cercle
(lngR, hautR) = (150, 150)
# dessin du cercle
rond = canvas.create_oval(xr0, yr0, xr0+lngR, yr0+hautR, fill='orange')
# fonction partielle avec les dimensions du cercle
bougeRond = partial(mouve, canvas, lngR, hautR)
# attachement du comportement sur mouvement de la souris, bouton 1 appuye
canvas.tag_bind(rond, '<B1-Motion>', bougeRond) 

canvas.pack()
fen.mainloop() 
