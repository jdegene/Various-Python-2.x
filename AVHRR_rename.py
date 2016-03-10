
# Kopiert AVHRR Daten in einen neuen Ordner und gibt ihnen eine neue Endung
# Kopiert eine existierende Header Datei mehrfach mit Namen der AVHRR Dateien
#  in den gleichen Ordner mit der Endung .hdr

# Voraussetzungen
# Ueberorder ist .../AVHRR/
#  Unterordner sind .../AVHRR/Data/   -> enthaelt Original Daten
#                   .../AVHRR/Output/ -> Speicherort fuer das Endergebnis
# Existierende Header Datei, diese kann irgendwo liegen



import os, shutil

# Definiere den Ordner, der die original AVHRR Daten enthaelt
# Der Ordner sollte nur diese enthalten und noch KEINE header files oder andere
inDataFol = 'D:/Test/AVHRR/Data/'

# Definiere den Speicherort der ersten header Datei
inHeaderFile = 'D:/Test/AVHRR/geo00apr15a.n14-VI3g.hdr'

# Definiere den Ordner, der das Endergebnis enthaelt (Daten mit Endung .BSQ und alle header files)
# Der Ordner sollte leer sein
outFol = 'D:/Test/AVHRR/Output/'


for fileName in os.listdir(inDataFol):
    shutil.copyfile(inDataFol + fileName, outFol + fileName + ".bsq")
    shutil.copyfile(inHeaderFile, outFol + fileName + ".hdr")

print "Kopiervorgang beendet"
