import pygame
import sys
from iaReglesDaina import ModelReglesEscolars
from grafics_iaDaina import VistaGraficaDaina

def main():
    pygame.init()

    # 1. Detectar automàticament la resolució nativa de la pantalla de l'ordinador/pissarra
    info_pantalla = pygame.display.Info()
    amplada_nativa, alcada_nativa = info_pantalla.current_w, info_pantalla.current_h

    # 2. Inicialitzar directament a pantalla completa amb la resolució nativa
    screen = pygame.display.set_mode((amplada_nativa, alcada_nativa), pygame.FULLSCREEN)
    pygame.display.set_caption("Generador de Suport Escolar - Escola (MVC)")

    model = ModelReglesEscolars()
    vista = VistaGraficaDaina(screen)

    estat_app = "MENU_ETAPA"  # Estats: "MENU_ETAPA", "MENU_SUBTIPUS", "EXERCICI", "PASSOS"
    feedback_actual = ""
    rects_actuals = {}

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_mouse = event.pos
                
                # 1. Botó vermell "Sortir" (global a totes les pantalles)
                if "_sortida" in rects_actuals and rects_actuals["_sortida"].collidepoint(pos_mouse):
                    pygame.quit()
                    sys.exit()

                # 2. Botó blau "Enrere"
                if "_enrere" in rects_actuals and rects_actuals["_enrere"].collidepoint(pos_mouse):
                    if estat_app == "MENU_SUBTIPUS":
                        estat_app = "MENU_ETAPA"
                    elif estat_app == "EXERCICI":
                        estat_app = "MENU_SUBTIPUS"
                    elif estat_app == "PASSOS":
                        estat_app = "EXERCICI"

                # 3. Accions específiques de la pantalla d'EXERCICI
                if estat_app == "EXERCICI":
                    if "_genera" in rects_actuals and rects_actuals["_genera"].collidepoint(pos_mouse):
                        model.generar_nou_exercici()
                        feedback_actual = ""
                    elif "_passos" in rects_actuals and rects_actuals["_passos"].collidepoint(pos_mouse):
                        estat_app = "PASSOS"

                # 4. Navegació dels menús principals
                if estat_app == "MENU_ETAPA":
                    for etapa, rect in rects_actuals.items():
                        if etapa not in ["_sortida", "_enrere"] and rect.collidepoint(pos_mouse):
                            model.configurar_etapa(etapa)
                            estat_app = "MENU_SUBTIPUS"

                elif estat_app == "MENU_SUBTIPUS":
                    for subtipus, rect in rects_actuals.items():
                        if subtipus not in ["_sortida", "_enrere"] and rect.collidepoint(pos_mouse):
                            model.configurar_subtipus(subtipus)
                            model.generar_nou_exercici()
                            feedback_actual = ""
                            estat_app = "EXERCICI"

            elif event.type == pygame.KEYDOWN:
                # Tecla ESC: Tanca l'aplicació
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                # Tecla F11: Alterna entre pantalla completa i mode finestra
                elif event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()

        # Renderitzat segons l'estat actual
        if estat_app == "MENU_ETAPA":
            rects_actuals = vista.dibuixar_menu_principal()
        elif estat_app == "MENU_SUBTIPUS":
            subtipus_disponibles = model.obtenir_subtipus_etapa()
            rects_actuals = vista.dibuixar_menu_subtipus(model.etapa_actual, subtipus_disponibles)
        elif estat_app == "EXERCICI":
            rects_actuals = vista.dibuixar_pantalla_exercici(model.exercici_actual, feedback_actual)
        elif estat_app == "PASSOS":
            rects_actuals = vista.dibuixar_passos_solucio(model.exercici_actual)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()