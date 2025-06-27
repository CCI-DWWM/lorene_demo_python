# Lecture CSV
import csv
import sqlite3
con = sqlite3.connect("departement.db")

#Pour exécuter des instructions SQL et récupérer les résultats de ces requêtes
cur = con.cursor()

# Création de la DB SQLITE
# cur.execute("CREATE TABLE dept(code_departement, nom_departement, code_region, nom_region)")

with open('departements-france.csv', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        cur.execute("""INSERT INTO dept VALUES('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)""")

        print(row[0:2])