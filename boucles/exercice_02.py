Énoncé

Demande à l'utilisateur de saisir un nombre entier positif, puis indique si ce nombre est un palindrome.

Exemples :

121 → C'est un palindrome.
1331 → C'est un palindrome.
1234 → Ce n'est pas un palindrome.
7 → C'est un palindrome.
Contraintes
Utilise input() et int().
Utilise une boucle while.
N'utilise pas str() pour convertir le nombre en chaîne de caractères.
Utilise les opérations % 10 et // 10.

Première réponse:

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
  
  if nombre_inverse == x:
      print(f"{x} est un palindrome")
  else:
    print(f"{x} n'est pas un palindrome")

deuxième réponse (il faut corriger l'indentation):

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
  
if nombre_inverse == x:
    print(f"{x} est un palindrome")
else:
  print(f"{x} n'est pas un palindrome")
  



