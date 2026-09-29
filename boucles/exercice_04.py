Énoncé

Demande à l'utilisateur de saisir un entier positif, puis compte combien de chiffres de ce nombre sont pairs.

Exemples :

4582 → 2 chiffres pairs (4 et 8)
731 → 1 chiffre pair (2 ? Non, aucun : 7, 3 et 1 sont impairs, donc 0)
2468 → 4 chiffres pairs
1020 → 3 chiffres pairs (0, 2 et 0)
Contraintes
Utilise input() et int().
Utilise une boucle while.
Utilise % 10 pour récupérer chaque chiffre.
Utilise // 10 pour supprimer chaque chiffre.

Ma réponse:

nombre = int(input("veuillez choisir un nombre")) 
x = nombre

if nombre < 0: 
  print("veuillez choisir un nombre positif.") 
  exit()

compteur_nombre_pair = 0
compteur_nombre_impair = 0

while nombre > 0:
  test = nombre % 10
  if test % 2 == 0:
    compteur_nombre_pair =  compteur_nombre_pair + 1
  else:
    compteur_nombre_impair = compteur_nombre_impair + 1
  nombre = nombre // 10

print(f"dans le nombre {x}, il y a {compteur_nombre_pair} nombre pairs et {compteur_nombre_impair} nombre impairs")  $

ECHEC: j'ai pas pris en compte le fit que l'utilisateur peut rentrer 0.                












  
