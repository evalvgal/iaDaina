import random

def generar(tipus_actual):
    if tipus_actual == "derivades":
        a = random.randint(2, 6)
        n = random.randint(2, 4)
        detall = f"f(x) = {a}x^{n}"
        res_corr = f"{a*n}x^{n-1}"
        passos = [
            f"1. Funció donada: f(x) = {a}x^{n}.",
            f"2. Aplica la regla de la potència (baixa l'exponent multiplicant i resta 1): {a} · {n}x^({n}-1).",
            f"3. Simplifica el resultat: {a*n}x^{n-1}."
        ]
    else:
        detall = "Equilibra la següent reacció: H2 + O2 -> H2O"
        res_corr = "2h2+o2->2h2o"
        passos = [
            "1. Compta els àtoms de cada element a reactius i productes.", 
            "2. Ajusta els coeficients estequiomètrics per igualar hidrògens i oxígens.", 
            "3. Comprova que es compleix la conservació de la massa."
        ]

    return {
        "enunciat": f"Exercici de Batxillerat ({tipus_actual}):",
        "detall": detall,
        "resposta_correcta": res_corr,
        "passos": passos,
        "tipus": tipus_actual
    }