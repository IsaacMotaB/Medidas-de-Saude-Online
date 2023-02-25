#!/usr/bin/env python

import cgitb
import cgi
import menu

form = cgi.FieldStorage()
cgitb.enable(display=0, logdir="./")
"""Agua = kilograma * 35 ml"""

print("""\
Content-type:text/html\n\n
<head>
  <meta charset="UTF-8">
  <link href="../style.css" type="text/css" rel="stylesheet">
  <title>Hidratação</title>
</head>""")

try:
  peso = float(form.getvalue("peso"))
  ConsumoAgua = peso * 35
  print(f"<h1>Consumo de água recomendado: {ConsumoAgua} ml</h1>")
except Exception:
  peso = ''

print(f"""\
{menu.navbar()}
<h1>Digite o seu peso para calcular o consumo indicado de água</h1>
<form>
    Peso: <input type="text" name="peso" value="{peso}"> kg<br>
    <input type="submit" value="Enviar">
</form>
""")
