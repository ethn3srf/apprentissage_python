Énoncé

Écris une fonction qui reçoit une liste de nombres et retourne le deuxième plus grand nombre de la liste.

Exemple
nombres = [8, 3, 15, 6, 12, 20, 5]

Résultat attendu :

15
Contraintes
Utilise une liste.
Utilise une boucle.
Ne modifie pas la liste originale.
N'utilise pas sort() ni sorted().

Ma réponse:

def deuxieme_plus_grand(nombres):
    plus_grand = 0
    deuxieme = 0

    for i in range(len(nombres)):
        if nombres[i] > plus_grand:
            deuxieme = plus_grand
            plus_grand = nombres[i]
        elif nombres[i] > deuxieme:
            deuxieme = nombres[i]
    return deuxieme


nombres = [8, 3, 15, 6, 12, 20, 5]

resultat = deuxieme_plus_grand(nombres)

print(resultat)

CORRECTE
      
      
  














