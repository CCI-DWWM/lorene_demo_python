# Écrivez un programme qui demande à l'utilisateur un nombre entier positif et calcule sa factorielle.
# La factorielle de n (notée n!) est le produit de tous les entiers de 1 à n.
# Par exemple, 5! = 5 × 4 × 3 × 2 × 1 = 120.

n = int(input("Entrez un nombre entier positif : "))
r = 1

for n in range(1, n+1):
    r = r * n
    print(r)

# Explication du code ci-dessus :
# iteration 1 : R <- 1 x 1 = 1
# iteration 2 : R <- 1 x 2 = 2
# iteration 3 : R <- 2 x 3 = 6
# iteration 4 : R <- 6 x 4 = 24
# iteration 5 : R <- 24 x 5 = 120