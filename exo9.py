# Créer une fonction est_premier(N) qui retourne True si le nombre passé est premier, False sinon

def est_premier(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


n = int(input("Entrez un nombre : "))
if est_premier(n):
    print(f"{n} est un nombre premier.")
else:
    print(f"{n} n'est pas un nombre premier.")