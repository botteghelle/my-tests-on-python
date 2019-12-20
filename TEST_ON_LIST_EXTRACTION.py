# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 15:18:47 2019

@author: Emanuele NUZZO
"""
list_for_menu_inflaction = [2016,2017,2018,2019]
from tkinter import *
 
w = Tk()
 
# création listbox
lbx = Listbox(w)
for i in range(0,len(list_for_menu_inflaction)): 
    lbx.insert(i, list_for_menu_inflaction[i])
#lbx.insert(0, "Riri")
#lbx.insert(1, "Fifi")
#lbx.insert(2, "Loulou")
lbx.select_set(0)
lbx.grid(row=0, column=0)
 
# on crée une variable StringVar() pour stocker la
# valeur de l'item sélectionné
selected_item = StringVar()
 
# fonction appelée avec le bouton
def updateLabel():
    line = lbx.curselection()[0]
    global item
    item = lbx.get(line)
    # on affecte la valeur de l'item à la variable :
    selected_item.set(item)
 
# bouton
bt = Button(w, text="Get item", command=updateLabel)
bt.grid(row=1, column=0)
 
# label qui affiche l'item sélectionné
# on utilise une option textvariable pour
# le lier à l'objet StringVar qu'on a défini auparavant
lbl = Label(w, textvariable=selected_item)
lbl.grid(row=2, column=0)
 
w.mainloop()
print(item)
