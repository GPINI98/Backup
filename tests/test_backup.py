import pytest
from backup import esegui_backup

def test_copia_file(tmp_path):
    sorgente = tmp_path / "sorgente"
    destinazione = tmp_path / "backup"

    sorgente.mkdir()

    file_originale = sorgente / "documento.txt"
    file_originale.write_text("Test backup", encoding="utf-8")

    esegui_backup(sorgente, destinazione)

    file_copiato = destinazione / "documento.txt"

    assert file_copiato.exists()
    assert file_copiato.read_text(encoding="utf-8") == "Test backup"


def test_copia_sottocartelle(tmp_path):
    sorgente = tmp_path / "sorgente"
    destinazione = tmp_path / "backup"

    sottocartella = sorgente / "documenti"
    sottocartella.mkdir(parents=True)

    file_originale = sottocartella / "fattura.txt"
    file_originale.write_text("Fattura", encoding="utf-8")

    esegui_backup(sorgente, destinazione)

    file_copiato = destinazione / "documenti" / "fattura.txt"

    assert file_copiato.exists()
    assert file_copiato.read_text(encoding="utf-8") == "Fattura"


def test_sorgente_inesistente(tmp_path):
    sorgente = tmp_path / "inesistente"
    destinazione = tmp_path / "backup"

    with pytest.raises(FileNotFoundError):
        esegui_backup(sorgente, destinazione)


def test_destinazione_dentro_sorgente(tmp_path):
    sorgente = tmp_path / "sorgente"
    destinazione = sorgente / "backup"

    sorgente.mkdir()

    with pytest.raises(ValueError):
        esegui_backup(sorgente, destinazione)


def test_backup_ripetuto(tmp_path):
    sorgente = tmp_path / "sorgente"
    destinazione = tmp_path / "backup"

    sorgente.mkdir()

    file_originale = sorgente / "documento.txt"
    file_originale.write_text("Prima versione", encoding="utf-8")

    esegui_backup(sorgente, destinazione)

    file_originale.write_text("Seconda versione", encoding="utf-8")

    esegui_backup(sorgente, destinazione)

    file_copiato = destinazione / "documento.txt"

    assert file_copiato.read_text(encoding="utf-8") == "Seconda versione"
