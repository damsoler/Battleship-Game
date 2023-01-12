
from hf_clases import tablero
import hf_funciones, time, pandas, numpy, random
from hf_funciones import clear


clear()

hf_funciones.intro()
time.sleep (3)


def battleship():
    nom_jug = hf_funciones.set_jugador()

    time.sleep (1)

    ## marca la dificultad del juego, estará relacionada con la cantidad de disparos doble tiros de la PC y tamaño de tablero##
    # niv_dif = hf_funciones.set_dificultad() 
    print("Inicializando Tableros...\n\n")

    time.sleep(2.5)

    clear()
    tab_j1_naves = tablero(nom_jug, "tablero de naves")
    tab_j1_naves.inicializar_tablero()
    tab_j1_naves.imprimir_tablero() 
    tab_j1_disparos = tablero(nom_jug, "tablero de disparos")
    tab_j1_disparos.inicializar_tablero()
    tab_j1_disparos.imprimir_tablero()

    time.sleep(1)
    clear()

    tab_pc_naves = tablero("Pc-AI", "tablero de naves")
    tab_pc_naves.inicializar_tablero()
    tab_pc_naves.imprimir_tablero()
    tab_pc_disparos = tablero("Pc-AI", "tablero de disparos")
    tab_pc_disparos.inicializar_tablero()
    tab_pc_disparos.imprimir_tablero()

    time.sleep(1)
    clear()

    tab_j1_naves.imprimir_tablero()
    tab_j1_naves.ubicar_barcos_jugador()
    time.sleep(3)
    clear()

    tab_pc_naves.random_barcos_pc()
    clear()
    # tab_pc_naves.imprimir_tablero()
    # time.sleep(10)
    # clear()

    jugadores = ["Pc-AI", nom_jug]
    proximo_turno = random.choice(jugadores)
    print(f"El sorteo inicial dio como resultado que {proximo_turno} comenzará con el juego.")
    time.sleep(3)
    clear()

    while True:
        if proximo_turno == "Pc-AI":
            tab_pc_disparos.disparar(tab_j1_naves, jugador_pc=True)
            disparos_acertados = 0

            for i in range(10):
                for j in range(10):
                    if tab_pc_disparos.matrix[i][j] == "X":
                        disparos_acertados += 1
            
            if disparos_acertados >= 20:
                print("\n\nEL GANADOR ES Pc-AI !!!\n\n")
                time.sleep(4)
                while True:
                    play_again = input("Desea jugar de nuevo? Tipee 'y' para SI, o 'n' para NO: ").lower()
                    if (play_again == "n") or (play_again == "y"):
                        break
                    else:
                        print("Input no válido.")
                if play_again == "y":
                    battleship()
                else:
                    print("\nHasta la próxima!")
                    time.sleep(4)
                    clear()
                    break
            else:
                print(f"\nAhora es el turno de disparar para {nom_jug}.")
                proximo_turno = nom_jug
                time.sleep(5)
                clear()
        else:
            tab_j1_disparos.disparar(tab_pc_naves)
            disparos_acertados = 0

            for i in range(10):
                for j in range(10):
                    if tab_j1_disparos.matrix[i][j] == "X":
                        disparos_acertados += 1
            
            if disparos_acertados >= 20:
                print(f"\n\nEL GANADOR ES {nom_jug} !!!\n\nBien Jugado!!!!!\n\n")
                time.sleep(4)
                while True:
                    play_again = input("Desea jugar de nuevo? Tipee 'y' para SI, o 'n' para NO: ").lower()
                    if (play_again == "n") or (play_again == "y"):
                        break
                    else:
                        print("Input no válido.")
                if play_again == "y":
                    battleship()
                else:
                    print("\nHasta la próxima!")
                    time.sleep(4)
                    clear()
                    break
            else:
                print("\nAhora es el turno de disparar para Pc-AI.")
                proximo_turno = "Pc-AI"
                time.sleep(5)
                clear()

battleship()