# partida.py
import random

class Partida:
    def __init__(self, jugadores, impostores, lista_palabras):
        self.jugadores_totales = jugadores
        self.impostores_iniciales = impostores
        self.lista_palabras = lista_palabras

        self.jugadores_vivos = [f"Jugador {i+1}" for i in range(jugadores)]
        self.asignaciones = {}  # jugador -> palabra o None
        self.votaciones = {}
        self.palabra_actual = None
        self.ronda = 1

    def nueva_palabra(self):
        self.palabra_actual = random.choice(self.lista_palabras)

    def asignar_roles(self):
        impostores = random.sample(self.jugadores_vivos, self.impostores_iniciales)

        for j in self.jugadores_vivos:
            if j in impostores:
                self.asignaciones[j] = None
            else:
                self.asignaciones[j] = self.palabra_actual

    def votar(self, votante, sospechoso):
        if votante in self.jugadores_vivos:
            self.votaciones[votante] = sospechoso

    def resultado_votacion(self):
        conteo = {}
        for voto in self.votaciones.values():
            if voto in self.jugadores_vivos:
                conteo[voto] = conteo.get(voto, 0) + 1

        if not conteo:
            return None

        expulsado = max(conteo, key=conteo.get)
        return expulsado

    def eliminar_jugador(self, jugador):
        if jugador in self.jugadores_vivos:
            self.jugadores_vivos.remove(jugador)

    def es_impostor(self, jugador):
        return self.asignaciones.get(jugador) is None

    def reiniciar_votacion(self):
        self.votaciones = {}

    def siguiente_ronda(self):
        self.ronda += 1
        self.reiniciar_votacion()


