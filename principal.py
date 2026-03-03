# principal.py

from partida import Partida
from graficos import Graficos
import pygame
import time

def main():
    print("=== CONFIGURACIÓN DEL JUEGO ===")
    graficos = Graficos()
    jugadores = graficos.input_number("Cantidad de jugadores:", min_val=3, max_val=20)
    impostores = graficos.input_number("Cantidad de impostores:", min_val=1, max_val=max(1, jugadores-1))

    lista_palabras = [
        "Perro", "Montaña", "Computadora", "Pizza", "Fútbol",
        "Playa", "Coche", "Chocolate", "Escuela", "Robot",
        "Hospital", "Guitarra", "Avión", "Bosque", "Tiburón"
    ]

    partida = Partida(jugadores, impostores, lista_palabras)

    partida.nueva_palabra()
    partida.asignar_roles()

    # Mostrar rol a cada jugador
    for jugador in partida.jugadores_vivos:
        graficos.mostrar_mensaje(f"Turno de {jugador}. Pulsa ENTER cuando esté listo.")
        graficos.mostrar_rol(partida.asignaciones[jugador])
        graficos.mostrar_mensaje("Oculta la pantalla y pulsa ENTER para continuar.")

    # Rondas
    while True:
        print(f"\n=== RONDA {partida.ronda} ===")
        print("Hablen entre ustedes y luego voten.")

        time.sleep(2)

        # Votación
        partida.reiniciar_votacion()
        for jugador in list(partida.jugadores_vivos):
            opciones = [p for p in partida.jugadores_vivos if p != jugador]
            if not opciones:
                continue
            sospechoso = graficos.seleccionar_jugador(opciones, f"{jugador}, ¿a quién votas?")
            partida.votar(jugador, sospechoso)

        expulsado = partida.resultado_votacion()

        if expulsado is None:
            print("Nadie fue expulsado.")
        else:
            print(f"\n{expulsado} ha sido expulsado.")
            graficos.pantalla_eliminado(expulsado)
            # comprobar rol antes de eliminar de jugadores_vivos
            era_impostor = partida.es_impostor(expulsado)
            partida.eliminar_jugador(expulsado)

            if era_impostor:
                graficos.mostrar_mensaje("¡Era impostor! Los inocentes ganan.")
                print("¡Era impostor! Los inocentes ganan.")
                break
            else:
                graficos.mostrar_mensaje("No era impostor. ¡El impostor gana!")
                print("No era impostor. El impostor gana.")
                break

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


