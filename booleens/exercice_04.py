Énoncé

Écris une fonction qui reçoit deux listes et retourne True si elles contiennent exactement les mêmes éléments dans le même ordre, sinon False.

Exemple
liste1 = [4, 7, 2, 9]
liste2 = [4, 7, 2, 9]

Résultat :

True
Contraintes
Utilise une boucle.
Retourne uniquement True ou False.
N'utilise pas directement liste1 == liste2.

Ma réponse:

def listes_identiques(liste1, liste2):
    if len(liste1) != len(liste2):
      return False

    for i in range(len(liste1)):
      if element(liste1) != element(liste2):
        return False

    Return True

    Deuxième essai:

  def listes_identiques(liste1, liste2):
    if len(liste1) != len(liste2):
      return False

    for i in range(len(liste1)):
      if liste1[i] != liste2[i]:
        return False

    return True

    CORRECTE
    








