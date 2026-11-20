import random
from esquemaiaDaina import EDUCATIONAL_RULES

def generar(tipus_actual):
    if tipus_actual == "aritmetica_basica":
        n1 = random.randint(1, 20)
        n2 = random.randint(1, 20)
        op = random.choice(EDUCATIONAL_RULES["primaria"]["operadors"])
        if op == "+": 
            res = n1 + n2
            passos = [f"1. Tenim una suma de {n1} més {n2}.", "2. Ajuntem les quantitats comptant cap endavant.", f"3. El resultat final és {res}."]
        elif op == "-": 
            res = n1 - n2 if n1 >= n2 else n2 - n1
            n_gran, n_petit = (n1, n2) if n1 >= n2 else (n2, n1)
            passos = [f"1. Tenim una resta: {n_gran} menys {n_petit}.", "2. Traguem la quantitat menor de la major.", f"3. El resultat final és {res}."]
        else: 
            res = n1 * n2
            passos = [f"1. Tenim una multiplicació: {n1} per {n2}.", f"2. Sumem {n1} de manera iterativa {n2} vegades.", f"3. El resultat final és {res}."]
        
        detall = f"{n1} {op} {n2} = ?"
        res_corr = str(res)
    else:
        detall = "Tria si porten accent o no: a-vío / o-e-ll-a"
        res_corr = "a"
        passos = [
            "1. Analitza la síl·laba tònica de la paraula.", 
            "2. Aplica les normes generals d'accentuació (agudes, planes, esdrúixoles).", 
            "3. Determina si porta accent o no."
        ]

    return {
        "enunciat": f"Exercici de Primària ({tipus_actual}):",
        "detall": detall,
        "resposta_correcta": res_corr,
        "passos": passos,
        "tipus": tipus_actual
    }