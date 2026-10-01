Énoncé

Étant donné une liste d'entiers nombres, compte le nombre de fois où un élément est strictement supérieur à l'élément qui le précède.

Exemple unique
nombres = [4, 7, 3, 5, 8, 2]

Résultat attendu :

3

Explication : 7 > 4, 5 > 3 et 8 > 5.

Contraintes

1 <= len(nombres) <= 10 000

Les éléments sont des entiers compris entre -10**9 et 10**9.

Tu dois utiliser une boucle.

Tu ne dois pas modifier la liste.

Si la liste contient un seul élément, le résultat est 0.

Ma réponse:

nombres = [6, 9, 0, 8, 5, 6, 7, 4, 67, 6, 87, 09, 56, 67, 433, 8907, 890756, 6, 78, 908, 9007, 34567894, 4, 456, 21, 2, 2, 2, 1, 1, 9]

compteur = 0
def compter_montee(nombres):
  for i in range(len(nombres)):
    if len(nombres) < 1:
      print("Liste trop courte")
      exit()
    elif len(nombres) > 10000:
      print("Liste trop longue.")
      exit()

      if nombres[i] > nombres[i - 1]:
        compteur = compteur + 1

print(f" Le résultat est {compteur})

Deuxième réponse :

nombres = [6, 9, 0, 8, 5, 6, 7, 4, 67, 6, 87, 09, 56, 67, 433, 8907, 890756, 6, 78, 908, 9007, 34567894, 4, 456, 21, 2, 2, 2, 1, 1, 9]

def compter_montee(nombres):
  compteur = 0
  if len(nombres) < 1:
    print("Liste trop courte")
    exit()
  elif len(nombres) > 10000:
    print("Liste trop longue.")
    exit()
  for i in range(len(nombres)):
    if nombres[i + 1] > nombres[i]:
        compteur = compteur + 1

  return compteur

  Dernière réponse:

nombres = [6, 9, 0, 8, 5, 6, 7, 4, 67, 6, 87, 09, 56, 67, 433, 8907, 890756, 6, 78, 908, 9007, 34567894, 4, 456, 21, 2, 2, 2, 1, 1, 9]

def compter_montee(nombres):
  compteur = 0
  if len(nombres) < 1:
    print("Liste trop courte")
    exit()
  elif len(nombres) > 10000:
    print("Liste trop longue.")
    exit()
  for i in range(len(nombres) - 1):
    if nombres[i + 1] > nombres[i]:
        compteur = compteur + 1
  return compteur

  CORRECTE
        
