from pathlib import Path
import shutil
from datetime import datetime


def esegui_backup(cartella_sorgente, cartella_destinazione):

    cartella_sorgente = Path(cartella_sorgente)
    cartella_destinazione = Path(cartella_destinazione)

    if not cartella_sorgente.exists():
        raise FileNotFoundError("Cartella sorgente inesistente")

    if not cartella_sorgente.is_dir():
        raise NotADirectoryError("La sorgente non è una cartella")

    sorgente = cartella_sorgente.resolve()
    destinazione = cartella_destinazione.resolve()

    if destinazione == sorgente or sorgente in destinazione.parents:
        raise ValueError("La destinazione non può essere dentro la sorgente")

    cartella_destinazione.mkdir(parents=True, exist_ok=True)

    for elemento in cartella_sorgente.iterdir():

        if elemento.is_file():
            shutil.copy2(
                elemento,
                cartella_destinazione / elemento.name
            )

        elif elemento.is_dir():
            shutil.copytree(
                elemento,
                cartella_destinazione / elemento.name,
                dirs_exist_ok=True
            )
    return datetime.now()
