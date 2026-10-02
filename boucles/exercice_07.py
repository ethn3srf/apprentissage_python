Énoncé

Étant donné une liste d'entiers nombres, trouve le premier nombre qui apparaît au moins deux fois dans la liste.

Tu dois parcourir la liste dans l'ordre.

Si aucun nombre n'apparaît deux fois, retourne -1.

Exemple
nombres = [4, 7, 2, 9, 5, 2, 8, 7]

Résultat attendu :

2

Car 2 est le premier nombre rencontré qui apparaît une deuxième fois.

Contraintes
Les éléments sont des entiers.
Tu dois utiliser une boucle.
Tu ne dois pas modifier nombres.
Si aucun doublon n'existe, retourne -1

Ma réponse:

def premier_doublon(nombres):
  nombres = [8, 14, 3, 27, 6, 19, 42, 11, 5, 31, 14, 9, 22, 3, 17]
  deja_vus = []

  for nombre in nombres:
    if nombre in deja_vus:
      exit()
      return nombre
    else:
      deja_vus.append(nombre)
      return "-1"

deuxième réponse:

def premier_doublon(nombres):
  nombres = [8, 14, 3, 27, 6, 19, 42, 11, 5, 31, 14, 9, 22, 3, 17]
  deja_vus = []

  for nombre in nombres:
    if nombre in deja_vus:
      return nombre
    else:
      deja_vus.append(nombre)

  return "-1"

CORRECTE
























