
"""Schreibt die Werte einer bestimmten Koordinate in ein Dictionary
    und berechnet die Monatsmittel in einem zweiten Dictionary
    und schreibt diese in eine Datei"""

import os

dir_in = ".../Temperatur/"  #Input Folder
dir2= ".../Klimadiagramme/" #Output Folder

#Dateinamen abfragen, Datei erstellen, "a" fuer append = Daten anhaengen
name = raw_input("Dateiname zum speichern: ")
w = open(dir2 + name + ".txt", "a")


#Definiere je ein leeres Dictionary
dic = {}
dicMon = {}

#Funktion zur Beschneidung der Dezimalstellen 
def trunc(f, n):
    return ('%.*f' % (n + 1, f))[:-1]

    
#Einlesen der Werte und umwandeln der Strings in Integer
Hstr = raw_input("Hochwert: ")
H = int(Hstr)
Rstr = raw_input("Rechtswert: ")
R = int(Rstr)

#Erste Zeile der Datei schreiben
w.write("Year" + " " + "Month" + " " + "Value" + "R/H" + Rstr + "/" + Hstr +"\n")

#Umrechnung Hochwert/Rechtswert in Zellennummer; +11 da das 11. 'Wort' den ersten Datenpunkt darstellt
k = (((5990000 - H)/100*3600+1)+((R - 3330000)/100)) + 11

#Start- und Endjahr automatisch aus dem Verzeichnis auslesen
ListStart = os.listdir(dir_in)[0]
ListStartStr = ListStart[12:16]
ListStartInt = int(ListStartStr)

if len(os.listdir(dir_in)[-1]) < 15:
    ListEnd = os.listdir(dir_in)[-2]
    ListEndStr = ListEnd[12:16]
    ListEndInt = int(ListEndStr)
else:
    ListEnd = os.listdir(dir_in)[-1]
    ListEndStr = ListEnd[12:16]
    ListEndInt = int(ListEndStr)


#Daten fuer jedes Jahr (1. for Schleife) komplett durchsuchen
#Das jeweilige Jahr (2. for Schleife bzw. if Bedingung) berechnen
print "Schreibe Datenpunkte in Library"
for i in range(ListStartInt, ListEndInt + 1):
    for x in os.listdir(dir_in):
        iStr = str(i)
        xStr = str(x)
        if iStr == x[12:16]:

            #Testet ob Daten Temperaturwerte und .asc Dateien sind
            if x[0:4] == "temp" and x[33:37] == ".asc":
                
                #Datei oeffnen. Attribut r, damit nur gelesen wird aus Datei
                f = open(dir_in + x, "r")

                #Ascii Datei in Strings unterteilen, die durch Leerzeichen getrennt sind
                d = f.read().split()

                #Den k-ten Wert aus der .asc Datei unter definiertem Namen ins dictionary eintragen
                dic[x[12:16] + "-" + x[17:19] + "-" + x[20:21]] = d[k]
                print "."
                f.close()

            #Testet ob Daten Niederschlagswerte und .asc Dateien sind
            elif x[0:4] == "prec" and x[33:37] == ".asc":

                #Datei oeffnen. Attribut r, damit nur gelesen wird aus Datei
                f = open(dir_in + x, "r")

                #Ascii Datei in Strings unterteilen, die durch Leerzeichen getrennt sind
                d = f.read().split()

                #Den k-ten Wert aus der .asc Datei unter definiertem Namen ins dictionary eintragen
                dic[x[14:18] + "-" + x[19:21] + "-" + x[22:23]] = d[k]
                print "."
                f.close()

            else:
                continue
        else:
            continue
    


#Monatsmittelwerte bilden
print "\n Berechne Monatsmittel"
for i in range(ListStartInt, ListEndInt + 1):
    for x in range(1,13):
        iStr = str(i)
        xStr = str(x)

# Unterscheiden zwischen Schreibweisen,
# da in den Datennamen nicht 1 sonder 01 steht --> Probleme
        if x < 10:
            if iStr + "-0" + xStr + "-0" in dic: #testet ob Monat vorhanden
                v0Str = dic[iStr + "-0" + xStr + "-0"]
                v1Str = dic[iStr + "-0" + xStr + "-1"]
                v2Str = dic[iStr + "-0" + xStr + "-2"]
            else:
                continue
        else:
            if iStr + "-" + xStr + "-0" in dic:
                v0Str = dic[iStr + "-" + xStr + "-0"]
                v1Str = dic[iStr + "-" + xStr + "-1"]
                v2Str = dic[iStr + "-" + xStr + "-2"]
            else:
                continue
            
        #Umwandeln der Werte in float
        v0Flo,v1Flo,v2Flo = float(v0Str),float(v1Str),float(v2Str)
        
        #Mittelwerte bilden
        div = (v0Flo + v1Flo + v2Flo) / 3

        #Mittelwerte mit 2 Dezimalstellen in Dictionary eintragen
        dicMon[iStr + "-" + xStr] = trunc(div, 2)
        
        #Eintrag aus dem Dictionary in die Datei schreiben
        w.write(iStr + " " + xStr + " " + dicMon[iStr + "-" + xStr] + "\n")
        
        print "."



w.close()
print "Fertig!"







    
    
