Énoncé

Écris une fonction qui reçoit un mot et retourne True si le mot se lit de la même façon dans les deux sens, sinon False.

Exemple
mot = "radar"

Résultat attendu :

True
Contraintes
Utilise une boucle.
N'utilise pas [::-1].
N'utilise pas reversed().

Ma réponse:

def est_palindrome(mot):
    for i in range(len(mot)):
      if mot[i] != mot[-i - 1]:
        return False
    return True

CORRECTE



              









