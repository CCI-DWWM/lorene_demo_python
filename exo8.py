# Créez un tuple de nombres aléatoires, puis trouvez le nombre le plus grand et le plus petit dans le tuple.

import random

nombres = tuple(random.randint(0, 100) for _ in range(50))

print(nombres)

plus_petit = min(nombres)
plus_grand = max(nombres)

print("Le plus petit nombre est :", plus_petit)
print("Le plus grand nombre est :", plus_grand)


def ma_fonction(v1, v2, v3):
    """
    Cette fonction fait xxx
    :param v1:
    :param v2:
    :param v3:
    :return:
    """
# tout ce que contient le commentaire ci-dessus a été généré automatiquement en faisant """ puis en allant à la ligne,
# j'ai juste rajouté la 1ère phrase "Cette fonction fait xxx"