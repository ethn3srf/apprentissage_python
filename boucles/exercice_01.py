
Énoncé

Demande à l'utilisateur de saisir un nombre entier positif, puis affiche ce nombre à l'envers.

Exemples :

4582 → 2854
730 → 37
91 → 19
Contraintes
Utilise input() et int().
Utilise une boucle while.
Interdiction de convertir le nombre en chaîne de caractères avec str().
Utilise des opérations mathématiques pour extraire les chiffres.

Ma réponse:

nombre = int(input("veuillez saisir un nombre:"))

if nombre <= 1:
  print("veuillez choisir un nombre positif")
  exit()

nombre_inverse = 0

while nombre // 10 != 0:
  nombre % 10 
  nombre_inverse = nombre_inverse + nombre

print(f"{nombre} --> {nombre_inverse}")

Deuxième réponse:

nombre = int(input("veuillez saisir un nombre:"))
nombre = x

if nombre <= 1:
  print("veuillez choisir un nombre positif")
  exit()

nombre_inverse = 0

while nombre // 10 > 0:
  dernier_chiffre = nombre % 10 
  nombre_inverse = nombre_inverse * 10 + dernier_chiffre
  nombre = nombre // 10

print(f"{nombre} --> {nombre_inverse}")

Dernière réponse:

nombre = int(input("veuillez saisir un nombre:"))
x = nombre

if nombre < 0:
  print("veuillez choisir un nombre positif")
  exit()

nombre_inverse = 0

while nombre > 0:
  dernier_chiffre = nombre % 10 
  nombre_inverse = nombre_inverse * 10 + dernier_chiffre
  nombre = nombre // 10

print(f"{x} --> {nombre_inverse}")

CORRECTE

