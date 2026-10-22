import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

source = ROOT / "data/chinois.json"
destination = ROOT / "widgets/DailyLearning/@Resources/chinois.inc"

with source.open(encoding="utf-8") as f:
    fiches = json.load(f)

if not fiches:
    raise ValueError("La bibliothèque chinoise est vide.")

fiche = fiches[date.today().toordinal() % len(fiches)]

if len(fiche["exemples"]) < 2:
    raise ValueError("La fiche doit contenir au moins deux exemples.")

variables = {
    "ChineseWord": fiche["mot"],
    "ChinesePinyin": fiche["pinyin"],
    "ChineseMeaning": fiche["signification"],
}

for numero, exemple in enumerate(fiche["exemples"][:2], start=1):
    variables[f"ChineseExample{numero}"] = exemple["chinois"]
    variables[f"ChineseExamplePinyin{numero}"] = exemple["pinyin"]
    variables[f"ChineseExampleFrench{numero}"] = exemple["francais"]

expression = fiche["expression"]

variables.update({
    "ChineseExpression": expression["chinois"],
    "ChineseExpressionPinyin": expression["pinyin"],
    "ChineseExpressionMeaning": expression["signification"],
    "ChineseExpressionExample": expression["exemple"],
    "ChineseExpressionExamplePinyin": expression["exemple_pinyin"],
    "ChineseExpressionFrench": expression["francais"],
})

lignes = ["[Variables]"]

for cle, valeur in variables.items():
    valeur = str(valeur).replace("\r", " ").replace("\n", " ")
    lignes.append(f"{cle}={valeur}")

destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_bytes(
    ("\n".join(lignes) + "\n").encode("utf-16")
)

print("Fichier chinois.inc généré.")
print("Mot sélectionné :", fiche["mot"])
print("Pinyin :", fiche["pinyin"])
print("Nombre de variables :", len(variables))
