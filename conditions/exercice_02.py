Énoncé

Écris un programme Python qui demande à l'utilisateur de saisir un nombre entier positif.

Le programme doit déterminer si ce nombre est un nombre premier.

Un nombre premier est un entier supérieur à 1 qui possède exactement deux diviseurs : 1 et lui-même.

Exemples
Nombre : 7
7 est un nombre premier.
Nombre : 8
8 n'est pas un nombre premier.
Nombre : 1
1 n'est pas un nombre premier.
Contraintes
Utiliser input() et int() pour récupérer le nombre.
Utiliser des conditions if et else.
Ne pas utiliser de bibliothèque externe.

Ma réponse:

x = int(input("Nombre:"))

if x <= 0:
    print("Fin du programme")
    exit()
  else:
    pass
  
if only x / 1 and x / x:
    print(f"{x} est un nombre premier")
  else
    print(f"{x} n'est pas un nombre premier") 

Deuxième réponse:

x = int(input("Nombre:"))

if x <= 0:
    print("Fin du programme")
    exit()

for i in range(2, x - 1)
  if x % i != 0:
    break
    print(f"{x} n'est pas un nombre premier.")
  exit()
  else:
    continue

print(f"{x} est un nombre premier") 

Dernière réponse:

x = int(input("Nombre:"))

if x <= 1:
    print("Fin du programme")
    exit()

for i in range(2, x - 1):
  if x % i == 0:
    print(f"{x} n'est pas un nombre premier.")
    exit()
  
print(f"{x} est un nombre premier") 

CORRECTE

  






  
  
