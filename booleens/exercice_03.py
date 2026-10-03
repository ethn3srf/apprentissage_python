Énoncé

Écris une fonction qui reçoit un nombre et retourne :

True s'il est premier
False sinon

Un nombre premier est un nombre entier supérieur à 1 qui n'a que deux diviseurs : 1 et lui-même.

Exemple
nombre = 7

Résultat :

True
Contraintes
Utilise une boucle.
Utilise une condition.
La fonction doit retourner True ou False.
N'utilise pas de bibliothèque.

Ma réponse:

def est_premier(nombre):
  if nombre <= 1:
    return False
  for i in range(2, nombre):
    if nombre % i == 0:
      return False
  return True

CORRECTE
