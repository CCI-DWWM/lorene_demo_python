# Puis compte et affiche le nombre de voyelles (a, e, i, o, u, y) et consonnes dans la phrase.
# Écrivez un programme qui demande à l'utilisateur de saisir une phrase

# ALGORYTHME :
# demander phrase
# 2 accumulateurs
# consonne = 0
# voyelle = 0
# pour chaque lettre :
#     si consonne: consonne+=1
#     si voyelle: voyelle+=1

voyelles="aeiouy"
phrase = input("Saisir une phrase : ").lower() # Passe en minuscules les lettres

NbrVoyelles=0
NbrConsonnes=0
NbrAutres=0

for letter in phrase:
    if letter in voyelles:
        NbrVoyelles += 1
    elif (letter>='a') and (letter<='z'): #letter in alpha:
        NbrConsonnes += 1
    else:
        NbrAutres += 1

print(f'il y a {NbrConsonnes} consonnes, {NbrVoyelles} voyelles, {NbrAutres} autres')


# autre possibilités :

list = ['a', 'e', 'i', 'o', 'u','y']
listCons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']

sentence = input('phrase : ')
lowSentence = sentence.lower()
x = 0
y = 0
for i in lowSentence:
    if i in list:
        x += 1
    if i in listCons:
        y +=1
print(f"Il y a : {x} voyelle et {y} consonnes")