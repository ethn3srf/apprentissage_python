Énoncé:

Écris un programme Python qui demande à l'utilisateur de saisir trois nombres entiers.

Le programme doit ensuite identifier et afficher le plus grand des trois nombres.

Exemple d'exécution
Premier nombre : 12
Deuxième nombre : 7
Troisième nombre : 19

Le plus grand nombre est 19.
Contraintes
Utiliser input() pour récupérer les trois nombres.
Utiliser int() pour convertir les entrées en nombres entiers.
Utiliser if, elif et else pour comparer les nombres.
Ne pas utiliser la fonction max()

Ma réponse:

int(input("affichez 3 nombres"))

if premier_nombre >= deuxième_nombre and premier_nombre >= troisième_nombre:
  print(f"Le plus grand nombre est {premier_nombre}.")
elif deuxième_nombre >= premier_nombre and deuxième_nombre >= troisième_nombre
  print(f"Le plus grand nombre est {deuxième_nombre}.")
else 
  print(f"Le plus grand nombre est {troisième_nombre}.")

Deuxième essai avec aide de ChatGPT

premier_nombre = int(input("Premier nombre:"))
deuxième_nombre = int(input("Deuxième nombre:"))
troisième_nombre = int(input("Troisième nombre:"))

if premier_nombre >= deuxième_nombre and premier_nombre >= troisième_nombre:
  print(f"Le plus grand nombre est {premier_nombre}.")
elif deuxième_nombre >= premier_nombre and deuxième_nombre >= troisième_nombre:
  print(f"Le plus grand nombre est {deuxième_nombre}.")
else:
  print(f"Le plus grand nombre est {troisième_nombre}.")

CORRECTE


       






