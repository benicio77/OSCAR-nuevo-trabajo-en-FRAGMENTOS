# principal.py

from partida import Partida
from graficos import Graficos
import pygame
import time

def main():
    print("=== CONFIGURACIÓN DEL JUEGO ===")
    jugadores = int(input("Cantidad de jugadores: "))
    impostores = int(input("Cantidad de impostores: "))

    lista_palabras = [
        "Perro", "Montaña", "Computadora", "Pizza", "Fútbol",
        "Playa", "Coche", "Chocolate", "Escuela", "Robot",
        "Hospital", "Guitarra", "Avión", "Bosque", "Tiburón"
    ]

    partida = Partida(jugadores, impostores, lista_palabras)
    graficos = Graficos()

    partida.nueva_palabra()
    partida.asignar_roles()

    # Mostrar rol a cada jugador
    for jugador in partida.jugadores_vivos:
        print(f"\nTurno de {jugador}. Pulsa ENTER cuando esté listo.")
        input()
        graficos.mostrar_rol(partida.asignaciones[jugador])
        print("Oculta la pantalla y pulsa ENTER para continuar.")
        input()

    # Rondas
    while True:
        print(f"\n=== RONDA {partida.ronda} ===")
        print("Hablen entre ustedes y luego voten.")

        time.sleep(2)

        # Votación
        partida.reiniciar_votacion()
        for jugador in partida.jugadores_vivos:
            voto = input(f"{jugador}, ¿a quién votas? (Jugador X): ")
            partida.votar(jugador, voto)

        expulsado = partida.resultado_votacion()

        if expulsado is None:
            print("Nadie fue expulsado.")
        else:
            print(f"\n{expulsado} ha sido expulsado.")
            graficos.pantalla_eliminado(expulsado)
            partida.eliminar_jugador(expulsado)

            if partida.es_impostor(expulsado):
                print("¡Era impostor!")
            else:
                print("No era impostor.")

        # Condiciones de victoria
        impostores_vivos = sum(1 for j in partida.jugadores_vivos if partida.es_impostor(j))
        civiles_vivos = len(partida.jugadores_vivos) - impostores_vivos

        if impostores_vivos == 0:
            print("\n¡Los civiles ganan!")
            break

        if impostores_vivos >= civiles_vivos:
            print("\nLos impostores ganan.")
            break

        partida.siguiente_ronda()

if __name__ == "__main__":
    main()


