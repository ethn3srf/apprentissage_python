Énoncé

Demande à l'utilisateur de saisir un nombre entier positif, puis calcule la somme de tous ses chiffres.

Exemples :

4582 → 4 + 5 + 8 + 2 = 19
731 → 7 + 3 + 1 = 11
9005 → 9 + 0 + 0 + 5 = 14
Contraintes
Utilise input() et int().
Utilise une boucle while.
N'utilise pas str() pour convertir le nombre en chaîne de caractères.
Utilise % 10 pour récupérer le dernier chiffre.
Utilise // 10 pour supprimer le dernier chiffre.

Ma réponse:

nombre = int(input("veuillez choisir un nombre"))

if nombre < 0:
  print("veuillez choisir un nombre positif.")
  exit()

compteur = 0             

while nombre > 0:
  chiffre_récupéré = nombre % 10
  compteur = compteur + chiffre_récupéré
  nombre = nombre // 10

print(compteur) 

CORRECTE











             
