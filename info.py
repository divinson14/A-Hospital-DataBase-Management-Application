import psycopg2
from arduino import *


def base():

 try:
    conn = psycopg2.connect(
        user="postgres",
        password="siyam",
        host="localhost",
        port="5432",
        database="my_db"
    )
    cur = conn.cursor()
    info = intox()
    # Afficher la version de PostgreSQL
    cur.execute("SELECT *  FROM TABLE WHERE colone= %s ",(info,))
    position= cur.fetchone()

    # fermeture de la connexion à la base de données
    cur.close()
    conn.close()
    print("La connexion PostgreSQL est fermée")


    for row in position :
        ld="L'information sur la postion de ACAR " + row +"\n"
        return ld
 except (Exception, psycopg2.Error) as error:
    print("Erreur lors de la connexion à PostgreSQL", error)


def distance():

 try:
    conn = psycopg2.connect(
        user="postgres",
        password="siyam",
        host="localhost",
        port="5432",
        database="my_db"
    )
    cur = conn.cursor()
    info = intox()
    # Afficher la version de PostgreSQL
    cur.execute("SELECT *  FROM TABLE WHERE colone= %s ",(info,))
    position= cur.fetchone()

    # fermeture de la connexion à la base de données
    cur.close()
    conn.close()
    print("La connexion PostgreSQL est fermée")


    for row in position :
        ld="L'information sur la distance de ACAR " + row +"\n"
        return ld
 except (Exception, psycopg2.Error) as error:
    print("Erreur lors de la connexion à PostgreSQL", error)

