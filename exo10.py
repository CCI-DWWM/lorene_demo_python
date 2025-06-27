"""
Créer une fonction qui permette d'afficher un nom encadré :
┌──────────┐
│ Emmanuel │
└──────────┘
"""

from colorama import Fore, Back, Style

def encadre(name):
    nb_chars = len(name) + 2
    line = "─" * nb_chars
    red_name = Fore.RED + name + Style.RESET_ALL

    print(f"┌{line}┐\n│ {red_name} │\n└{line}┘")

encadre("Thibaut")
encadre("Lorène")
encadre("Olivier")


print("------------------------------------------")

# autre solution de code


import sys
from colorama import Fore, Back, Style

def encadre(name, color='BLACK'):
    """
       Affiche le nom encadré dans la couleur spécifiée
       :param name: ce qui doit être encadré
       :param color: couleur du cadre (string, noir par défault)
       :return: rien
       """
    x = '─' * len(name)
    couleur = getattr(Fore, color.upper())
    print(f"""
┌─{x}─┐
│ {couleur}{name}{Style.RESET_ALL} │
└─{x}─┘""")

if __name__ == "__main__":
    print(f"=> {sys.argv[1]}")

    encadre(sys.argv[1], sys.argv[2])