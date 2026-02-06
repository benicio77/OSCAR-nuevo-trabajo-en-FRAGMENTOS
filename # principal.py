# principal.py

from partida import Partida
from graficos import Graficos

def menu():
    print("=== CONFIGURACIÓN DE LA PARTIDA ===")
    tiempo = int(input("Tiempo de partida (segundos): "))
    jugadores = int(input("Cantidad de jugadores: "))
    impostores = int(input("Cantidad de impostores: "))

    return tiempo, jugadores, impostores

def main():
    tiempo, jugadores, impostores = menu()

    partida = Partida(tiempo, jugadores, impostores)
    graficos = Graficos()

    partida.mostrar_info()

    # Aquí iría el loop principal del juego
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        graficos.dibujar()

if __name__ == "__main__":
    main()
