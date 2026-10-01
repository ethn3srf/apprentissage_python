Énoncé

Étant donné une liste d'entiers nombres, trouve la plus grande différence entre deux éléments consécutifs.

La différence doit être calculée en valeur absolue : elle est toujours positive.

Exemple
nombres = [4, 9, 3, 12, 8]

Résultat attendu :

9

Car la plus grande différence est entre 3 et 12 :

|3 - 12| = 9
Contraintes
2 <= len(nombres) <= 10 000
Les éléments sont des entiers.
Tu dois utiliser une boucle.
Tu ne dois pas modifier la liste.
Tu ne dois pas utiliser max().

Ma première réponse:

def plus_grand_ecart(nombres):
  nombres = [47, 12, 89, 34, 156, 23, 78, 45, 67, 190, 8, 134, 56, 31, 74, 165, 92, 14, 237, 61]
  if len(nombres) < 2:
    print("Liste trop courte")
    exit()
  elif len(nombres) > 10000:
    print("Liste trop longue.")
    exit()

  for i in range(len(nombres) - 1):
    if nombres[i] < nombres[i + 1]:
      plus_petit = i

  for x in range(len(nombres) - 1):
    if nombres[x] > nombres[x + 1]:
    plus_grand = x
  ecart_absolu = abs(plus_petit - plus_grand)

  return ecart_absolu

J'ai mal compris l'exo. On cherche l'ecart le plus grand, pas de trouver le plus petit et le plus grand puis faire l'écart. On refait

Deuxième réponse:

def plus_grand_ecart(nombres):
  nombres = [47, 12, 89, 34, 156, 23, 78, 45, 67, 190, 8, 134, 56, 31, 74, 165, 92, 14, 237, 61]
  if len(nombres) < 2:
    print("Liste trop courte")
    exit()
  elif len(nombres) > 10000:
    print("Liste trop longue.")
    exit()
    
  ecart = []
  
  for i in range(len(nombres) - 1):
    ecart.append(abs(nombres[i] - nombres[i + 1]))

  for i in range(len(ecart) - 1): 
    if ecart[i] < ecart[i + 1]: 
      plus_petit = i 
    
  for x in range(len(ecart) - 1): 
    if ecart[x] > ecart[x + 1]: 
      plus_grand = x 
      
  ecart_max = abs(plus_petit - plus_grand)
    
  return ecart_max

  ECHEC. Certaines intuitions étaient bonnes mais il y avait qlq éléments qui clochaient! Voici le code corrigé:

def plus_grand_ecart(nombres):
    nombres = [47, 12, 89, 34, 156, 23, 78, 45, 67, 190, 8, 134, 56, 31, 74, 165, 92, 14, 237, 61]

    if len(nombres) < 2:
        print("Liste trop courte")
        exit()
    elif len(nombres) > 10000:
        print("Liste trop longue.")
        exit()

    ecart = []

    for i in range(len(nombres) - 1):
        ecart.append(abs(nombres[i] - nombres[i + 1]))

    ecart_max = 0

    for i in range(len(ecart)):
        if ecart[i] > ecart_max:
            ecart_max = ecart[i]

    return ecart_max


      











