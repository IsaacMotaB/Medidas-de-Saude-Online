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
  <link href="../style.css" type="text/css" rel="stylesheet">
  <title>Circumferência abdominal</title>  
</head>""")

try:
  sexo = form.getvalue("sexo")
  circumferencia = float(form.getvalue("circumferencia"))
  if sexo == "Feminino":
    if circumferencia <= 80:
      cardiopatia = ("normal")
    elif circumferencia < 84:
      cardiopatia = ("médio")
    elif circumferencia < 88:
      cardiopatia = ("alto")
    else:
      cardiopatia = ("altíssimo")
  elif sexo == "Masculino":
    if circumferencia <= 90:
      cardiopatia = ("normal")
    elif circumferencia < 94:
      cardiopatia = ("médio")
    elif circumferencia < 102:
      cardiopatia = ("alto")
    else:
      cardiopatia = ("altíssimo")
  print(
    f"<h1>Risco de cardiopatia: {cardiopatia}</h1>"
  )
except Exception:
  circumferencia = ''

print(f"""\
{menu.navbar()}
<h1>Digite as seus dados para calcular risco de cardiopatia</h1>
<form>
    Circumferencia Abdominal: <input type="text" name="circumferencia" value="{circumferencia}"> cm<br>
    Sexo: <select name="sexo" id="sexo">
        <option value="Masculino" {"selected" if sexo == "Masculino" else ""}>Masculino</option>
        <option value="Feminino" {"selected" if sexo == "Feminino" else ""}>Feminino</option>
    </select><br>
    <input type="submit" value="Enviar">
</form>""")