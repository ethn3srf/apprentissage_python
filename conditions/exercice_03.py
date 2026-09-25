Énoncé

Écris un programme Python qui demande à l'utilisateur de saisir un nombre entier positif.

Le programme doit ensuite compter le nombre de chiffres qui composent ce nombre et afficher le résultat.

Exemple 1
Nombre : 4582
Ce nombre contient 4 chiffres.
Exemple 2
Nombre : 73
Ce nombre contient 2 chiffres.
Exemple 3
Nombre : 6
Ce nombre contient 1 chiffre.
Contraintes
Utiliser input() et int().
Utiliser une boucle while ou for.
Ne pas convertir le nombre en chaîne de caractères avec str() pour compter ses chiffres.

Ma réponse:

x = int(input("Nombre:"))

if x <= 1: 
  print("Fin du programme") 
  exit()

compteur = 0

while int((x / 10 ) > 1:
  compteur = compteur + 1

print(f"Nombre : {x}")
print(f"Ce nombre contient {compteur} chiffres.")

Deuxième réponse:

x = int(input("Nombre:"))

if x <= 1: 
  print("Fin du programme") 
  exit()

compteur = 0

while x // 10 > 1:
  x / 10
  compteur = compteur + 1

print(f"Nombre : {x}")
print(f"Ce nombre contient {compteur} chiffres.")

Dernière réponse : 

x = int(input("Nombre:"))
y = x 

if x <= 1: 
  print("Fin du programme") 
  exit()

compteur = 0

while x > 0:
  x = x // 10
  compteur = compteur + 1

print(f"Nombre : {y}")
print(f"Ce nombre contient {compteur} chiffres.")

Raté de peu: pour le nombre 1, c'est bien un chiffre il fallait donc mettre  if x <= 0 au début du code

















