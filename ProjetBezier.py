#!/usr/bin/env python3

from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import *
from functools import partial
from math import *
from random import *

root = Tk()

##########################Initialisation des fenêtres#########################
root['bg']='#A4A4A4'
root.geometry("1000x600-10+10")
root.title('Projet Bézier')
#################################Left frame###################################
frame0 = LabelFrame(root, borderwidth=0, background='#A4A4A4')
frame0.pack(side='left', padx=1, pady=1)

frame3 = LabelFrame(frame0, text='Options', borderwidth=3, background='LightGrey')
frame3.pack(side='top', padx=1, pady=1)

frame1 = LabelFrame(frame0, text='Widgets', borderwidth=3, background='LightGrey')
frame1.pack(side='top', padx=1, pady=1)

frame2 = LabelFrame(frame0, borderwidth=3, background='LightGrey')
frame2.pack(side='bottom', padx=1, pady=1)

##########################Points################################################
#framePoints = LabelFrame(root, borderwidth=0, background='#A4A4A4')
#framePoints.pack(side='right', padx=1, pady=1)

framex = LabelFrame(frame3, borderwidth=0, background='LightGrey')
framex.pack(side='left', padx=1, pady=1)

framey = LabelFrame(frame3, borderwidth=0, background='LightGrey')
framey.pack(side='right', padx=1, pady=1)

#################################Canvas#######################################
canvas = Canvas(root, width=800, height=600, background='white')
canvas.pack(side='right', padx=2, pady=2)

#--------------FUNCTIONS-GRAPH-PART--------------#

#########################Scale in Menubar#############################

# Auteur: Gauthier
# Pré-condition: 0
# Post-condition: points, degre, X, Y
def effacerTout():
    global points, degre, X, Y
    canvas.delete(ALL)
    points = []
    degre = 0
    X = []
    Y = []

# Auteur: Axel
# Pré-condition: 0
# Post-condition: 0
def info():
    showinfo('Informations', 'Un programme réalisé par Nicolas.T & Axel.R & Gauthier.C')

# Auteur: Gauthier
# Pré-condition: 0
# Post-condition: clrPoint
def colorPoints():
	global clrPoint
	color = askcolor()
	clrPoint = color[1]
	for elmt in canvas.find_withtag("points"):
		canvas.itemconfig(elmt,fill=clrPoint)
	canvas.itemconfig(points[degre-1],fill='DeepSkyBlue2')

# Auteur: Gauthier
# Pré-condition: 0
# Post-condition: clrCourbe
def colorCourbe():
	global clrCourbe
	color = askcolor()
	clrCourbe = color[1]
	for elmt in canvas.find_withtag("courbe"):
		canvas.itemconfig(elmt,outline=clrCourbe,fill=clrCourbe)

# Auteur: Axel
# Pré-condition: 0
# Post-condition: 0
def callback():
    if askyesno('Quitter', 'Etes-vous sûr de vouloir quitter ?'):
        quit()

# Auteur: Axel
# Pré-condition: 0
# Post-condition: courbe
def recupRadiobutton():
    global courbe
    courbe = value.get()

# Auteur: Gauthier
# Pré-condition: event
# Post-condition: degre
def nbrePoints(event):
	global degre
	degre = nombrePoints.get()

# Auteur: Gauthier
# Pré-condition: event
# Post-condition: rayon, degre, points
def rynPoints(event):
	global rayon, degre, points
	rayon = rayonPoints.get()
	if degre>0 & tracer==True:
		for elmt in canvas.find_withtag("points"):
			canvas.delete(elmt)
		points=[]
		for i in range(0,degre-1):
			points.append(canvas.create_oval(X[i]-rayon,Y[i]-rayon,X[i]+rayon,Y[i]+rayon,tags="points", fill = clrPoint))
		points.append(canvas.create_oval(X[degre-1]-rayon,Y[degre-1]-rayon,X[degre-1]+rayon,Y[degre-1]+rayon,tags="points", fill = 'DeepSkyBlue2'))
		print(points)

# Auteur: Gauthier
# Pré-condition: event
# Post-condition: echelleZoom, echelleDezoom
def echlZoom(event):
	global echelleZoom, echelleDezoom
	echelleZoom= echelleDuZoom.get()
	echelleDezoom=2-echelleDuZoom.get()
###############Recup Listbox####################
# Auteur: Nicolas
# Pré-condition: 0
# Post-condition: tracer, points, X, Y
def tracerCourbe():
    global tracer, X, Y, points
    if tracer==False:
        tracer=True
        if degre==0:
            showinfo("Attention","Vous n'avez choisi aucun point")
        else:
            for i in range(0,degre):
                X.append(randint(0,800))
                Y.append(randint(0,600))
                points.append(canvas.create_oval(X[i]-rayon,Y[i]-rayon,X[i]+rayon,Y[i]+rayon,tags="points", fill = clrPoint))
                canvas.tag_bind(points[i], '<Enter>', partial(survoler, points[i]))
                canvas.tag_bind(points[i], '<Leave>', partial(survoler, points[i]))
                canvas.tag_bind(points[i],'<B1-Motion>', partial(deplacer, i))
            canvas.itemconfig(points[degre-1], fill='DeepSkyBlue2')
            t=0
            for i in range(0,N):
                (coordsX,coordsY) = coor(degre-1,X,Y,t)
                canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline=clrCourbe,fill=clrCourbe)
                t+=1/N
    else:
        canvas.delete(ALL)
        points = []
        X=[]
        Y=[]
        tracer=False
        tracerCourbe()

tracer=False
#--------------GRAPH PART----------------#


##########Options##########
nombrePoints=Scale(frame3, label="Modifier le nombre de points", from_=0, to=100, orient="horizontal", length=210,command=nbrePoints)
nombrePoints.pack(side="top", padx=1, pady=1)

rayonPoints=Scale(frame3, label="Rayon des points de contrôle", from_=0, to=20, orient="horizontal", length=210, command=rynPoints)
rayonPoints.pack(side="top", padx=1, pady=1)

echelleDuZoom=Scale(frame3, label="Echelle du zoom", from_=1.0, to=2.0,resolution=0.01, orient="horizontal", length=210, command=echlZoom)
echelleDuZoom.pack(side="top", padx=1, pady=1)

nombrePoints.set(0)
rayonPoints.set(10)
echelleDuZoom.set(1.2)

##########Consigne 1##########
lab1 = Label(frame1, text='Choisissez le degré de la courbe', font= 'Verdana 10 underline', bg='LightGrey')
lab1.pack(side='top', padx=1, pady=1)

##########Spinbox##########
value1 = StringVar(frame1)
values = StringVar(frame1, ('Linéaire (1)','Quadratique (2)', 'Cubique (3)', '4', '5', '6', '7', '8', '9', '10'))
s = Spinbox(frame1, values=['Linéaire (1)','Quadratique (2)', 'Cubique (3)', '4', '5', '6', '7', '8', '9', '10'], bg='#E6E6E6',state='disabled')
s.pack(side='top',padx=1, pady=1)

##########Radiobutton##########
value = IntVar()
bouton = Radiobutton(frame1, text="Courbe ouverte", variable=value, value=0, command=recupRadiobutton, bg='#E6E6E6', highlightcolor='#FFFFFF')
bouton.pack(side='top', padx=1, pady=1)
bouton2 = Radiobutton(frame1, text="Courbe fermée", variable=value, value=1, command=recupRadiobutton, bg='#E6E6E6', highlightcolor='#FFFFFF',state='disabled')
bouton2.pack(side='top', padx=1, pady=1)

##########Consigne 2##########
lab1 = Label(frame1, text='Choisissez le type de courbe', font= 'Verdana 10 underline', bg='LightGrey')
lab1.pack(side='top', padx=1, pady=1)

#########Listbox#########
choices = Variable(frame1, ('Bézier'))
listbox = Listbox(frame1, listvariable=choices, selectmode="single", bg='#E6E6E6')
button = Button(frame1, text='Ok', command=tracerCourbe, bg='#E6E6E6', highlightcolor='#FFFFFF', width=10)
listbox.pack(side='top',padx=1, pady=1)
button.pack(side='top',padx=1, pady=1)

###################Quitter###########################
button1 = Button(frame2,text='Quitter', command=callback, bg='#E6E6E6', highlightcolor='#FFFFFF', width=10)
button1.pack(side='bottom',padx=70,pady=10)

##########Menu Bar##########
menubar = Menu(root)
menu1 = Menu(menubar, tearoff=0)

menu1.add_command(label="Couleur des points", command=colorPoints)
menu1.add_command(label="Couleur de la courbe", command=colorCourbe)
menu1.add_command(label="Effacer tout", command=effacerTout)
menubar.add_cascade(label="Editer", menu=menu1)
 
menu2 = Menu(menubar, tearoff=0)
 
menu2.add_command(label="A propos", command=info)
menubar.add_cascade(label="Options", menu=menu2)
 
root.config(menu=menubar)

#--------------------PROGRAM PART----------------------#

###########functions###############
# Auteur: Axel
# Pré-condition: degre,X,Y,t
# Post-condition: resX, resY
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

# Auteur: Gauthier
# Pré-condition: event
# Post-condition: X,Y,degre
def ajouterPoints(event):
    global X, Y, degre
    if not(tracer):
    	showerror("Erreur","Veuillez rentrer les paramètres et appuyer sur ok")
    else:	
	    if not(pointDetecte):
	        t = 0
	        X.append(event.x)
	        Y.append(event.y)
	        points.append(canvas.create_oval(X[degre]-rayon,Y[degre]-rayon,X[degre]+rayon,Y[degre]+rayon,tags="points", fill = 'DeepSkyBlue2'))
	        canvas.tag_bind(points[degre], '<Enter>', partial(survoler, points[degre]))
	        canvas.tag_bind(points[degre], '<Leave>', partial(survoler, points[degre]))
	        canvas.tag_bind(points[degre],'<B1-Motion>', partial(deplacer, degre))
	        if degre != 0:
	            if degre>1:
	                for elt in canvas.find_withtag("courbe"):
	                    canvas.delete(elt)
	            canvas.itemconfig(points[degre-1], fill=clrPoint)
	            for i in range(0,N):
	                (coordsX,coordsY) = coor(degre,X,Y,t)
	                canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline=clrCourbe,fill=clrCourbe)
	                t+=1/N
	        degre=degre+1

# Auteur: Nicolas
# Pré-condition: pointSelectionne, event
# Post-condition: 0
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
            canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1, tags="courbe",outline=clrCourbe,fill=clrCourbe)
            t+=1/N
    canvas.update()

# Auteur: Axel
# Pré-condition: item_id, event
# Post-condition: pointDetecte, pointSurvole
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
            canvas.itemconfig(item_id, fill=clrPoint)
        canvas.config(cursor='plus')
        pointDetecte = False
        pointSurvole = None

# Auteur: Gauthier
# Pré-condition: event
# Post-condition: degre
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
                    canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline=clrCourbe, fill=clrCourbe)
                    t+=1/N

# Auteur: Nicolas
# Pré-condition: echelle, event
# Post-condition: rayon, X, Y    
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
                canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline=clrCourbe, fill=clrCourbe)
                t+=1/N

# Auteur: Nicolas
# Pré-condition: event
# Post-condition: xTrans, yTrans
def transClic(event):
    global xTrans, yTrans
    xTrans=event.x
    yTrans=event.y

# Auteur: Nicolas
# Pré-condition: event
# Post-condition: xTrans, yTrans
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
                    canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline=clrCourbe, fill=clrCourbe)
                    t+=1/N

# Auteur: Nicolas
# Pré-condition: event
# Post-condition: xRota, yRota
def rotatInit(event):
    global xRota, yRota
    xRota = event.x
    yRota = event.y

# Auteur: Nicolas
# Pré-condition: event
# Post-condition: xRota, yRota
def rotation(event):
    global xRota, yRota
    x=event.x
    y=event.y
    a=sqrt((xRota-centreX)**2+(yRota-centreY)**2)
    b=sqrt((x-centreX)**2+(y-centreY)**2)
    c=sqrt((xRota-x)**2+(yRota-y)**2)
    angle=acos((a**2+b**2-c**2)/(2*a*b))
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
                    canvas.create_oval(coordsX-1,coordsY-1,coordsX+1,coordsY+1,tags="courbe",outline=clrCourbe, fill=clrCourbe)
                    t+=1/N

#-----------------------PROGRAMME PRINCIPAL-----------------------#
degre = 0                         
X = []
Y = []
points = []
rayon = 10
pointDetecte = False
N=1000
echelleZoom=1.2
echelleDezoom=0.8
centreX=400
centreY=300
clrCourbe='LightCyan2'
clrPoint='slategray'

canvas.bind('<Shift-Button-1>',transClic)
canvas.bind('<Shift-B1-Motion>', translation)
canvas.bind('<Control-Button-1>',rotatInit)
canvas.bind('<Control-B1-Motion>',rotation)
canvas.bind('<Button-1>', ajouterPoints)
canvas.bind('<Button-3>', suppPoint)
canvas.bind('<Button-4>',partial(zoom,echelleZoom))
canvas.bind('<Button-5>',partial(zoom,echelleDezoom))


root.mainloop()
