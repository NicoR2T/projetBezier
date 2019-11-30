#!/usr/bin/env python3

from math import *
from tkinter import *

fen = Tk()

def coor(degre,X,Y,t):
	resX=0
	resY=0
	for i in range(0,degre+1):
		resX+=factorial(degre)/(factorial(i)*factorial(degre-i))*t**i*(1-t)**(degre-i)*X[i]
		resY+=factorial(degre)/(factorial(i)*factorial(degre-i))*t**i*(1-t)**(degre-i)*Y[i]
		
	return(resX,resY)


def ajouterPoints(event):
    global X, Y, degre, t
    X.append(event.x)
    Y.append(event.y)
    points.append(canvas.create_oval(X[degre]-rayon,Y[degre]-rayon,X[degre]+rayon,Y[degre]+rayon, fill = 'orange'))
    if degre != 0:
        if degre>1:
            for i in range(0,N):
                canvas.delete(lignes[-1])
                del lignes[-1]
        canvas.itemconfig(points[degre-1], fill='blue')
        for i in range(0,N):
            (coordsX,coordsY) = coor(degre,X,Y,t)
            lignes.append(canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,fill='purple'))
            t+=1/N
    degre=degre+1
    t=0

X=[]
Y=[]
points = []
lignes = []
rayon = 10
degre = 0
t=0
N=1000

canvas = Canvas(fen, width=500, height=500, background='white')

bou1 = Button(fen,text='Quitter',command=fen.quit)
bou1.pack(side=BOTTOM)

canvas.bind("<Button-1>", ajouterPoints)
canvas.pack()
fen.mainloop()

fen.destroy()