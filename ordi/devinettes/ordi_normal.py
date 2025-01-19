########################################################################################
#Ce fichier contient l'ordinateur normal du jeu des devinettes
########################################################################################

import sys, random
sys.path.append("./")

from ordi.ordi_struct import JoueursDevinette

def ordi_cherche_normal(ordi : JoueursDevinette, borne_min: int, borne_max: int, limite:int, réponse: int, proposition: int) -> tuple[int, int, int]:
    """
    Cette fonction permet de jouer au jeu de la devinette avec l'ordinateur en mode normal.

    Args:
        borne_min (int): La borne inférieure pour les propositions.
        borne_max (int): La borne supérieure pour les propositions.
        réponse (int): Indique si la dernière proposition était trop grande (2), trop petite (1), ou correcte (0).
        proposition (int): Dernière proposition effectuée par le bot.

    Returns:
        tuple[int, int, int]: La nouvelle proposition, la borne inférieure mise à jour, et la borne supérieure mise à jour.
    """
    if réponse == 1:  # Trop petit
        borne_min = max(borne_min, proposition + 1)
    elif réponse == 2:  # Trop grand
        borne_max = min(borne_max, proposition - 1)

    # Nouvelle proposition : mélange d'aléatoire et de stratégie
    if borne_min <= borne_max:
        if random.random() < 0.6:
            proposition = (borne_min + borne_max) // 2  # Stratégie : choisir au milieu
        else:
            proposition = random.randint(borne_min, borne_max)  # Choix aléatoire
    else:
        proposition = -1  # Cas où les bornes sont incohérentes

    return proposition, borne_min, borne_max
