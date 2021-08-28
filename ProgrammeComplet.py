#!/usr/bin/env python3


# Second projet d'informatique
 
from tkinter import *
from functools import partial
from math import *
 
# --- définition des fonctions gestionnaires d'événements : ---
def coor(degre,X,Y,t):
    resX=0
    resY=0
    factdeg=factorial(degre)
    factinv = factdeg
    facto = 1
    for i in range(0,degre+1):
        if i > 0:
            facto *= i
            factinv = factinv/(degre-i+1)
        mult = factdeg/(facto*factinv)*t**i*(1-t)**(degre-i)
        resX+=mult*X[i]
        resY+=mult*Y[i]
        
    return(resX,resY)

def ajouterPoints(event):
    global X, Y, degre
    if not(pointDetecte):
        t = 0
        X.append(event.x)
        Y.append(event.y)
        points.append(canvas.create_oval(X[degre]-rayon,Y[degre]-rayon,X[degre]+rayon,Y[degre]+rayon, fill = 'orange'))
        canvas.tag_bind(points[degre], '<Enter>', partial(survoler, points[degre]))
        canvas.tag_bind(points[degre], '<Leave>', partial(survoler, points[degre]))
        canvas.tag_bind(points[degre],'<B1-Motion>', partial(deplacer, degre))
        if degre != 0:
            if degre>1:
                for elt in canvas.find_withtag("courbe"):
                    canvas.delete(elt)
            canvas.itemconfig(points[degre-1], fill='blue')
            for i in range(0,N):
                (coordsX,coordsY) = coor(degre,X,Y,t)
                canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline='dark green',fill='dark green')
                t+=1/N
        degre=degre+1

def deplacer(pointSelectionne, event):
    x=event.x
    y=event.y
    X[pointSelectionne]=x
    Y[pointSelectionne]=y
    canvas.coords(CURRENT,x-rayon,y-rayon,x+rayon,y+rayon)
    if degre>1:
        t=0
        for elt in canvas.find_withtag("courbe"):
            canvas.delete(elt)
        for i in range(0,N):
            (coordsX,coordsY) = coor(degre-1,X,Y,t)
            canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1, tags="courbe",outline='dark green',fill='dark green')
            t+=1/N
    canvas.update()

def survoler(item_id, event):
    global pointDetecte, pointSurvole
    if event.type == '7':
        canvas.itemconfig(item_id, fill='cyan')
        canvas.config(cursor='fleur')
        pointDetecte = True
        pointSurvole = item_id
    elif event.type == '8':
        if item_id == points[degre-1]:
            canvas.itemconfig(item_id, fill='orange')
        else:
            canvas.itemconfig(item_id, fill='blue')
        canvas.config(cursor='plus')
        pointDetecte = False
        pointSurvole = None

def suppPoint(event):
    global degre
    if degre >0:
        canvas.delete(points[-1])
        canvas.itemconfig(points[degre-2], fill='orange')
        del points[-1]
        del X[-1]
        del Y[-1]
        degre=degre-1
        if degre >=1:
            for elt in canvas.find_withtag("courbe"):
                canvas.delete(elt)
            if degre >1:
                t=0
                for i in range(0,N):
                    (coordsX,coordsY) = coor(degre-1,X,Y,t)
                    canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline='dark green', fill='dark green')
                    t+=1/N
    
def zoom(echelle, event):
    global rayon,X,Y
    x=event.x
    y=event.y
    canvas.scale(ALL,x,y,echelle,echelle)
    rayon*=echelle
    for i in range(0,degre):
        if X[i]>x:
            X[i]=(X[i]-x)*echelle+x
        else:
            X[i]=x-((x-X[i])*echelle)
        if Y[i]>y:
            Y[i]=(Y[i]-y)*echelle+y
        else:
            Y[i]=y-(y-Y[i])*echelle
    if degre >=1:
        for elt in canvas.find_withtag("courbe"):
            canvas.delete(elt)
        if degre >1:
            t=0
            for i in range(0,N):
                (coordsX,coordsY) = coor(degre-1,X,Y,t)
                canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline='dark green', fill='dark green')
                t+=1/N

def transClic(event):
    global xTrans, yTrans
    xTrans=event.x
    yTrans=event.y

def translation(event):
    global xTrans, yTrans
    x=event.x
    y=event.y
    for i in range(0,degre):
        X[i]+=x-xTrans
        Y[i]+=y-yTrans
        canvas.coords(points[i],X[i]-rayon,Y[i]-rayon,X[i]+rayon,Y[i]+rayon)
    xTrans=x
    yTrans=y
    if degre >=1:
            for elt in canvas.find_withtag("courbe"):
                canvas.delete(elt)
            if degre >1:
                t=0
                for i in range(0,N):
                    (coordsX,coordsY) = coor(degre-1,X,Y,t)
                    canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline='dark green', fill='dark green')
                    t+=1/N

def rotatInit(event):
    global xRota, yRota
    xRota = event.x
    yRota = event.y

def rotation(event):
    global xRota, yRota
    x=event.x
    y=event.y
    a=sqrt((xRota-centreX)**2+(yRota-centreY)**2)
    b=sqrt((x-centreX)**2+(y-centreY)**2)
    c=sqrt((xRota-x)**2+(yRota-y)**2)
    angle=acos((a**2+b**2-c**2)/(2*a*b))
    print(sqrt((X[0]-centreX)**2+(Y[0]-centreY)**2))
    for i in range(0,degre):
        X[i] = centreX + (X[i] - centreX) * cos(angle) - (Y[i] - centreY) * sin(angle)
        Y[i] = centreY + (X[i] - centreX) * sin(angle) + (Y[i] - centreY) * cos(angle)
        canvas.coords(points[i],X[i]-rayon,Y[i]-rayon,X[i]+rayon,Y[i]+rayon)
    xRota=x
    yRota=y
    if degre >=1:
            for elt in canvas.find_withtag("courbe"):
                canvas.delete(elt)
            if degre >1:
                t=0
                for i in range(0,N):
                    (coordsX,coordsY) = coor(degre-1,X,Y,t)
                    canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline='dark green', fill='dark green')
                    t+=1/N


def effacerTout():
    global points, degre, X, Y
    canvas.delete(ALL)
    points = []
    degre = 0
    X = []
    Y = []

#------ Programme principal -------
 
# les variables suivantes seront utilisées de manière globale :
degre = 0                         
X = []
Y = []
points = []
rayon = 10
pointDetecte = False
N=100
echelleZoom=1.2
echelleDezoom=0.8
centreX=250
centreY=250
# Création du widget principal ("maître") :
fen = Tk()
# création des widgets "esclaves" :
canvas = Canvas(fen,bg='white',height=500,width=500, cursor='plus')
canvas.pack(side=LEFT)
bou1 = Button(fen,text='Quitter',command=fen.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen,text='Effacer',command=effacerTout)
bou2.pack()

canvas.bind('<Shift-Button-1>',transClic)
canvas.bind('<Shift-B1-Motion>', translation)
canvas.bind('<Control-Button-1>',rotatInit)
canvas.bind('<Control-B1-Motion>',rotation)
canvas.bind('<Button-1>', ajouterPoints)
canvas.bind('<Button-3>', suppPoint)
canvas.bind('<Button-4>',partial(zoom,echelleZoom))
canvas.bind('<Button-5>',partial(zoom,echelleDezoom))
#canvas.bind('<Control-B1-Motion>', rotation)
fen.mainloop()              # démarrage du réceptionnaire d'événements