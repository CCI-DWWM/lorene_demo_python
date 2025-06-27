# Liste des Carrés,
# Créez une liste contenant les carrés des nombres entre 1 et 10 (inclus).

rangeNumber = range(1,11)
listResult = []

for i in rangeNumber:
    listResult.append(i * i)
print(listResult)