from esquemaiaDaina import EDUCATIONAL_RULES
from Infantil.exercicisInfantil import generar as gen_infantil
from Primaria.exercicisPrimaria import generar as gen_primaria
from ESO.exercicisESO import generar as gen_eso
from Batxillerat.exercicisBatxillerat import generar as gen_batx

class ModelReglesEscolars:
    def __init__(self):
        self.etapa_actual = None
        self.tipus_actual = None
        self.exercici_actual = None

    def configurar_etapa(self, etapa):
        self.etapa_actual = etapa.lower()
        if self.etapa_actual not in EDUCATIONAL_RULES:
            raise ValueError("Etapa no reconeguda.")

    def obtenir_subtipus_etapa(self):
        if not self.etapa_actual:
            return []
        return EDUCATIONAL_RULES[self.etapa_actual]["tipus"]

    def configurar_subtipus(self, tipus_contingut):
        self.tipus_actual = tipus_contingut

    def generar_nou_exercici(self):
        if not self.etapa_actual or not self.tipus_actual:
            raise ValueError("Cal configurar l'etapa i el subtipus primer.")
        
        # Deriva la generació cap al mòdul de la carpeta corresponent
        if self.etapa_actual == "infantil":
            self.exercici_actual = gen_infantil(self.tipus_actual)
        elif self.etapa_actual == "primaria":
            self.exercici_actual = gen_primaria(self.tipus_actual)
        elif self.etapa_actual == "eso":
            self.exercici_actual = gen_eso(self.tipus_actual)
        elif self.etapa_actual == "batxillerat":
            self.exercici_actual = gen_batx(self.tipus_actual)
            
        return self.exercici_actual

    def validar_resposta(self, resposta_usuari):
        if not self.exercici_actual:
            return False
        return resposta_usuari.strip().lower() == self.exercici_actual["resposta_correcta"].lower()