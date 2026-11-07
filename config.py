# from pathlib import Path
# import shutil
# from datetime import datetime
# import os

#pathlib
# percorso = input("Inserisci percorso cartella: ")
# cartella = Path(percorso)
# 
# print(cartella.exists()) #verifica se il percorso esiste
# print(cartella.is_dir()) # verifica se è una cartella

#shutil

# shutil.copy("documeto.txt", "backup/documento.txt") #copia un file
# shutil.copytree("documeti", "backup/documenti") #copia una cartella
# shutil.copytree("documeti", "backup/documenti", dirs_exist_ok=True) #copia cartella aggiornando quella corrente 

#datetime
# ora = datetime.now()
# print(ora) 
# data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# print(data)

# #os

# import os

# os.listdir("documenti")       # Elenca i contenuti
# os.path.getsize("file.txt")   # Dimensione del file
# os.path.isfile("file.txt")   # Verifica se è un file
# os.path.isdir("documenti")   # Verifica se è una cartella