import random

def generar(tipus_actual):
    if tipus_actual == "fisica_mru":
        v = random.randint(10, 90)
        t = random.randint(2, 5)
        d = v * t
        detall = f"Un cotxe circula a {v} km/h durant {t} hores. Quina distància recorre?"
        res_corr = f"{d} km"
        passos = [
            f"1. Identifica les dades: Velocitat (v) = {v} km/h, Temps (t) = {t} h.",
            "2. Recorda la fórmula del MRU: Distància (d) = v · t.",
            f"3. Substitueix els valors: d = {v} · {t} = {d} km."
        ]
    elif tipus_actual == "equacions":
        a = random.randint(2, 6)
        b = random.randint(1, 15)
        x = random.randint(1, 10)
        c = (a * x) + b
        detall = f"{a}x + {b} = {c}  (Quin és el valor de x?)"
        res_corr = str(x)
        passos = [
            f"1. Equació inicial: {a}x + {b} = {c}.",
            f"2. Aïlla el terme amb x passant el {b} a l'altre costat restant: {a}x = {c} - {b} => {a}x = {c - b}.",
            f"3. Despeja la x dividint pel coeficient: x = {c - b} / {a} => x = {x}."
        ]
    else:
        detall = "Analitza sintàcticament la frase: 'En Joan compra pomes.'"
        res_corr = "predicat"
        passos = [
            "1. Identifica el subjecte de l'oració preguntant 'Qui compra pomes?'.", 
            "2. La resta de la frase constitueix el predicat.", 
            "3. Identifica el nucli del predicat (el verb)."
        ]

    return {
        "enunciat": f"Problema d'ESO ({tipus_actual}):",
        "detall": detall,
        "resposta_correcta": res_corr,
        "passos": passos,
        "tipus": tipus_actual
    }