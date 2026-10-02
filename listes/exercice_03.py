Énoncé

Écris une fonction qui reçoit deux listes de nombres et crée une nouvelle liste contenant tous les éléments des deux listes.

Les éléments de la première liste doivent rester dans leur ordre, puis ceux de la deuxième liste.

Exemple
liste1 = [4, 7, 2]
liste2 = [9, 1, 6]

Résultat attendu :

[4, 7, 2, 9, 1, 6]
Contraintes
Utilise des listes.
Crée une nouvelle liste.
N'utilise pas extend().
N'utilise pas +.

Ma réponse:

liste1 = [4, 7, 2]
liste2 = [9, 1, 6]

def fusionner_listes(liste1, liste2):
  fusionner_liste = []

  for element in liste1:
    fusionner_liste.append(element)

  for x in liste2:
    fusionner_liste.append(x)

  return fusionner_liste

resultat = fusionner_listes(liste1, liste2)
print(resultat)

CORRECTE
      








