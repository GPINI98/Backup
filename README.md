# Python Backup System

Applicazione CLI sviluppata in Python per creare copie di sicurezza di file e cartelle.

## Funzionalità
- Selezione della cartella sorgente e destinazione.
- Creazione automatica della cartella di backup.
- Copia di file e sottocartelle.
- Mantenimento dei metadati dei file.
- Visualizzazione della data dell'ultimo backup.
- Gestione degli errori.

## Tecnologie
- Python 3.12
- pathlib
- shutil
- datetime
- pytest

## Avvio

```bash
python main.py
```

## Test

```bash
python -m pytest -v
```

I test verificano la copia dei file, delle sottocartelle e la gestione dei principali casi di errore.