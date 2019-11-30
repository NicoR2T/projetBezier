#!/usr/bin/env python3

from tkinter import *
from functools import partial
from tkinter.messagebox import *
from math import *

root = Tk()

##########################Initialisation des fenêtres#########################
root['bg']='LightSkyBlue2'
root.geometry("1000x600-10+10")
root.title('Projet Bézier')
root.resizable(True, False)
#################################Left frame###################################
frame1 = LabelFrame(root, text='Widget', borderwidth=3, background='LightCyan4')
frame1.pack(side='left', padx=5, pady=5)

#################################Canvas#######################################
canvas = Canvas(root, width=800, height=600, background='black')
canvas.pack(side='right', padx=2, pady=2)
##############################################################################


#--------------FUNCTIONS-GRAPH-PART--------------#


#############################Callback##############################
def callback():
    if askyesno('Quitter', 'Etes-vous sûr de vouloir quitter ?'):
        quit()
    else:
        showinfo('Quitter', 'Une prochaine fois alors...')

############################Recup Radiobutton########################
def recupradiobutton():
    print(value.get())

###############Recup Listbox####################
def show_selection(label, choices, listbox):
    0
#    choices = choices.get()
#    text = ""
#    for index in listbox.curselection():
#        text += choices[index] + " "
#    lab3.config(text=text)
##########################Recup Spinbox#################################
#def recupspinbox1():
#   if value1 in values:
#   print(value1.get())

###########################Fonction Listbox###############################
#Valeur = listbox.getvar(listbox.cget('listvariable'))
#recupère la valeur de la listbox

#--------------GRAPH PART----------------#

##########Consigne 1##########
lab1 = Label(frame1, text='Choisissez le degré de la courbe', bg='LightCyan4').pack(side='top', padx=1, pady=1)

##########Spinbox##########
value1 = StringVar(frame1)
values = StringVar(frame1, ('Linéaire (1)','Quadratique (2)', 'Cubique (3)', '4', '5', '6', '7', '8', '9', '10'))
s = Spinbox(frame1, values=['Linéaire (1)','Quadratique (2)', 'Cubique (3)', '4', '5', '6', '7', '8', '9', '10'], bg='LightCyan4')
s.pack(side='top',padx=2, pady=2)

##########Radiobutton##########
value = StringVar(frame1)
bouton = Radiobutton(frame1, text="Courbe ouverte", variable=value, value='courbe ouverte', command=recupradiobutton, bg='LightCyan4')
bouton.pack(side='top', padx=2, pady=2)
bouton2 = Radiobutton(frame1, text="Courbe fermée", variable=value, value='courbe fermée', command=recupradiobutton, bg='LightCyan4')
bouton2.pack(side='top', padx=2, pady=1)

############Consigne 2##############
lab2 = Label(frame1, text='Nombre de points', bg='LightCyan4')
lab2.pack(side='top', padx=2, pady=2)

##########Spinbox##########
s = Spinbox(frame1, from_=0, to=10, bg='LightCyan4')
s.pack(side='top',padx=2, pady=2)

#########Listbox#########
choices = Variable(frame1, ('Bézier', 'Spline', 'B⁻spline', 'Nurb'))
listbox = Listbox(frame1, listvariable=choices, selectmode="single", bg='LightCyan4')
lab3 = Label(frame1, text='')
button = Button(frame1, text='Ok', command=partial(show_selection, lab3, choices, listbox), bg='LightBlue4')
listbox.pack(side='top',padx=2, pady=2)
button.pack(side='top',padx=2, pady=2)
lab3.pack(side='top',padx=2, pady=2)

###################Quitter###########################
button1 = Button(frame1,text='Quitter', command=callback, bg='LightBlue4')
button1.pack(side='bottom')

#--------------------PROGRAM PART----------------------#

###########functions###############
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
        points.append(canvas.create_oval(X[degre]-rayon,Y[degre]-rayon,X[degre]+rayon,Y[degre]+rayon, fill = 'DeepSkyBlue2'))
        canvas.tag_bind(points[degre], '<Enter>', partial(survoler, points[degre]))
        canvas.tag_bind(points[degre], '<Leave>', partial(survoler, points[degre]))
        deplace = partial(deplacer, canvas, rayon, degre)
        canvas.tag_bind(points[degre],'<B1-Motion>', deplace)
        if degre != 0:
            if degre>1:
                for elt in canvas.find_withtag("courbe"):
                    canvas.delete(elt)
            canvas.itemconfig(points[degre-1], fill='slate gray')
            for i in range(0,N):
                (coordsX,coordsY) = coor(degre,X,Y,t)
                canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline='LightCyan2',fill='LightCyan2')
                t+=1/N
        degre=degre+1

def deplacer(canvas, rayon, pointSelectionne, event):
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
            canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1, tags="courbe",outline='LightCyan2',fill='LightCyan2')
            t+=1/N
    canvas.update()

def survoler(item_id, event):
    global pointDetecte, pointSurvole
    if event.type == '7':
        canvas.itemconfig(item_id, fill='LightSkyBlue2')
        canvas.config(cursor='fleur')
        pointDetecte = True
        pointSurvole = item_id
    elif event.type == '8':
        if item_id == points[degre-1]:
            canvas.itemconfig(item_id, fill='DeepSkyBlue2')
        else:
            canvas.itemconfig(item_id, fill='slate gray')
        canvas.config(cursor='plus')
        pointDetecte = False
        pointSurvole = None

def suppPoint(event):
    global degre
    if degre >0:
        canvas.delete(points[-1])
        canvas.itemconfig(points[degre-2], fill='DeepSkyBlue2')
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
                    canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline='LightCyan2', fill='LightCyan2')
                    t+=1/N
    


def effacerTout():
    global points, degre, X, Y
    canvas.delete(ALL)
    points = []
    degre = 0
    X = []
    Y = []

#-----------------------PROGRAMME PRINCIPAL-----------------------#
degre = 0                         
X = []
Y = []
points = []
rayon = 10
pointDetecte = False
t=0
N=1000

canvas.bind('<Button-3>', suppPoint)
canvas.bind('<Button-1>', ajouterPoints)

###Redimensionnement###
#def redimensionnement(event):
#   global coords
#    touche = event.keysym

#canvas.bind('<MouseWheel>', redimensionnement)

def mouse_wheel(event):
    global count
    # respond to Linux or Windows wheel event
    if event.num == 5 or event.delta == -120:
        count -= 1
    if event.num == 4 or event.delta == 120:
        count += 1
    label['text'] = count
    print(label)

root.bind("<Button-4>", mouse_wheel)
root.bind("<Button-5>", mouse_wheel)

label = Label(root, font=('courier', 18, 'bold'), width=10)
label.pack(padx=40, pady=40)

root.mainloop()