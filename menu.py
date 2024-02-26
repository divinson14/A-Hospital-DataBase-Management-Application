from tkinter import *
from compl import *
import psycopg2
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
from PIL import Image,ImageTk



# C'est ici que je dois mettre le code pour la nouvelle fenetre pour l'insertion
def remplie():
    # remplie=Tk()
    # remplie.geometry("500x200")
    # remplie.config(bg='green')
    # remplie.title('Insertion des informations du Patient')
    compassion1 = Toplevel()
    compassion1.geometry("600x200")
    compassion1.config(bg="green")
    # 200c'est la longeur et 600 c'est la largeur
    compassion1.title("Insertion des informations du Patient ")
    # global c'est pour utiliser cela dans tout le programme
    id = Label(compassion1, text="ID du patient", bg='white')
    id.grid(row=0, column=4)
    id_entry = Entry(compassion1)
    id_entry.grid(row=0, column=8)
    nom = Label(compassion1, text="Nom du Patient", bg='white')
    nom.grid(row=2, column=4)
    nom_entry = Entry(compassion1)
    nom_entry.grid(row=2, column=8)
    cons_doc = Label(compassion1, text='A été reçu par de le DR.', bg='white')
    cons_doc.grid(row=4, column=4)
    doc = Entry(compassion1)
    doc.grid(row=4, column=8)
    type_service = Label(compassion1, text='Type de Service reçu ', bg='white')
    type_service.grid(row=8, column=4)
    ment = ttk.Combobox(compassion1, values=options)
    ment.grid(row=8, column=8)
    maladie = Label(compassion1, text="La maladie qu'on vous a détecté ", bg="white")
    maladie.grid(row=16, column=4)
    maladie_entry = Entry(compassion1)
    maladie_entry.grid(row=16, column=8)
    traitement = Label(compassion1, text="Les Soins Reçu ", bg="white")
    traitement.grid(row=32, column=4)
    traitement_entry = Entry(compassion1)
    traitement_entry.grid(row=32, column=8)
    # service=Listbox(remplie)
    # service.grid(row=8,column=8)
    date = Label(compassion1, text='La Date au quel tu as  reçu les soins ', bg="white")
    date.grid(row=64, column=4)
    day = ttk.Combobox(compassion1, text="Jour(Date)", values=options_jour, width=4, height=2)
    day.grid(row=64, column=8)
    month = ttk.Combobox(compassion1, values=options_mois, height=10, width=10)
    month.grid(row=64, column=16)
    year = ttk.Combobox(compassion1, height=10, width=10, values=options_annee)
    year.grid(row=64, column=32)
    # TODO je dois faire dans chaque case  que leur attribut apparaisse
    sauv = Button(compassion1, text="Sauvergarder  L'information ", bg="white", command= lambda : dauv(id_entry,nom_entry,maladie_entry,traitement_entry,doc,day,month,
                                                                                                    year ,ment, ))
    #recup(id_entry,nom_entry,doc,ment,maladie_entry,traitement_entry,day,month,year))
    # command=lambda : recup(id_entry,nom_entry,doc,maladie_entry,traitement_entry,day,month,year))
    sauv.grid(row=128, column=4)
    quite = Button(compassion1, text="Quitter la Page", bg="white", command=compassion1.destroy)
    quite.grid(row=128, column=8)
    compassion1.mainloop()
    return id_entry, nom_entry, doc, ment, maladie_entry, traitement_entry, day, month, year


def retire():
    compassion2 = Toplevel()
    compassion2.geometry("600x150")
    compassion2.config(bg="green")
    # 100  c'est la largeur et 400 c'est la longeur
    compassion2.title("Recherches  des informations sur Un Patient ")
    id = Label(compassion2, text="ID du patient", bg='white')
    id.grid(row=0, column=4)
    id_entry = Entry(compassion2)
    id_entry.grid(row=0, column=8)
    nom = Label(compassion2, text="Nom du Patient", bg='white')
    nom.grid(row=2, column=4)
    nom_entry = Entry(compassion2)
    nom_entry.grid(row=2, column=8)
    date = Label(compassion2, text='La Date au quel tu as  reçu les soins ', bg="white")
    date.grid(row=16, column=4)
    day = ttk.Combobox(compassion2, text="Jour(Date)", values=options_jour, width=4, height=2)
    day.grid(row=16, column=8)
    month = ttk.Combobox(compassion2, values=options_mois, height=10, width=10)
    month.grid(row=16, column=16)
    year = ttk.Combobox(compassion2, height=10, width=10, values=options_annee)
    year.grid(row=16, column=32)
    # TODO je dois faire dans chaque case  que leur attribut apparaisse
    retirer = Button(compassion2, text="Afficher le resultat", bg="white",command= lambda  : search(id_entry , nom_entry))
    retirer.grid(row=20, column=4)
    quite = Button(compassion2, text="Quitter la Page", bg="white", command=compassion2.destroy)
    quite.grid(row=20, column=8)
    compassion2.mainloop()
    return id_entry, nom_entry


def save1(ide,nom,maladie,traite):
    conn=psycopg2.connect(
        user="postgres",
        password="siyam",
        host="localhost",
        port="5432",
        database="Hopital"
    )
    cur=conn.cursor()
    sl="INSERT INTO public.patient(id_patient,nom,maladie,soins) VALUES (%s,%s,%s,%s)"
    valeu=[ide,nom,maladie,traite]
    print(valeu)
    cur.execute(sl,valeu,)
    conn.commit()
    # fermeture de la connexion à la base de données
    cur.close()
    conn.close()

def sav2(docteur,jour,mois,annee,menr):
    conn=psycopg2.connect(
        user="postgres",
        password="siyam",
        host="localhost",
        port="5432",
        database="Hopital"
    )
    cur=conn.cursor()
    sq="INSERT INTO public.dat(docteur,jour,month,annee,service) VALUES (%s,%s,%s,%s,%s)"
    vale=[docteur,jour,mois,annee,menr]
    print(vale)
    cur.execute(sq,vale,)
    conn.commit()
    # fermeture de la connexion à la base de données
    cur.close()
    conn.close()

def dauv(idin,name,sick,treat,nurse,jour,moi,ann,service):
    idi=idin.get()
    nam=name.get()
    sic=sick.get()
    trit=treat.get()
    nurs=nurse.get()
    j=jour.get()
    mo=moi.get()
    an=ann.get()
    ser=service.get()
    save1(idi,nam,sic,trit)
    sav2(nurs,j,mo,an,ser)
    print("fleur " + idi + nam+sic+trit+nurs+j+mo+an+ser)


def affiche (value):
    root = Toplevel()
    root.config(bg='dark blue')
    root.geometry("800x800")
    # Créer un objet PhotoImage de l'image dans le chemin spécifié
    image1 = Image.open("image.png")
    photo = ImageTk.PhotoImage(image1)
    # Créer une étiquette pour afficher l'image
    id_photo = Label(root,image=photo)
    id_photo.image = photo  # Garder une référence à l'image pour éviter la suppression par le garbage collector
    id_photo.pack(side=TOP, padx=5, pady=5)  # Afficher l'étiquette dans la fenêtre Tkinter

    # Valeur Obtenue
    Infor=Label(root,text=value[:0],bg='white')
    Infor.pack()
    Infor.place(relx=0.5, rely=0.5, anchor="center")
    Infor.config(font=22)
    print(value)

    Information = Label(root, text=value[0:1], bg='white')
    Information.pack(side=BOTTOM)
   # Information.place(relx=0.5, rely=0.5, anchor="center")
    Information.config(font=22)

    root.mainloop()


def search(info,info1):
    conn = psycopg2.connect(
        user="postgres",
        password="siyam",
        host="localhost",
        port="5432",
        database="Hopital"
    )
    cur = conn.cursor()
    #sl = "INSERT INTO public.patient(id_patient,nom,maladie,soins) VALUES (%s,%s,%s,%s)"
    do= info.get()
    do1=info1.get()


    if (do1 == '') :
     print("L'ID DU PATIENT  : "  + do)
     val="SELECT * FROM public.patient  where  id_patient = %s "
     cur.execute(val,(do,))
     idor=cur.fetchall()
     print(idor)
     #print("VOICI LES INFORMATIONS QUE VOUS AVIEZ DEMANDER :")
     #print(idor)
     # fermeture de la connexion à la base de données
     for i in idor :
         taille= len(i)
         #valeur=i[:taille]
    cur.close()
    conn.close()
    affiche(i)
    if (do == ''):
        print("Le NOM DU PATIENT  : " + do1)
        val = "SELECT * FROM public.patient  where  nom = %s "
        cur.execute(val, (do1,))
        idor = cur.fetchall()
        print("VOICI LES INFORMATIONS QUE VOUS AVIEZ DEMANDER :")
        print(idor)
        # fermeture de la connexion à la base de données
        cur.close()
        conn.close()
    if (do != '' and do1 != '') :
        print("L'ID DU PATIENT  : " + do)
        print("LE NOM  DU PATIENT  : " + do1)
        val = "SELECT * FROM public.patient  where  id_patient = %s  and  nom = %s"
        cur.execute(val, (do,do1))
        idor = cur.fetchall()
        print("VOICI LES INFORMATIONS QUE VOUS AVIEZ DEMANDER :")
        print(idor)
        # fermeture de la connexion à la base de données
        cur.close()
        conn.close()

def action():
    infor=Toplevel()
    infor.geometry("600x200")
    infor.config(bg="green")
    helper=Label(infor,text="Contacte le Service Client à L'adresse suivant divinsonsiyam@gmail.com  \n Contact : +237 653142685 \n Adress: Home ",bg='white')
    helper.config(font=20)
    helper.pack()
    helper.place(relx=0.5, rely=0.5, anchor="center")
   # adress=Label(infor,text="Contact ")
    infor.mainloop()



def rechercher():
    texte_recherche= simpledialog.askstring("Recherche","Entrez votre recherche : ")
    if texte_recherche :
        compassion.tag_remove("Orabf")
        messagebox.showinfo("Resultats de Recherche","Vous avez recherché : " + texte_recherche)
    else:
        messagebox.showinfo("Résultats de recherche ", "Aucun texte de recherche saisi. ")





#compassion = Toplevel()
compassion = Tk()


compassion.geometry("400x300")
compassion.title("Clinique Compassion 3S ")
compassion.config(bg='green')

barre_menu=Menu(compassion)
compassion.config(menu=barre_menu)

menu_fichier=Menu(barre_menu)
menu_fichier2=Menu(barre_menu)
menu_fichier3=Menu(barre_menu)

barre_menu.add_cascade(label="Nouveau",menu=menu_fichier)
barre_menu.add_cascade(label="Edit",menu=menu_fichier3)
barre_menu.add_cascade(label="Help",menu=menu_fichier2)


menu_fichier.add_command(label="Inserer",command=remplie)
menu_fichier.add_command(label="Extraire",command=retire)
menu_fichier.add_command(label="quit",command=compassion.destroy)

menu_fichier2.add_command(label="Info",command=action)


menu_fichier3.add_command(label="Search",command=rechercher)

salut = Label(compassion, text="Bienvenue chez la Clinique Compassion 3S ")
salut.pack(side=TOP, padx=5, pady=5)
# salut.grid(row=0)
salut.config(font=22)
action = Label(compassion, text="Que pouvons nous faire pour vous ! ")
action.pack()
action.place(relx=0.5, rely=0.5, anchor="center")
action.config(font=22)
# action.grid(row=2)

quitter = Button(compassion, text="Quitter de la page ", command=compassion.destroy, bg='white')
quitter.pack(side=BOTTOM)
quitter.config(font=20)

# quitter.grid(row=6)

sele = Button(compassion, text="Trouvez une information sur le patient ", bg='white', command=retire)
sele.pack(side=BOTTOM)
sele.config(font=20)
# sele.grid(row=5)

insert = Button(compassion, text="Entrer des informations sur le patient ", bg='white', command=remplie)
insert.pack(side=BOTTOM)
insert.config(font=20)
# insert.grid(row=4)
# TODO je dois faire du genre on doit afficher la dernière session qu'on a lance le programme

logo_img= Image.open("istockphoto-863958328-612x612.jpg")
logo=ImageTk.PhotoImage(logo_img)
'''logo_ico=Image.open("petits-medecins-patients-pres-illustration-vectorielle-plane-hopital-therapeute-masque-facial-disant-au-revoir-aux-personnes-gueries-pres-du-batiment-medical-ambulance-urgence-concept-clinique_74855-25338.ico")
icon=ImageTk.PhotoImage(logo_ico)

compassion.iconbitmap(bitmap=icon)
compassion.iconphoto(False,logo)
'''
compassion.mainloop()
