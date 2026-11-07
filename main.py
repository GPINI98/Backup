from pathlib import Path
scelta = 0


while scelta != 4:
     
    print("1. Seleziona cartella sorgente")
    print("2. Esegui backup")
    print("3. Visualizza informazioni ultimo backup")
    print("4. Esci")

    scelta = int(input("Fai la tua scelta: "))

    if scelta == 1:
        print("seleziona cartella sorgente")
        percorso = r"C:\Users\pinig\Desktop\Progetti\TEST_BACKUP"
        # percorso = input("Inserisci percorso cartella: ")
        cartella = Path(percorso)
        print(cartella.exists()) #verifica se il percorso esiste
        print(cartella.is_dir()) # verifica se è una cartella
    if scelta == 2:
        print("esegui backup")
        
    if scelta == 3:
        print("visualizza info ultimo backup")


#pathlib
# percorso = input("Inserisci percorso cartella: ")
# cartella = Path(percorso)
# 
# print(cartella.exists()) #verifica se il percorso esiste
# print(cartella.is_dir()) # verifica se è una cartella