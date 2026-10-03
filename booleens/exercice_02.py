Énoncé

Écris une fonction qui reçoit une liste de nombres et retourne True si les nombres sont dans l'ordre croissant ou égal, sinon False.

Exemple
nombres = [2, 4, 4, 7, 10]

Résultat :

True
Contraintes
Utilise une boucle.
Ne modifie pas la liste.
N'utilise pas sort() ou sorted().

Ma réponse:

def est_triee(nombres):
  for i in range(len(nombres) - 1):
    if nombres[i] > nombres[i + 1]:
      return False
    else:
      return True

Deuxième essai:

def est_triee(nombres):
  for i in range(len(nombres) - 1):
    if nombres[i] > nombres[i + 1]:
      return False
   return True

CORRECTE






















