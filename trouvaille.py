from  tkinter import *
from tkinter import ttk
from compl import *

def retire():
#remplie=Tk()
    #remplie.geometry("500x200")
    #remplie.config(bg='green')
    #remplie.title('Insertion des informations du Patient')
    compassion2=Tk()#Toplevel()
    compassion2.geometry("600x150")
    compassion2.config(bg="green")
    #100  c'est la largeur et 400 c'est la longeur
    compassion2.title("Recherches  des informations sur Un Patient ")
    id=Label(compassion2,text="ID du patient",bg='white')
    id.grid(row=0,column=4)
    id_entry=Entry(compassion2)
    id_entry.grid(row=0,column=8)
    nom=Label(compassion2,text="Nom du Patient",bg='white')
    nom.grid(row=2,column=4)
    nom_entry=Entry(compassion2)
    nom_entry.grid(row=2,column=8)
    date=Label(compassion2,text='La Date au quel tu as  reçu les soins ',bg="white")
    date.grid(row=16, column=4)
    day=ttk.Combobox(compassion2,text="Jour(Date)",values=options_jour,width=4,height=2)
    day.grid(row=16,column=8)
    month=ttk.Combobox(compassion2,values=options_mois,height=10,width=10)
    month.grid(row=16,column=16)
    year=ttk.Combobox(compassion2,height=10,width=10,values=options_annee)
    year.grid(row=16, column=32)
    #TODO je dois faire dans chaque case  que leur attribut apparaisse
    retirer=Button(compassion2,text="Afficher le resultat",bg="white",)
    retirer.grid(row=20,column=4)
    quite=Button(compassion2,text="Quitter la Page",bg="white")
    quite.grid(row=20,column=8)
    compassion2.mainloop()


retire()