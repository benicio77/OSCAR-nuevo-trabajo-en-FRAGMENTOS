# graficos.py
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

    def _esperar_tecla(self):
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    esperando = False
                if evento.type == pygame.QUIT:
                    esperando = False

