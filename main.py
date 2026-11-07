from pathlib import Path
import shutil
from datetime import datetime
scelta = 0

cartella_sorgente = None

while scelta != 4:
     
    print("1. Seleziona cartella sorgente")
    print("2. Esegui backup")
    print("3. Visualizza informazioni ultimo backup")
    print("4. Esci")

    scelta = int(input("Fai la tua scelta: "))
    # cartella_sorgente = None
    # cartella_destinazione = None

    if scelta == 1:
        print("seleziona cartella sorgente")
        percorso_sorgente = r"C:\Users\pinig\Desktop\Progetti\TEST_BACKUP"
        # percorso = input("Inserisci percorso cartella: ")
        cartella_sorgente = Path(percorso_sorgente)
        if cartella_sorgente.exists() and cartella_sorgente.is_dir():
            print("Cartella sorgente valida")
        else:
            cartella_sorgente = None
            print("Percorso non valido")
    if scelta == 2:
        if cartella_sorgente is None:
            print("Devi prima selezionare una cartella sorgente")
            continue # interrompe l'iterazione e riporta il programma all'inizio

        percorso_destinazione = r"C:\Users\pinig\Desktop\Progetti\TEST_BACKUP_IN"
        cartella_destinazione = Path(percorso_destinazione)
        cartella_destinazione.mkdir(exist_ok=True)

        for elemento in cartella_sorgente.iterdir():
            if elemento.is_file():
                shutil.copy2(cartella_sorgente/elemento.name, cartella_destinazione/elemento.name)
            elif elemento.is_dir():
                shutil.copytree(cartella_sorgente/elemento.name, cartella_destinazione/elemento.name)

        
    if scelta == 3:
        print("visualizza info ultimo backup")
