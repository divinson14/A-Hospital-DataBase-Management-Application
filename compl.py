import  datetime


options = ["Consultation", "Chirugie", "Opthamologie", "Pediatrie", "Soins Intensif"]
options_jour = []
for jour in range(1, 31):
        options_jour.append(jour)

options_mois=["Janvier","Fevrier","Mars","Avril","Mai","Juin","Juillet","Août","Septembre","Octobre","Novembre","Decembre"]


date_actuelle=datetime.date.today()
annee_actuelle=date_actuelle.year
options_annee=[]
for year in range(2020,annee_actuelle+1):
    options_annee.append(year)