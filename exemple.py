#!/usr/bin/env python3

from tkinter import *
from functools import partial

root = Tk()

##########Initialisation geometrique##########
root['bg']='darkgrey'
root.geometry("1000x600-10+10")
root.title('Projet Bézier')
##############################################

###############Fonction Listbox####################
def show_selection(label, choices, listbox):
    choices = choices.get()
    text = ""
    for index in listbox.curselection():
        text += choices[index] + ""
###################################################

#Left frame
frame1 = LabelFrame(root, text='Widget', borderwidth=3, background='white')
frame1.pack(side='left', padx=5, pady=5)


#Right frame
#frame2 = Frame(paned, borderwidth=5, relief='groove')
#frame2.pack(side='top', padx=5, pady=5)

##########Consignes##########
lab1 = Label(frame1, text='Choisissez le degré de la courbe', bg='white').pack(side='top', padx=1, pady=1)
#############################

##########Spinbox##########
s = Spinbox(frame1, values=['Linéaire', 'Quadratique', 'Cubique'], bg='white')
s.pack(side='top',padx=2, pady=2)
##################################

##########Checkbutton##########
value = StringVar(frame1)
bouton = Radiobutton(frame1, text="Courbe ouverte", variable=value, value=1, bg='white')
bouton.pack(side='top', padx=2, pady=2)
bouton2 = Radiobutton(frame1, text="Courbe fermée", variable=value, value=2, bg='white')
bouton2.pack(side='top', padx=2, pady=1)
###############################

##########Canvas##########
canvas = Canvas(root, width=800, height=600, background='grey')
rect_id = canvas.create_rectangle((10,10),(20, 20), fill="green")
rect_id2 = canvas.create_rectangle((10,10),(20, 20), fill="green")
rect_id3 = canvas.create_rectangle((10,10),(20, 20), fill="green")
canvas.pack(side='right', padx=2, pady=2)

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
##########################

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
##################################################

button1 = Button(frame1,text='Quitter', command=root.quit, bg='white')
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

root.mainloop()
###########################