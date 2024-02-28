from cryptography.fernet import Fernet
import psycopg2
#password=str(input("Entrez votre mot de passe : "))


def crypt():
    password = str(input("Entrez votre mot de passe : "))
    key_password=Fernet.generate_key()
    fernet_key= Fernet(key_password)
    password_encrypt=fernet_key.encrypt(password.encode())
    return fernet_key,password_encrypt,password
    #print(password + '\t'  'Hell Here ' )
    #print (password_encrypt )

def sauv_crypt():
    encrypt_password = crypt()
    conn = psycopg2.connect(
        user="postgres",
        password="siyam",
        host="localhost",
        port="5432",
        database="Hopital"
    )
    cur = conn.cursor()
    sql = "INSERT INTO public.password(id_matricule,password,fernet_key,password_encrypt) VALUES (%s,%s,%s,%s)"
    valeur=str(encrypt_password[0])
    valeur1=str(encrypt_password[1])
    vale = ["2238186",encrypt_password[2],valeur,valeur1]
    print(vale)
    cur.execute(sql, vale, )
    conn.commit()
    # fermeture de la connexion à la base de données
    cur.close()
    conn.close()


def retrouve_decrypt():
    conn = psycopg2.connect(
        user="postgres",
        password="siyam",
        host="localhost",
        port="5432",
        database="Hopital"
    )
    cur = conn.cursor()
    sql = "SELECT * FROM public.password where id_matricule = %s"
    #valeur = str(encrypt_password[0])
    #valeur1 = str(encrypt_password[1])
    vale = ["2238186"]
    print(vale)
    cur.execute(sql, vale )
    fetch=cur.fetchall()
    print(fetch[0:1])
    #print(fetch[1])
    #print(fetch[2])
    return fetch
    # fermeture de la connexion à la base de données
    cur.close()
    conn.close()


def decrypt():
    decrypt_password=crypt()
    print(decrypt_password)
    decryption=decrypt_password[0].decrypt(decrypt_password[1]).decode()
    if (decryption == decrypt_password[2]):
        print("OK")
    else :
         print("Mot de passe Incorrect")
         KeyError

def decrypt1():
    decrypt_password=retrouve_decrypt()
    print(decrypt_password)
    decryption=decrypt_password[2].decrypt(decrypt_password[3]).decode()
    if (decryption == decrypt_password[1]):
        print("OK")
    else :
         print("Mot de passe Incorrect")
         KeyError

#sauv_crypt()
retrouve_decrypt()
#decrypt1()