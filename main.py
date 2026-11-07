from pathlib import Path
from backup import esegui_backup

scelta = 0
cartella_sorgente = None
ultimo_backup = None

while scelta != 4:

    print("\n1. Seleziona cartella sorgente")
    print("2. Esegui backup")
    print("3. Visualizza informazioni ultimo backup")
    print("4. Esci")

    while True:
        try:
            scelta = int(input("Scegli un'opzione: "))

            if scelta < 1 or scelta > 4:
                print("Scelta non valida. Inserisci un numero tra 1 e 4.")
            else:
                break

        except ValueError:
            print("Devi inserire un numero valido.")

    if scelta == 1:

        percorso_sorgente = input("Inserisci percorso cartella: ").strip()
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

        percorso_destinazione = input("Inserisci il percorso di destinazione del backup: ").strip()
        cartella_destinazione = Path(percorso_destinazione)
        cartella_destinazione.mkdir(parents=True, exist_ok=True)

        try:
            ultimo_backup = esegui_backup(
                cartella_sorgente,
                cartella_destinazione
            )

            data_formattata = ultimo_backup.strftime("%d/%m/%Y alle %H:%M:%S")

            print(f"Backup completato il {data_formattata}")

        except (OSError, ValueError) as errore:
            print(f"Errore durante il backup: {errore}")

    elif scelta == 3:

        if ultimo_backup is None:
            print("Nessun backup è stato ancora effettuato")
        else:
            data_formattata = ultimo_backup.strftime("%d/%m/%Y alle %H:%M:%S")
            print(f"Ultimo backup effettuato il {data_formattata}")

