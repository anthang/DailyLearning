import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

source = ROOT / "data/cyber.json"
destination = ROOT / "widgets/DailyLearning/@Resources/cyber.inc"

with source.open(encoding="utf-8") as f:
    fiches = json.load(f)

if not fiches:
    raise ValueError("La bibliothèque cybersécurité est vide.")

fiche = fiches[date.today().toordinal() % len(fiches)]

types = {
    "reflexion": "RÉFLEXION CYBER",
    "actualite": "ACTUALITÉ CYBER",
    "outil": "OUTIL CYBER",
}

type_contenu = fiche["type"]

if type_contenu not in types:
    raise ValueError(f"Type inconnu : {type_contenu}")

outil = fiche.get("outil", {})

variables = {
    "CyberType": types[type_contenu],
    "CyberTitle": fiche["titre"],
    "CyberExplanation": fiche["explication"],
    "CyberTakeaway": fiche["a_retenir"],
    "CyberPrecision": fiche["precision"],
    "CyberToolName": outil.get("nom", ""),
    "CyberToolDescription": outil.get("description", ""),
    "CyberSource": fiche.get("source", ""),
    "CyberDate": fiche.get("date_actualite", ""),
}

lignes = ["[Variables]"]

for cle, valeur in variables.items():
    valeur = str(valeur).replace("\r", " ").replace("\n", " ")
    lignes.append(f"{cle}={valeur}")

destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_bytes(
    ("\n".join(lignes) + "\n").encode("utf-16")
)

print("Fichier cyber.inc généré.")
print("Type :", variables["CyberType"])
print("Sujet :", variables["CyberTitle"])
print("Outil :", variables["CyberToolName"])
print("Nombre de variables :", len(variables))
