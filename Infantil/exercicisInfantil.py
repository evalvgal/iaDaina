import random
from esquemaiaDaina import EDUCATIONAL_RULES
from Infantil.Dibuix.grafics_dibuix import DibuixAppGrafica

def generar(tipus_actual):
    if tipus_actual == "dibuix_animat":
        # Crida i executa l'entorn interactiu de dibuix animat
        app_dibuix = DibuixAppGrafica()
        app_dibuix.executar()
        return {
            "enunciat": "Dibuix Màgic i Animant",
            "detall": "Has creat un dibuix fantàstic!",
            "resposta_correcta": "creat",
            "passos": ["1. Dibuixa el que vulguis.", "2. Prem 'Animar dibuix' per veure'l cobrar vida."],
            "tipus": tipus_actual
        }

    # Resta de lògica per a comptar objectes o formes
    num = random.randint(1, 5)
    obj = random.choice(EDUCATIONAL_RULES["infantil"]["banc_objectes"])
    passos = [
        f"1. Observa atentament la imatge o el grup de {obj}.",
        "2. Assenyala amb el dit cada element un per un.",
        f"3. Comptatge final: hi ha exactament {num} elements."
    ]
    return {
        "enunciat": "Compta quants elements hi ha:",
        "detall": f"Objectiu: {num} {obj}",
        "resposta_correcta": str(num),
        "passos": passos,
        "tipus": tipus_actual
    }