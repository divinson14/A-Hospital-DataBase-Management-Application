import serial

import serial

def intox():
 # Configure la connexion série
 #ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
 ser = serial.Serial('COM7',9600,timeout=1)
 while True:
    # Lit les données depuis la connexion série
    pos = ser.readline().decode('utf-8').rstrip()
    pos=str(pos)
    pin = pos%10
    if pin == 3 :
     # Affiche la valeur lue dans la console
     data="Valeur lue : "+ pos
     return data
