# Demandez à l’utilisateur de saisir son PRENOM, puis son NOM, et enfin,
# son année de naissance
# Afficher « Bonjour PRENOM NOM, vous avez XX ans »
# Note : vérifier que l'année est un nombre

# mon code :

nom = input('saisissez votre prénom : ')
prenom = input('saisissez votre nom : ')
year = input('saisissez votre année de naissance : ')

e = int(year)
g = 2025-e

print('Bonjour ', prenom , nom , 'vous avez ' ,g ,'ans')

# code corrigé avec Emmanuel sans if :

prenom = input('saisissez votre prénom : ')
nom = input('saisissez votre nom : ')
year = input('saisissez votre année de naissance : ')
year = int(year) # convertion en int
age = 2025-year

print(f"Bonjour {prenom} {nom}, vous avez {age} ans")

# code corrigé avec Emmanuel AVEC if :

prenom = input('saisissez votre prénom : ')
nom = input('saisissez votre nom : ')
year = input('saisissez votre année de naissance : ')
year = int(year) # convertion en int
age = 2025-year

if year.isdigit():
    print(f"Bonjour {prenom} {nom}, vous avez {age} ans")
else:
    print("L'année n'est pas valide")