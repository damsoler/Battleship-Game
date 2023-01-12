#######################################
######### BATTLESHIP ARG ##############
#######################################

#######################################
#########  NOMBRE JUEGO  ##############
#######################################

nombre_juego =  "Batalla Naval" #"Guerra del Atlántico Sur"# 

#######################################
######### TAMAÑO TABLERO ##############
#######################################

TAMANO_TABLERO = 10

########################################
############# BARCOS ###################
########################################
### [1]             FRAGATA          ###
### [1, 1]          DESTRUCTOR       ###  
### [1, 1, 1]       SUBMARINO        ###
### [1, 1, 1, 1]    PORTA-AVIONES    ### 
########################################

BARCOS_JUGADOR = [[1], [1], [1], [1], [1, 1], [1, 1], [1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1, 1]]
BARCOS_PC = [[1, 1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1], [1, 1], [1, 1], [1], [1], [1], [1]]

########################################
############# BIENVENIDA ###############
########################################

mensaje = """
La guerra de las Malvinas (en inglés, Falklands War) fue un conflicto armado 
    entre Argentina y el Reino Unido desatado en 1982, en el cual se disputó la 
        soberanía de las islas Malvinas, Georgias del Sur y Sandwich del Sur 
            ubicadas en el Atlántico Sur.
La Organización de las Naciones Unidas (ONU) continúa considerando los tres archipiélagos 
    con sus aguas circundantes como territorios DISPUTADOS

        CARGANDO CAMPO DE BATALLA......................................................
        CARGANDO FLOTA.................................................................
        CARGANDO REGLAS DE JUEGO ......................................................
        CARGANDO LOGICA PC-AI  .......................................................

        """

tips_ubicacion_barcos = """
Es su turno para ubicar sus barcos. Usted dispone de:
            > 4 FRAGATAS 1 posición sobre el tablero.
            > 3 DESTRUCTORES que ocupan 2 posiciones.
            > 2 SUBMARINOS que ocupan 3 posiciones.
            > 1 PORTA-AVIONES de 4 posiciones.
            
Su tablero tiene 10 filas por 10 columnas, y las coordenadas de ambos ejes están numeradas del 0 al 9.
Para ubicar cada barco, deberá indicar sólo las coordenadas de la proa del barco; si el barco es de 2 posiciones o más, 
deberá indicar la orientación del barco: si elige vertical, el resto de las posicones del barco se completarán automáticamente 
en dirección hacia abajo de las coordenadas de la proa del barco; y si elige la orientación horizontal, el barco se completará 
en dirección hacia la derecha de las coordenadas de la proa del barco.
"""

#########################################
############# 2 jugadores   #############
############# 1 jugador -PC #############
#########################################

dual_player = False 
