#!/usr/bin/env python

import cgitb
import cgi
import menu

form = cgi.FieldStorage()
cgitb.enable(display=0, logdir="./")

print("""\
Content-type:text/html\n\n
<head>
    <meta charset="UTF-8">
    <title>Índice de massa corpórea</title>
    <link href="../style.css" type="text/css" rel="stylesheet">
</head>""")

try:
  peso = float(form.getvalue("peso"))
except:
  peso = ''

try:
  altura = float(form.getvalue("altura"))
except:
  altura = ''

if peso and altura:
  IMC = peso / altura**2
  print(f"<h1>Seu IMC é {IMC:.1f} kg/m²</h1>")

print(f"""\
{menu.navbar()}
<h1>Digite as suas medidas para calcular IMC</h1>
<form action="./IMC.py" >
    Peso: <input type="text" name="peso" value="{peso}"><br>
    Altura: <input type="text" name="altura" value="{altura}"><br>
    <input type="submit" value="Enviar">
</form>""")
