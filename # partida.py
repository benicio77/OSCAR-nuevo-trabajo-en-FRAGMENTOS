# partida.py

class Partida:
    def __init__(self, tiempo, jugadores, impostores):
        self.tiempo = tiempo
        self.jugadores = jugadores
        self.impostores = impostores
        self.votacion_activa = False
        self.estado = "en curso"

    def iniciar_votacion(self):
        self.votacion_activa = True
        print("La votación ha comenzado.")

    def terminar_votacion(self):
        self.votacion_activa = False
        print("La votación ha terminado.")

    def mostrar_info(self):
        print(f"Tiempo: {self.tiempo}")
        print(f"Jugadores: {self.jugadores}")
        print(f"Impostores: {self.impostores}")
        print(f"Votación activa: {self.votacion_activa}")

