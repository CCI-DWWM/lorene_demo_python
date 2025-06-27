# Écrivez une fonction qui compte le nombre d'occurrences de chaque élément
# dans une liste et retourne un dictionnaire avec ces comptages.

maliste = [5,5,5,6,7,2,0,0]
res = {}
for k in set(maliste):
    print(f'{k} : {maliste.count(k)}')
    res[k] = maliste.count(k)

print(res)

# ou

maliste=[5,2,4,8,65,6,8,7,1,3,9,8,5,2,2,6,54,2,4,85,4,5,54,8,5,5,1,58,8]
res = {}
for i in maliste:
    res[i] = maliste.count(i)
print(res)



# ou

listNumber = [5,5,5,6,7,2,0,0]
dictionnary = {}

for x in listNumber:
    if str(x) in dictionnary.keys():
        dictionnary[str(x)] = dictionnary[str(x)] + 1
    else:
        dictionnary[str(x)] = 1
print(dictionnary)