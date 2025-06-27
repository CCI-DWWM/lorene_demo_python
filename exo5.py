# Vérification de nombres premiers :
# Écrivez une fonction en Python qui vérifie si un nombre donné est premier ou non.
# Un nombre entier naturel (supérieur ou égal à 2) est un nombre premier s('il admet exactement 2 diviseurs : 1 et lui-même.
# Exemple : 2, 3, 5, 7, 11, 13, 17, 19 … sont des nombres premiers. Il en existe une infinité)

# ALGORYTHME :
#
# demander N
# vérifier que N est un nombre
# si N<1: pas premier
# faire de 2 à N-1 (i)
#     si N divisible par
#         i: pas premier

nombre = int(input("Entrez un nombre entier positif : "))

if nombre<=1:
    print("pas premier")

for i in range (2, nombre):
    if nombre % i == 0:
        print("pas premier, divisible par ", i)
print("c'est un nombre premier")