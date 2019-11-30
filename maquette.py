#!/usr/bin/env python3

from tkinter import *
from functools import partial
from tkinter.messagebox import *
import math

root = Tk()

##########################Initialisation des fenêtres#########################
root['bg']='darkgrey'
root.geometry("1000x600-10+10")
root.title('Projet Bézier')
root.resizable(True, False)
#################################Left frame###################################
frame1 = LabelFrame(root, text='Widget', borderwidth=3, background='white')
frame1.pack(side='left', padx=5, pady=5)

#################################Canvas#######################################
canvas = Canvas(root, width=800, height=600, background='grey')
rect_id = canvas.create_rectangle((10,10),(20, 20), fill="green")
rect_id2 = canvas.create_rectangle((10,10),(20, 20), fill="green")
rect_id3 = canvas.create_rectangle((10,10),(20, 20), fill="green")
canvas.pack(side='right', padx=2, pady=2)
##############################################################################


#--------------FUNCTIONS-GRAPH-PART--------------#

###################Animation optionnelle###############
def move_rectangle():
    coords = canvas.coords(rect_id)
    if coords[1] <= 560:
        coords[1] = 580
        coords[3] = 590
    else:
        coords[1] += -4
        coords[3] += -4
    root.after(70, move_rectangle)
    canvas.coords(rect_id, *tuple(coords))
root.after(70, move_rectangle)

def move_rectangle2():
    coords = canvas.coords(rect_id2)
    if coords[1] <= 560:
        coords[0] = 30
        coords[1] = 580
        coords[2] = 40
        coords[3] = 590
    else:
        coords[0] = 30
        coords[1] += -4
        coords[2] = 40
        coords[3] += -4
    root.after(70, move_rectangle2)
    canvas.coords(rect_id2, *tuple(coords))
root.after(70, move_rectangle2)

def move_rectangle3():
    coords = canvas.coords(rect_id3)
    if coords[1] <= 560:
        coords[0] = 50
        coords[1] = 580
        coords[2] = 60
        coords[3] = 590
    else:
        coords[0] = 50
        coords[1] += -4
        coords[2] = 60
        coords[3] += -4
    root.after(70, move_rectangle3)
    canvas.coords(rect_id3, *tuple(coords))
root.after(70, move_rectangle3)

#############################Callback##############################
def callback():
    if askyesno('Quitter', 'Êtes-vous sûr de vouloir quitter ?'):
        quit()
    else:
        showinfo('Quitter', 'Une prochaine fois alors...')

############################Recup Radiobutton########################
def recupradiobutton():
	print(value.get())

###############Recup Listbox####################
def show_selection(label, choices, listbox):
    choices = choices.get()
    text = ""
    for index in listbox.curselection():
        text += choices[index] + " "
    lab3.config(text=text)
##########################Recup Spinbox#################################
#def recupspinbox1():
#	if value1 in values:
#	print(value1.get())

###########################Fonction Listbox###############################
#Valeur = listbox.getvar(listbox.cget('listvariable'))
#recupère la valeur de la listbox

#--------------GRAPH PART----------------#

##########Consigne 1##########
lab1 = Label(frame1, text='Choisissez le degré de la courbe', bg='white').pack(side='top', padx=1, pady=1)

##########Spinbox##########
value1 = StringVar(frame1)
values = StringVar(frame1, ('10', '9', '8', '7', '6', '5', 'Cubique (4)', 'Quadratique (3)', 'Linéaire (2)'))
s = Spinbox(frame1, values=['10', '9', '8', '7', '6', '5', 'Cubique (4)', 'Quadratique (3)', 'Linéaire (2)'], bg='white')
s.pack(side='top',padx=2, pady=2)

##########Radiobutton##########
value = StringVar(frame1)
bouton = Radiobutton(frame1, text="Courbe ouverte", variable=value, value='courbe ouverte', command=recupradiobutton, bg='white')
bouton.pack(side='top', padx=2, pady=2)
bouton2 = Radiobutton(frame1, text="Courbe fermée", variable=value, value='courbe fermée', command=recupradiobutton, bg='white')
bouton2.pack(side='top', padx=2, pady=1)

############Consigne 2##############
lab2 = Label(frame1, text='Nombre de points', bg='white')
lab2.pack(side='top', padx=2, pady=2)

##########Spinbox##########
s = Spinbox(frame1, from_=0, to=10, bg='white')
s.pack(side='top',padx=2, pady=2)

#########Listbox#########
choices = Variable(frame1, ('Bézier', 'Spline', 'B⁻spline', 'Nurb'))
listbox = Listbox(frame1, listvariable=choices, selectmode="single", bg='white')
lab3 = Label(frame1, text='')
button = Button(frame1, text='Ok', command=partial(show_selection, lab3, choices, listbox), bg='white')
listbox.pack(side='top',padx=2, pady=2)
button.pack(side='top',padx=2, pady=2)
lab3.pack(side='top',padx=2, pady=2)

###################Quitter###########################
button1 = Button(frame1,text='Quitter', command=callback, bg='white')
button1.pack(side='bottom')

##########Menu Bar##########
def alert():
    showinfo("alerte", "Bravo!")

menubar = Menu(root)
	
menu1 = Menu(menubar, tearoff=0)

menu1.add_command(label="Créer", command=alert)
menu1.add_command(label="Couper", command=alert)
menu1.add_command(label="Copier", command=alert)
menubar.add_cascade(label="Editer", menu=menu1)

menu2 = Menu(menubar, tearoff=0)

menu2.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Options", menu=menu2)

root.config(menu=menubar)

#--------------------PROGRAM PART----------------------#

###########functions###############
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

#######################ROTATION##############################
# a square
xy = [(50, 50), (150, 50), (150, 150), (50, 150)]

polygon_item = canvas.create_polygon(xy)

center = 100, 100

def getangle(event):
    dx = canvas.canvasx(event.x) - center[0]
    dy = canvas.canvasy(event.y) - center[1]
    try:
        return complex(dx, dy) / abs(complex(dx, dy))
    except ZeroDivisionError:
        return 0.0 # cannot determine angle

def press(event):
    # calculate angle at start point
    global start
    start = getangle(event)

def motion(event):
    # calculate current angle relative to initial angle
    global start
    angle = getangle(event) / start
    offset = complex(center[0], center[1])
    newxy = []
    for x, y in xy:
        v = angle * (complex(x, y) - offset) + offset
        newxy.append(v.real)
        newxy.append(v.imag)
    canvas.coords(polygon_item, *newxy)

canvas.bind("<Control-Button-1>", press)
canvas.bind("<Control-B1-Motion>", motion)

#-----------------------PROGRAMME PRINCIPAL-----------------------#
nbre_points = 0 
count = 0                        
X = []
Y = []
points = []
lignes = []
rayon = 10
pointDetecte = False

canvas.bind('<Button-3>', suppPoint)
canvas.bind('<Button-1>', ajouterPoints)

###Redimensionnement###
#def redimensionnement(event):
#	global coords
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

root.bind("<Button-4>", mouse_wheel)
root.bind("<Button-5>", mouse_wheel)

label = Label(root, font=('courier', 18, 'bold'), width=10)
label.pack(padx=40, pady=40)

root.mainloop()