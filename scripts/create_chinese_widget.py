from pathlib import Path

destination = Path("widgets/DailyLearning/Chinois/Chinois.ini")
destination.parent.mkdir(parents=True, exist_ok=True)

content = """[Rainmeter]
Update=1000
AccurateText=1
DynamicWindowSize=1

[Variables]
White=235,242,255,255
Blue=117,201,255,255
Muted=190,205,220,255
Gold=255,211,111,255

[Background]
Meter=Shape
Shape=Rectangle 0,0,370,500,14 | Fill Color 20,28,42,240 | StrokeWidth 1 | Stroke Color 70,95,130,180

[Title]
Meter=String
Text=CHINOIS - 中文
FontFace=Microsoft YaHei UI
FontSize=16
FontWeight=700
FontColor=#Gold#
X=20
Y=18
AntiAlias=1

[Word]
Meter=String
Text=意思
FontFace=Microsoft YaHei UI
FontSize=26
FontColor=#White#
X=20
Y=58
AntiAlias=1

[Pinyin]
Meter=String
Text=yìsi
FontFace=Segoe UI
FontSize=17
FontColor=#Blue#
X=20
Y=105
AntiAlias=1

[Meaning]
Meter=String
Text=Signification, intérêt, intention
FontFace=Segoe UI
FontSize=11
FontColor=#Muted#
X=20
Y=143
AntiAlias=1

[Examples]
Meter=String
Text=这是什么意思？#CRLF#Zhè shì shénme yìsi?#CRLF#Qu'est-ce que ça signifie ?#CRLF##CRLF#这个电影很有意思。#CRLF#Zhège diànyǐng hěn yǒu yìsi.#CRLF#Ce film est très intéressant.
FontFace=Microsoft YaHei UI
FontSize=12
FontColor=#White#
X=20
Y=195
W=330
H=185
ClipString=2
AntiAlias=1

[ExpressionTitle]
Meter=String
Text=EXPRESSION : 摸鱼 - mō yú
FontFace=Microsoft YaHei UI
FontSize=12
FontWeight=700
FontColor=#Gold#
X=20
Y=390
AntiAlias=1

[ExpressionText]
Meter=String
Text=我今天在公司摸鱼。#CRLF#Wǒ jīntiān zài gōngsī mōyú.#CRLF#Aujourd'hui, je glande au bureau.
FontFace=Microsoft YaHei UI
FontSize=11
FontColor=#White#
X=20
Y=425
W=330
H=65
ClipString=2
AntiAlias=1
"""

destination.write_bytes(content.encode("utf-16"))
print(f"Widget créé : {destination}")
