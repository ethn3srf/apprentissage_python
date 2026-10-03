Énoncé

Écris une fonction qui reçoit une liste de nombres et un nombre cible. Elle doit retourner l'indice de la première apparition de cible.

Si cible n'est pas dans la liste, retourne -1.

Exemple
nombres = [7, 3, 9, 4, 9, 2]
cible = 9

Résultat attendu :

2

Car 9 apparaît pour la première fois à l'indice 2.

Contraintes
Utilise une liste.
Utilise une boucle.
N'utilise pas .index().
Retourne -1 si le nombre n'existe pas.

Ma réponse:

nombres = [7, 3, 9, 4, 9, 2]

def trouver_position(nombres, cible):
    for i in range(len(nombres)):
        if nombres[i] == cible:
            return i
    return -1

cible = int(input("Veuillez choisir un nombre : "))

resultat = trouver_position(nombres, cible)
print(resultat)

CORRECTE

  





  nombres = [7, 3, 9, 4, 9, 2]
  












