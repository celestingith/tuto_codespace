"""Ce module fournit une fonction pour calculer une moyenne de valeurs"""

# NB: Ce fichier contient du code à compléter

from rich.console import Console
from rich.markdown import Markdown


def moyenne(valeurs):
    # docstrings en markdown
    """
    # Calcule la moyenne des valeurs.

    **Paramètres**
    - `valeurs` : valeurs dont on veut calculer la moyenne

    **Retour**
    - la moyenne des valeurs

    **Exceptions**
    - `ValueError` : si la liste est vide

    ---
    """
    try:
        moy = sum(valeurs)
        moy = moy/len(valeurs)
        return moy
    except ZeroDivisionError:
        print("False")

if __name__ == "__main__":
    Console().print(Markdown(moyenne.__doc__))
    print("moyenne([10, 20, 15]) :", end=" ")
    print(moyenne([10, 20, 15]))
    print(moyenne([])) 
