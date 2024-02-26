from tkinter import  *
import psycopg2

passion= Tk()


def mdp_resp(mdp_ans, matricule_ans):
    conn = psycopg2.connect(
        user="postgres",
        password="siyam",
        host="localhost",
        port="5432",
        database="Hopital"
    )
    cur = conn.cursor()
    val = "SELECT mdp FROM public.password  where  id_matricule  = %s"
    # cur.execute(val, (mdp_ans,matricule_ans))
    cur.execute(val, (matricule_ans,))
    answer = cur.fetchall()
    # fermeture de la connexion à la base de données
    cur.close()
    conn.close()
    if (mdp_ans == answer):
        reaction=Label(passion, text="Bienvenue ", bg='white')
        reaction.config(font=22)
        #reaction.grid(row=2, column=4)
        # TODO peux faire du genre quand le mot de passe sera correct s'affiche bienvenu Mr t-elle
        #TODO faire un pack pour la position de la reaction en haut et ajouter les valeur dans la base de donnee
    else:
        reaction2 = Label(passion, text=" Mot de passe Incorrect ", bg='white')
        #reaction2.grid(row=2, column=4)



passion.geometry("400x300")
passion.config(bg='green')
passion.title("Clinique Compassion 3S")
salut = Label(passion, text="Bienvenue chez la Clinique Compassion 3S ")
salut.pack(side=TOP, padx=5, pady=5)
salut.config(font=22)

matricule3=Label(passion,text="Entrer votre matricule ", bg='white')
#matricule3.grid(row=0,column=4)

matricule_request=Entry(passion)
#matricule_request.grid(row=0,column=8)

mdp= Label(passion,text="Entrer votre mot de passe ",bg='white')
#mdp.grid(row=1,column=8)

mdp_request=Entry(passion)
mdp_request.pack(side=BOTTOM)
#mdp_request.grid(row=1,column=8)

mdp_reqansw=mdp_request.get()
matricule_reqansw=matricule_request.get()

enter=Button(passion,text="Enter/Entrer",bg='white',command=mdp_resp(mdp_reqansw,matricule_reqansw))
enter.pack(side=BOTTOM)
enter.config(font=22)

passion.mainloop()