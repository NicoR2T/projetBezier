#!/usr/bin/env python3


# Second projet d'informatique
 
from tkinter import *
from functools import partial
 
# --- définition des fonctions gestionnaires d'événements : ---
def ajouterPoints(event):
    global X, Y, nbre_points
    if not(pointDetecte):
        X.append(event.x)
        Y.append(event.y)
        points.append(canvas.create_oval(X[nbre_points]-rayon,Y[nbre_points]-rayon,X[nbre_points]+rayon,Y[nbre_points]+rayon, fill = 'orange'))
        canvas.tag_bind(points[nbre_points], '<Enter>', partial(survoler, points[nbre_points]))
        canvas.tag_bind(points[nbre_points], '<Leave>', partial(survoler, points[nbre_points]))
        deplace = partial(deplacer, canvas, rayon, nbre_points)
        canvas.tag_bind(points[nbre_points],'<B1-Motion>', deplace)
        if nbre_points != 0:
            canvas.itemconfig(points[nbre_points-1], fill='blue')
            lignes.append(canvas.create_line(X[nbre_points-1],Y[nbre_points-1],X[nbre_points],Y[nbre_points],width=1,fill='purple'))
        nbre_points=nbre_points+1

def deplacer(canvas, rayon, pointSelectionne, event):
    x=event.x
    y=event.y
    X[pointSelectionne]=x
    Y[pointSelectionne]=y
    canvas.coords(CURRENT,x-rayon,y-rayon,x+rayon,y+rayon)
    if pointSelectionne == 0:
        canvas.coords(lignes[pointSelectionne],X[pointSelectionne],Y[pointSelectionne],X[pointSelectionne+1],Y[pointSelectionne+1])
    elif lignes[pointSelectionne-1] == lignes[-1]:
        canvas.coords(lignes[pointSelectionne-1],X[pointSelectionne-1],Y[pointSelectionne-1],X[pointSelectionne],Y[pointSelectionne])
    else:
        canvas.coords(lignes[pointSelectionne-1],X[pointSelectionne-1],Y[pointSelectionne-1],X[pointSelectionne],Y[pointSelectionne])
        canvas.coords(lignes[pointSelectionne],X[pointSelectionne],Y[pointSelectionne],X[pointSelectionne+1],Y[pointSelectionne+1])
    canvas.update()

def survoler(item_id, event):
    global pointDetecte, pointSurvole
    if event.type == '7':
        canvas.itemconfig(item_id, fill='cyan')
        canvas.config(cursor='fleur')
        pointDetecte = True
        pointSurvole = item_id
    elif event.type == '8':
        if item_id == points[nbre_points-1]:
            canvas.itemconfig(item_id, fill='orange')
        else:
            canvas.itemconfig(item_id, fill='blue')
        canvas.config(cursor='plus')
        pointDetecte = False
        pointSurvole = None

def suppPoint(event):
    global nbre_points
    if nbre_points > 1:
        canvas.delete(points[-1])
        canvas.delete(lignes[-1])
        del points[-1]
        del lignes[-1]
        del X[-1]
        del Y[-1]
        nbre_points = nbre_points-1
        canvas.itemconfig(points[nbre_points-1], fill='orange')
    elif nbre_points == 1:
        canvas.delete(points[-1])
        del points[-1]
        del X[-1]
        del Y[-1]
        nbre_points = nbre_points-1


def effacerTout():
    global points, lignes, nbre_points, X, Y
    canvas.delete(ALL)
    points = []
    nbre_points = 0
    X = []
    Y = []
    lignes = []

#------ Programme principal -------
 
# les variables suivantes seront utilisées de manière globale :
nbre_points = 0                         
X = []
Y = []
points = []
lignes = []
rayon = 10
pointDetecte = False
# Création du widget principal ("maître") :
fen = Tk()
# création des widgets "esclaves" :
canvas = Canvas(fen,bg='white',height=500,width=500, cursor='plus')
canvas.pack(side=LEFT)
bou1 = Button(fen,text='Quitter',command=fen.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen,text='Effacer',command=effacerTout)
bou2.pack()

canvas.bind('<Button-3>', suppPoint)
canvas.bind('<Button-1>', ajouterPoints)
 
fen.mainloop()              # démarrage du réceptionnaire d'événements
 
fen.destroy()               # destruction (fermeture) de la fenêtre
