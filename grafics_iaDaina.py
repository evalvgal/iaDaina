import pygame

# Colors corporatius i pedagògics
BLANC = (255, 255, 255)
NEGRE = (40, 40, 40)
BLAU_PASTEL = (70, 130, 180)
BLAU_CLAR = (100, 160, 210)
BLAU_BOTO = (51, 122, 183)
VERD_EXIT = (46, 139, 87)
VERD_CLAR = (70, 170, 115)
GRIS_FONS = (245, 247, 250)
VERMELL_SORTIDA = (220, 60, 60)
VERMELL_CLAR = (240, 100, 100)
TARONJA_AJUDA = (230, 140, 40)
TARONJA_CLAR = (245, 170, 80)
ROSA_INF = (255, 182, 193)
ROSA_CLAR = (255, 210, 220)
TARONJA_PRI = (255, 165, 0)
TARONJA_PRI_CLAR = (255, 195, 70)
LILA_ESO = (147, 112, 219)
LILA_CLAR = (175, 145, 240)
VERMELL_BATX = (205, 92, 92)
VERMELL_BATX_CLAR = (230, 120, 120)

class VistaGraficaDaina:
    def __init__(self, screen):
        self.screen = screen
        self.amplada, self.alcada = screen.get_size()
        pygame.font.init()
        
        # Mida de font restaurada a l'original (32px)
        self.font_gran = pygame.font.SysFont("Arial", 32, bold=True)
        self.font_mitjana = pygame.font.SysFont("Arial", 22)
        self.font_petita = pygame.font.SysFont("Arial", 18)

    def _dibuixar_boto_interactiu(self, rect, color_normal, color_hover, text, es_gran=False):
        mouse_pos = pygame.mouse.get_pos()
        esta_a_sobre = rect.collidepoint(mouse_pos)
        color_actual = color_hover if esta_a_sobre else color_normal
        
        pygame.draw.rect(self.screen, color_actual, rect, border_radius=10)
        
        font = self.font_gran if es_gran else self.font_mitjana
        txt_render = font.render(text, True, BLANC)
        self.screen.blit(txt_render, (rect.centerx - txt_render.get_width() // 2, rect.centery - txt_render.get_height() // 2))

    def _dibuixar_boto_sortida(self):
        amplada_boto, alcada_boto = 110, 40
        x = self.amplada - amplada_boto - 20
        y = 20
        rect = pygame.Rect(x, y, amplada_boto, alcada_boto)
        self._dibuixar_boto_interactiu(rect, VERMELL_SORTIDA, VERMELL_CLAR, "Sortir")
        return rect

    def _dibuixar_boto_enrere(self):
        amplada_boto, alcada_boto = 110, 40
        x = 50
        y = self.alcada - 60
        rect = pygame.Rect(x, y, amplada_boto, alcada_boto)
        self._dibuixar_boto_interactiu(rect, BLAU_BOTO, BLAU_CLAR, "Enrere")
        return rect

    def _dibuixar_text_multilinia(self, text, font, color, x, y, max_amplada):
        """ Divideix el text automàticament en diverses línies si supera l'amplada màxima """
        paraules = text.split(' ')
        linies = []
        linia_actual = ""

        for paraula in paraules:
            prova_linia = f"{linia_actual} {paraula}".strip()
            if font.size(prova_linia)[0] <= max_amplada:
                linia_actual = prova_linia
            else:
                linies.append(linia_actual)
                linia_actual = paraula
        if linia_actual:
            linies.append(linia_actual)

        y_actual = y
        for linia in linies:
            txt_surface = font.render(linia, True, color)
            self.screen.blit(txt_surface, (x, y_actual))
            y_actual += font.get_linesize() + 4

        return y_actual

    def dibuixar_menu_principal(self):
        self.screen.fill(GRIS_FONS)
        titol = self.font_gran.render("Generador de Suport Escolar (Offline)", True, NEGRE)
        self.screen.blit(titol, (self.amplada // 2 - titol.get_width() // 2, 50))
        
        sub = self.font_mitjana.render("Selecciona l'etapa educativa:", True, (100, 100, 100))
        self.screen.blit(sub, (self.amplada // 2 - sub.get_width() // 2, 110))

        botons = [
            {"etapa": "infantil", "text": "Infantil (I3-I5)", "color": ROSA_INF, "hover": ROSA_CLAR, "y": 180},
            {"etapa": "primaria", "text": "Primària", "color": TARONJA_PRI, "hover": TARONJA_PRI_CLAR, "y": 270},
            {"etapa": "eso", "text": "ESO", "color": LILA_ESO, "hover": LILA_CLAR, "y": 360},
            {"etapa": "batxillerat", "text": "Batxillerat", "color": VERMELL_BATX, "hover": VERMELL_BATX_CLAR, "y": 450}
        ]

        rects_botons = {}
        for b in botons:
            rect = pygame.Rect(self.amplada // 2 - 200, b["y"], 400, 65)
            self._dibuixar_boto_interactiu(rect, b["color"], b["hover"], b["text"], es_gran=True)
            rects_botons[b["etapa"]] = rect

        rect_sortida = self._dibuixar_boto_sortida()
        rects_botons["_sortida"] = rect_sortida

        return rects_botons

    def dibuixar_menu_subtipus(self, etapa_actual, llista_subtipus):
        self.screen.fill(GRIS_FONS)
        titol = self.font_gran.render(f"Etapa: {etapa_actual.capitalize()}", True, NEGRE)
        self.screen.blit(titol, (self.amplada // 2 - titol.get_width() // 2, 50))
        
        sub = self.font_mitjana.render("Selecciona el tipus d'exercici:", True, (100, 100, 100))
        self.screen.blit(sub, (self.amplada // 2 - sub.get_width() // 2, 110))

        rects_botons = {}
        y_inici = 190
        for subtipus in llista_subtipus:
            rect = pygame.Rect(self.amplada // 2 - 220, y_inici, 440, 60)
            text_visible = subtipus.replace("_", " ").capitalize()
            self._dibuixar_boto_interactiu(rect, BLAU_PASTEL, BLAU_CLAR, text_visible)
            rects_botons[subtipus] = rect
            y_inici += 80

        rect_enrere = self._dibuixar_boto_enrere()
        rect_sortida = self._dibuixar_boto_sortida()
        rects_botons["_enrere"] = rect_enrere
        rects_botons["_sortida"] = rect_sortida

        return rects_botons

    def dibuixar_pantalla_exercici(self, exercici, feedback=""):
        self.screen.fill(GRIS_FONS)
        max_amplada_text = self.amplada - 160

        # Enunciat amb la mida original (32px) i salts de línia automàtics
        y_final = self._dibuixar_text_multilinia(exercici["enunciat"], self.font_gran, NEGRE, 80, 70, max_amplada_text)

        # Detall de l'exercici
        self._dibuixar_text_multilinia(exercici["detall"], self.font_mitjana, BLAU_PASTEL, 80, y_final + 20, max_amplada_text)

        if feedback:
            color_fb = VERD_EXIT if "Correcte" in feedback else (178, 34, 34)
            txt_fb = self.font_mitjana.render(feedback, True, color_fb)
            self.screen.blit(txt_fb, (80, 260))

        rect_enrere = self._dibuixar_boto_enrere()
        rect_sortida = self._dibuixar_boto_sortida()

        rect_genera = pygame.Rect(self.amplada // 2 + 20, self.alcada - 70, 210, 50)
        self._dibuixar_boto_interactiu(rect_genera, VERD_EXIT, VERD_CLAR, "Genera exercici")

        rect_passos = pygame.Rect(self.amplada // 2 - 240, self.alcada - 70, 240, 50)
        self._dibuixar_boto_interactiu(rect_passos, TARONJA_AJUDA, TARONJA_CLAR, "Mostra solució pas a pas")

        return {
            "_enrere": rect_enrere, 
            "_sortida": rect_sortida, 
            "_genera": rect_genera,
            "_passos": rect_passos
        }

    def dibuixar_passos_solucio(self, exercici):
        self.screen.fill(GRIS_FONS)
        max_amplada_text = self.amplada - 160
        
        titol = self.font_gran.render("Resolució Pas a Pas", True, TARONJA_AJUDA)
        self.screen.blit(titol, (80, 40))

        txt_ref = f"Problema: {exercici['enunciat']} {exercici['detall']}"
        y_pos = self._dibuixar_text_multilinia(txt_ref, self.font_petita, NEGRE, 80, 90, max_amplada_text)

        y_pos += 20
        for pas in exercici["passos"]:
            y_pos = self._dibuixar_text_multilinia(pas, self.font_mitjana, NEGRE, 100, y_pos, max_amplada_text)
            y_pos += 10

        rect_enrere = self._dibuixar_boto_enrere()
        rect_sortida = self._dibuixar_boto_sortida()

        return {
            "_enrere": rect_enrere,
            "_sortida": rect_sortida
        }