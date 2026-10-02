Énoncé

Écris une fonction qui reçoit une liste de nombres et retourne combien de nombres sont strictement supérieurs à la moyenne de la liste.

Exemple
nombres = [4, 8, 10, 6, 2]

La moyenne est 6.

Résultat attendu :

2

(car 8 et 10 sont supérieurs à 6)

Contraintes
Utilise une liste.
Utilise des boucles.
N'utilise pas sum().
N'utilise pas statistics.*

Ma réponse:

nombres = [4, 8, 10, 6, 2]
def compter_superieurs_moyenne(nombres):
  somme = 0
  compteur_nombre_sup_moyenne = 0
  for element in nombres:
    somme = somme + element

  moyenne = somme / len(nombres)

  for i in range(len(nombres)):
    if nombres[i] > moyenne:
      compteur_nombre_sup_moyenne = compteur_nombre_sup_moyenne + 1

  return compteur_nombre_sup_moyenne

resultat = compter_superieurs_moyenne(nombres)
print(resultat)

CORRECTE
    
      











  
