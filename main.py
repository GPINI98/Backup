from pathlib import Path
import shutil
from datetime import datetime
scelta = 0

cartella_sorgente = None
ultimo_backup = None

while scelta != 4:
     
    print("1. Seleziona cartella sorgente")
    print("2. Esegui backup")
    print("3. Visualizza informazioni ultimo backup")
    print("4. Esci")

    scelta = int(input("Fai la tua scelta: "))

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
    elif scelta == 2:
        if cartella_sorgente is None:
            print("Devi prima selezionare una cartella sorgente")
            continue # interrompe l'iterazione e riporta il programma all'inizio

        percorso_destinazione = r"C:\Users\pinig\Desktop\Progetti\TEST_BACKUP_IN"
        cartella_destinazione = Path(percorso_destinazione)
        cartella_destinazione.mkdir(exist_ok=True)

        for elemento in cartella_sorgente.iterdir():
            if elemento.is_file():
                shutil.copy2(elemento, cartella_destinazione/elemento.name)
            elif elemento.is_dir():
                shutil.copytree(elemento, cartella_destinazione/elemento.name, dirs_exist_ok=True)

        ultimo_backup = ora_backup = datetime.now()
        data_formattata = ora_backup.strftime("%d/%m/%Y alle %H:%M:%S")
        print(f"Backup completato il {data_formattata}")
        
    elif scelta == 3:
        if ultimo_backup is None:
            print("Nessun backup è stato ancora effettuato")
        else:
            data_formattata = ultimo_backup.strftime("%d/%m/%Y alle %H:%M:%S")
            print(f"Ultimo backup effettuato il {data_formattata}")