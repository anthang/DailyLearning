import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

source = ROOT / "data/anglais.json"
destination = ROOT / "widgets/DailyLearning/@Resources/anglais.inc"

with source.open(encoding="utf-8") as f:
    mots = json.load(f)

if not mots:
    raise ValueError("La bibliothèque anglaise est vide.")

mot = mots[date.today().toordinal() % len(mots)]

if len(mot["sens"]) < 3:
    raise ValueError("Le mot doit avoir au moins trois significations.")

variables = {
    "EnglishWord": mot["mot"],
    "EnglishType": mot["type"],
    "EnglishExpression": mot["expression"]["texte"],
    "EnglishExpressionMeaning": mot["expression"]["signification"],
    "EnglishExpressionExample": mot["expression"]["exemple"],
    "EnglishExpressionFrench": mot["expression"]["francais"]
}

for i, sens in enumerate(mot["sens"][:3], start=1):
    variables[f"EnglishMeaning{i}"] = sens["traduction"]
    variables[f"EnglishExample{i}"] = sens["exemple"]
    variables[f"EnglishFrench{i}"] = sens["francais"]

lignes = ["[Variables]"]

for cle, valeur in variables.items():
    valeur = str(valeur).replace("\r", " ").replace("\n", " ")
    lignes.append(f"{cle}={valeur}")

destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_bytes(
    ("\n".join(lignes) + "\n").encode("utf-16")
)

print("Fichier anglais.inc généré.")
print("Mot sélectionné :", mot["mot"])
print("Nombre de variables :", len(variables))
