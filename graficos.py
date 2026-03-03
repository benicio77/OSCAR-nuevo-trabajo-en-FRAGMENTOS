# graficos.py
import sys
import pygame


class Graficos:
    def __init__(self, ancho=800, alto=600):
        pygame.init()
        self.ventana = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption("Impostor de Palabras")
        self.fuente = pygame.font.SysFont("Arial", 40)

    def mostrar_rol(self, palabra):
        if palabra is None:
            color = (200, 0, 0)  # rojo impostor
            texto = "ERES IMPOSTOR"
        else:
            color = (0, 180, 0)  # verde civil
            texto = f"Palabra: {palabra}"

        self.ventana.fill(color)
        render = self.fuente.render(texto, True, (255, 255, 255))
        rect = render.get_rect(center=(400, 300))
        self.ventana.blit(render, rect)
        pygame.display.update()

        self._esperar_tecla()

    def pantalla_eliminado(self, jugador):
        self.ventana.fill((50, 50, 50))
        texto = f"{jugador} ha sido eliminado"
        render = self.fuente.render(texto, True, (255, 255, 255))
        rect = render.get_rect(center=(400, 300))
        self.ventana.blit(render, rect)
        pygame.display.update()
        self._esperar_tecla()

    def mostrar_mensaje(self, texto):
        self.ventana.fill((30, 30, 30))
        render = self.fuente.render(texto, True, (255, 255, 255))
        rect = render.get_rect(center=(400, 300))
        self.ventana.blit(render, rect)
        pygame.display.update()
        self._esperar_tecla()

    def input_number(self, prompt, min_val=1, max_val=99):
        valor = ""
        font_small = pygame.font.SysFont("Arial", 36)
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        if valor.isdigit():
                            n = int(valor)
                            if min_val <= n <= max_val:
                                return n
                        # invalid, ignore
                    elif evento.key == pygame.K_BACKSPACE:
                        valor = valor[:-1]
                    else:
                        if evento.unicode.isdigit():
                            valor += evento.unicode

            self.ventana.fill((20, 20, 20))
            prompt_r = font_small.render(prompt, True, (255, 255, 255))
            self.ventana.blit(prompt_r, (50, 200))
            val_r = font_small.render(valor or "_", True, (200, 200, 200))
            self.ventana.blit(val_r, (50, 260))
            info = pygame.font.SysFont("Arial", 20).render("ENTER para confirmar", True, (150, 150, 150))
            self.ventana.blit(info, (50, 320))
            pygame.display.update()

    def seleccionar_jugador(self, opciones, prompt="Selecciona:"):
        if not opciones:
            return None
        seleccion = 0
        font_small = pygame.font.SysFont("Arial", 28)
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_UP:
                        seleccion = (seleccion - 1) % len(opciones)
                    elif evento.key == pygame.K_DOWN:
                        seleccion = (seleccion + 1) % len(opciones)
                    elif evento.key == pygame.K_RETURN:
                        return opciones[seleccion]

            self.ventana.fill((30, 30, 30))
            prompt_r = font_small.render(prompt, True, (255, 255, 255))
            self.ventana.blit(prompt_r, (50, 30))

            for i, opcion in enumerate(opciones):
                color = (255, 255, 0) if i == seleccion else (200, 200, 200)
                text_r = font_small.render(f"{i+1}. {opcion}", True, color)
                self.ventana.blit(text_r, (60, 80 + i * 34))

            hint = pygame.font.SysFont("Arial", 18).render("ARRIBA/ABAJO para moverte, ENTER para elegir", True, (150, 150, 150))
            self.ventana.blit(hint, (50, 520))
            pygame.display.update()

    def _esperar_tecla(self):
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    esperando = False
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

