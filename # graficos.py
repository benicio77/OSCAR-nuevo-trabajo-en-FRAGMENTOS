# graficos.py
import pygame

class Graficos:
    def __init__(self, ancho=800, alto=600):
        pygame.init()
        self.ventana = pygame.display.set_mode((ancho, alto))
        pygame.display.set_caption("Juego del Impostor")
        self.fondo = None

    def cargar_fondo(self, ruta):
        self.fondo = pygame.image.load(ruta)

    def dibujar(self):
        if self.fondo:
            self.ventana.blit(self.fondo, (0, 0))
        pygame.display.update()
