#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
from tkinter import *              # GUI
from tkinter.ttk	import *	     # Widgets avec themes
from functools import partial  # used for partial function application



#----------------------------------
# Fonction : getMusiciens
# Parametre : groupe : numéro et nom du groupe
# Brief : Retourne la liste des musiciens ontenus dans "Musiciens.txt" du groupe 
def getMusiciens(groupe) :
    res = list() # Liste résultat
    num = groupe.split(" ")[0]  # numero du groupe
    # Ouverture en lecture du fichier contenant les musiciens
    objFic = open("Musiciens.txt", "r")
    # Lecture de la premiere ligne
    ligne = objFic.readline()
    # Tant qu'on n'est pas arrivé à la fin du fichier, cad que la ligne n'est pas vide
    while (ligne != "") :
        # Si la ligne commence par le numéro
        if (ligne.startswith(num)) :
            # On transforme la ligne pour être sous le format [musicien, instrument]
            ligneTmp = ligne[0:-1].split(";")
            musicien = ligneTmp[1]
            instrument = ligneTmp[2]
            res.append([musicien, instrument])
        # On lit la ligne suivante
        ligne = objFic.readline()
    # Une fois le fichier parcouru entierement, on ferme le fichier
    objFic.close()
    # On retourne le résultat obtenu
    return res
#----------------------------------

#----------------------------------
# Fonction : getGroupes
# Brief : Retourne la liste des groupes contenus dans "Groupes.txt"
def getGroupes() :
    res = list() # Liste résultat
    # Ouverture en lecture du fichier contenant les groupes
    objFic = open("Groupes.txt", "r")
    # Lecture de la premiere ligne
    ligne = objFic.readline()
    # Tant qu'on n'est pas arrivé à la fin du fichier, cad que la ligne n'est pas vide
    while (ligne != "") :
        # On transforme la ligne pour être sous le format numero - nom
        ligneTmp = ligne[0:-1].split(";")
        groupe = ligneTmp[0]+" - "+ligneTmp[1]
        res.append(groupe)
        # On lit la ligne suivante
        ligne = objFic.readline()
    # Une fois le fichier parcouru entierement, on ferme le fichier
    objFic.close()
    # On retourne le résultat obtenu
    return res
#----------------------------------


#----------------------------------
# Fonction : change_listes
# Parametre : listeMusicien : ListBox des musiciens
#                   listeInstrument : ListBox des instruments
#                   var : StringVar du Combobox
# Brief : Change la valeur des listes en fonction du groupe sélectionné dans la combobox
def change_listes(listeMusicien, listeInstrument, var):
    # On recupere les musiciens + instruments pour le groupe de la combobox
    musinstr = getMusiciens(var.get())
    # On vide les deux listes
    listeMusicien.delete(0, END)
    listeInstrument.delete(0, END)
    # On ajoute parallelement dans chaque liste pour garder la correspondance
    for i,mi in enumerate(musinstr,1) :
        listeMusicien.insert(i, mi[0])
        listeInstrument.insert(i, mi[1])
#----------------------------------


# Creation de la fenetre principale
fenetre = Tk()

# Creation de la combobox pour choisir le groupe
nomsGroupes = getGroupes()
groupeSelectionne = StringVar()
comboGroupe = Combobox(fenetre, textvariable=groupeSelectionne , values=nomsGroupes )

# Creation d'une Frame pour les listes
f1 = Frame(fenetre)

# Creation de la liste de musicien
labelMusicien = Label(f1,text="Musicien")
listeMusicien = Listbox(f1)

# Creation de la liste d'instrument
labelInstrument = Label(f1,text="Instrument")
listeInstrument = Listbox(f1)

# Creation du bouton pour valider
photo = PhotoImage(file="disk.gif")
buttonOk = Button(fenetre, image=photo, command=partial(change_listes, listeMusicien, listeInstrument, groupeSelectionne))

# Ajout des elements graphiques dans la frame
labelMusicien.grid(row=0, column=0)
labelInstrument.grid(row=0, column=1)
listeMusicien.grid(row=1, column=0, padx=5, pady=5)
listeInstrument.grid(row=1, column=1, padx=5, pady=5)

# Ajout des elements graphiques dans la fenetre
comboGroupe.grid(row=0,column=0, padx=5, pady=5)
f1.grid(row=1,column=0, padx=20, pady=20)
buttonOk.grid(row=2, column=0, padx=5, pady=5)

# Lancement de l'interface graphique
fenetre.mainloop()
