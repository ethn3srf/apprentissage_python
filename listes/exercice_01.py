Énoncé

Étant donné une liste d'entiers nombres, crée une nouvelle liste contenant chaque nombre une seule fois, en conservant l'ordre de première apparition.

Exemple
nombres = [4, 7, 4, 2, 7, 9, 2, 5]

Résultat attendu :

[4, 7, 2, 9, 5]
Contraintes
Les éléments sont des entiers.
Tu dois utiliser une boucle.
Tu ne dois pas modifier la liste nombres.
N'utilise pas set().

Ma réponse

def supprimer_doublons(nombres):
  liste = []
  
  for element in nombres:
    if not element in liste:
      liste.append(element)

  return liste

nombres = [4, 7, 4, 2, 7, 9, 2, 5]

resultat = supprimer_doublons(nombres)

print(resultat)

CORRECTE
    
    













