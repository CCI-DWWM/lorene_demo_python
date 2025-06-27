# commentaire mono ligne


"""
commentaire sur plusieurs lignes
la suite du commentaire...
bla bla bla
bla bla
"""

# exemple de code
print('tjs OK')

# exemple de code
x = """
ffdsf
fdsf
dsfsdfcv
cdsf"""

print(x)

# exemple de code
a = input('donner une valeur')
print('tjs OK, vous avez donné : ', a)


# exemple de code
# x=100
#
# if x==10:
#     print('X vaut 10')
# else:
#     print('X est différent de 10')
#
# print('suite...')


l1 = [1, 2, 4, 8]

for x in l1:
    print(f"- {x=}")
    # ou sans le nom de la variable
    # print(f"- {x}")

print('-----------------')

l2 = "Hello World"
for x in l2:
    print(f"- {x=}")

print('-----------------')

l3 = range(5, 10)
for x in l3:
    print(f"- {x=}")

print('-----------------')
#avec incrémentation : range(START, STOP, INCREMENT)
l4 = range(5, 10, 2)
for x in l4:
    print(f"- {x=}")

print('-----------------')

l5 = "Hello World"
for x in l5:
    print(f"- {x=}")
    if x==',':
        break

print('-----------------')


l6 = range(2, 101, 2)
for x in l6:
    if x==50:
        break
    print(f"{x=}")
else:
    print('cas ELSE')

# if / else écrit sur une ligne :
x = "positif" if x>0 else "negatif"

# code sur 1 ligne
maliste = [i for i in range(1, 11)]

#équivalent au code ci-dessus mais en plusieurs lignes
maliste = []
for i in range(1, 11):
    maliste.append(i)