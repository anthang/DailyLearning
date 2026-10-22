import subprocess
import sys
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def charger_contenus(categorie):
    fichier = ROOT / "data" / f"{categorie}.json"

    with fichier.open("r", encoding="utf-8") as f:
        contenus = json.load(f)

    if not contenus:
        raise ValueError(f"Aucun contenu dans {fichier}")

    return contenus


def choisir_contenu_quotidien(categorie):
    contenus = charger_contenus(categorie)

    jour = date.today().toordinal()
    index = jour % len(contenus)

    return contenus[index]




def generer_module(categorie, variable):
    information = choisir_contenu_quotidien(categorie)

    if categorie == "histoire":
        texte = f"{information['date']} : {information['texte']}"
    else:
        texte = information["texte"]

    destination = (
        ROOT / "widgets" / "DailyLearning"
        / "@Resources" / f"{categorie}.inc"
    )
    destination.parent.mkdir(parents=True, exist_ok=True)

    contenu = chr(10).join([
        "[Variables]",
        f"{variable}={texte}",
        ""
    ])

    destination.write_bytes(contenu.encode("utf-16"))

    print(f"{categorie} : {texte}")
    print(f"Fichier généré : {destination}")


if __name__ == "__main__":
    generer_module("histoire", "HistoryText")
    generer_module("geographie", "GeoText")
    generer_module("culture", "CultureText")
    subprocess.run([sys.executable, str(ROOT / "scripts/generate_english.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/generate_chinese.py")], check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/generate_cyber.py")], check=True)
