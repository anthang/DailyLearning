from pathlib import Path

destination = Path("widgets/DailyLearning/Anglais/Anglais.ini")
destination.parent.mkdir(parents=True, exist_ok=True)

content = """[Rainmeter]
Update=1000
AccurateText=1
DynamicWindowSize=1

[Variables]
FontName=Segoe UI
White=235,242,255,255
Muted=165,185,210,255

[Background]
Meter=Shape
Shape=Rectangle 0,0,370,530,14 | Fill Color 20,28,42,240 | StrokeWidth 1 | Stroke Color 70,95,130,180

[Title]
Meter=String
Text=ANGLAIS
X=20
Y=18
FontFace=#FontName#
FontSize=16
FontWeight=700
FontColor=255,149,149,255
AntiAlias=1

[Word]
Meter=String
Text=Get
X=20
Y=58
FontFace=#FontName#
FontSize=25
FontWeight=700
FontColor=#White#
AntiAlias=1

[Description]
Meter=String
Text=Verbe - Plusieurs significations
X=20
Y=105
FontFace=#FontName#
FontSize=10
FontColor=#Muted#
AntiAlias=1

[Examples]
Meter=String
Text=1. OBTENIR#CRLF#I got a new job.#CRLF#J'ai obtenu un nouvel emploi.#CRLF##CRLF#2. COMPRENDRE#CRLF#I get it!#CRLF#J'ai compris !#CRLF##CRLF#3. DEVENIR#CRLF#It's getting cold.#CRLF#Il commence à faire froid.
X=20
Y=145
W=330
H=250
FontFace=#FontName#
FontSize=12
FontColor=#White#
ClipString=2
AntiAlias=1

[ExpressionTitle]
Meter=String
Text=EXPRESSION : I'm down!
X=20
Y=415
W=330
FontFace=#FontName#
FontSize=12
FontWeight=700
FontColor=255,207,112,255
AntiAlias=1

[ExpressionText]
Meter=String
Text=We're going out. Are you down?#CRLF#On sort. Ça te dit ?
X=20
Y=450
W=330
H=60
FontFace=#FontName#
FontSize=11
FontColor=#White#
ClipString=2
AntiAlias=1
"""

destination.write_bytes(content.encode("utf-16"))

print(f"Widget créé : {destination}")
