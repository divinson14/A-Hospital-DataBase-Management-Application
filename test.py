class password :
    def __init__(self,mdp):
        self.mdp=mdp
    def passe(self):
        print(f"votre mot de passe est \t {self.mdp}")


#mot=str(input("Entrer ton mot de passe : "))
#resultat=password(mot)
#resultat.passe()

list=[]
i=str(input("Entrer : "))
for e in i :
    list.append(e)

print(list)


a='*'*2
b='*'*3


def pwd () :
    #f=len(list)-1
    taille=len(list)
    find = list[:taille]
    if ('a' in find) and ('b' in find):
        print(a + '\t + \t ' + b)
    if 'a' in find:
      print(a)
    if 'b' in find :
       print(b)
    if 'a ' not in find :
          print(TypeError)



pwd()