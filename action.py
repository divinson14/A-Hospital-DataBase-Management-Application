import psycopg2
#from recup import *

def insert ():
    conn = psycopg2.connect(
            user="postgres",
            password="siyam",
            host="localhost",
            port="5432",
            database="Hopital"
        )
    cur = conn.cursor()
    sql="INSERT INTO public.patient(id_patient,nom,maladie,groupe_sangin) VALUES (%s,%s,%s,%s)"
    #values=recup()
    #valeur=(values[0],values[1],values[3],values[4])
    valeur=("s","sr","rt","43")
    cur.execute(sql,valeur)
    #texter = "String"
    #sql="INSERT INTO public.val(lol)  VALUES (%s)"

        # Afficher la version de PostgreSQL et nous avons seulement pu connecter la base de Donnée du au temps
         #cur.execute("SELECT version();")
    #cur.execute(sql,(texter,))

    conn.commit()
    # fermeture de la connexion à la base de données
    cur.close()
    conn.close()

insert()