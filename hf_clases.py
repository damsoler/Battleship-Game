from pyparsing import line_end
from hf_variables import TAMANO_TABLERO, BARCOS_JUGADOR, BARCOS_PC, tips_ubicacion_barcos
import numpy as np
import random, time
from hf_funciones import chequear_input_coord, clear, texto_vintage, chequear_coords_ady, chk_bar, chequear_disparos_anteriores
from tkinter import W

########################################
#############   TABLERO  ###############
########################################

class tablero:
    """clase tablero para el juego"""

    def __init__(self,
                nombre_jug, 
                tipo,
                matrix = [], 
                tam_tab=TAMANO_TABLERO
                ):
        self.nombre_jug = nombre_jug
        self.tipo = tipo
        self.matrix = matrix
        self.tam_tab = tam_tab
        self.coords_posicion_barcos = []


    def inicializar_tablero(self):
        self.matrix = np.full((self.tam_tab,self.tam_tab), fill_value = '▓')
        # return self.matrix_coord
        

    def imprimir_tablero(self):
        print(f"\n{self.nombre_jug} - {self.tipo}")
        print("   0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9\n")
        print(self.matrix)
        print()

#################################################################
#####  UBICACION DE LOS BARCOS MANUALMENTE POR EL JUGADOR #######
#################################################################

    def ubicar_barcos_jugador(self):
        n = 0
        print("""
        ########################################
        ############# BARCOS ###################
        ########################################
        ### [1]             FRAGATA          ###
        ### [1, 1]          DESTRUCTOR       ###  
        ### [1, 1, 1]       SUBMARINO        ###
        ### [1, 1, 1, 1]    PORTA-AVIONES    ### 
        ########################################
        """)
        texto_vintage(tips_ubicacion_barcos)
        
        time.sleep(2)

        for barco in BARCOS_JUGADOR:
            n += 1
            coords_pos_barco = []
            coords_barco_ok = False

            while not coords_barco_ok:
                print(f"\nPor favor {self.nombre_jug}, ubique el {n}° barco.")
                print(f"\nEste barco es de {len(barco)} posiciones.")
                orientacion = None

                if n > 4:
                    control_orientacion = True
                    while control_orientacion:
                        print("\nIndique la orientación sobre la que se extenderá el barco:")
                        orientacion = input("\t\t\t\t\t\ttipee 'v' si desea que se extienda en dirección vertical (hacia abajo),\n"
                                            "\t\t\t\t\t\to 'h' para que sea en dirección horizontal (hacia la derecha):\n").lower()
                        if (orientacion == "v") or (orientacion == "h"):
                            break
                        else:
                            print(f"El valor '{orientacion}' ingresado no es válido.")

                limite_superior = [9, 9]
                if orientacion == "v":
                    limite_superior[0] = 10 - len(barco)
                elif orientacion == "h":
                    limite_superior[1] = 10 - len(barco)

                fila = chequear_input_coord("fila donde se ubicará la proa del barco", limite_superior[0])
                columna = chequear_input_coord("columna donde se ubicará la proa del barco", limite_superior[1])
                
                time.sleep(0.6)

                for indice in range(len(barco)):
                    if orientacion == "v":
                        coord_fila, coord_columna = (fila + indice), columna
                    elif orientacion == "h":
                        coord_fila, coord_columna = fila, (columna + indice)
                    else:
                        coord_fila, coord_columna = fila, columna
                        
                    check_coords = chequear_coords_ady(self.matrix, indice, coord_fila, coord_columna, orientacion)

                    if check_coords == True:
                        coords_pos_barco.append([coord_fila, coord_columna])

                    elif check_coords == False:
                        coords_pos_barco = []
                        print(f"\nLa ubicación elegida para el {n}° barco no es válida, ya que se superpone o colinda a menos de un "
                        "casillero de distancia con otra nave.\n\nVuelva a intentarlo.")
                        break   # me saca del for y me devuelve al inicio del while para intentar ubicar el mismo barco
                
                if len(barco) == len(coords_pos_barco):
                    for i, j in coords_pos_barco:
                        self.matrix[i][j] = "O"
                    self.coords_posicion_barcos.append(coords_pos_barco)
                    coords_barco_ok = True

            clear()
            print(f"\n{self.nombre_jug} - {self.tipo}")
            print(f"{self.matrix}\n")
            

    def disparar(self, adversario, jugador_pc=False):
        print(f"{self.nombre_jug}, deje la piedad a un lado y realice su disparo hacia {adversario.nombre_jug}.")
        self.imprimir_tablero()
        time.sleep(1.5)

        disparo_fila, disparo_columna = chequear_disparos_anteriores(self.matrix, jugador_pc)
        print(f"\nLas coordenadas de disparo elegidas por {self.nombre_jug} son [{disparo_fila},{disparo_columna}].")
        time.sleep(2)
        if adversario.matrix[disparo_fila][disparo_columna] == "O":
            print(f"\nMenuda puntería! {self.nombre_jug} le ha dado a un barco!\nSe ha ganado un nuevo turno!")
            self.matrix[disparo_fila][disparo_columna] = "X"
            time.sleep(5)
            clear()
            if jugador_pc == True:
                self.disparar(adversario, jugador_pc=True)
            else:
                self.disparar(adversario)
        else:
            print(f"\nNada más que agua para {self.nombre_jug}.")
            self.matrix[disparo_fila][disparo_columna] = "-"


#############################################
#####  RANDOM UBICATION FOR PC PLAYER #######
#############################################


    def random_barcos_pc(self):
       
        for barco in BARCOS_PC:

            if len(barco) == 4:
                '''ENTRADA DE LOS BARCOS DE 4 POSICIONES'''
                
                barco_ok = False    # inicio condicional del while, hasta no tener una posicion valida no saldrá
                while barco_ok == False:
                                       
                    random_orientacion = random.choice(["v","h"])   # random de vertical (hacia abajo) u horizontal (hacia derecha) 

                    if random_orientacion == "v":                   # modo vertical
                        random_fila = random.randint(0,6)           # limito el randint para que en vertical no se salga del tablero
                        random_columna = random.randint(0,9)
                        barco_ok = chk_bar(self.matrix, random_fila,random_columna, "v", 4)
                        if barco_ok == True:
                            for i in range(len(barco)):
                                #print(f"fila_{random_fila + i}, columna_{random_columna}")# print temporal para ver como se comporta el programa
                                self.matrix[random_fila + i][random_columna] = "O"
                            print(f"PORTA-AVIONES, coord : {random_fila},{random_columna} : {random_orientacion} : ACEPTADA")
                        #else:
                            #print(f" coord : {random_fila},{random_columna} {random_orientacion} :intento NO VALIDO\n")  
                        
                    elif random_orientacion == "h" :  # modo horizontal
                
                        random_fila = random.randint(0,9)           
                        random_columna = random.randint(0,6)        # limito el randint para que en horizontal no se salga del tablero
                        barco_ok = chk_bar(self.matrix,random_fila, random_columna, "h", 4)
                        if barco_ok == True:
                            for i in range(len(barco)):
                                #print(f"fila_{random_fila}, columna_{random_columna + i}")# print temporal para ver como se comporta el programa
                                self.matrix[random_fila][random_columna + i] = "O"
                            print(f"PORTA-AVIONES, coord : {random_fila},{random_columna} : {random_orientacion} : ACEPTADA")
                        #else:
                            #print(f" coord : {random_fila},{random_columna} {random_orientacion} :intento NO VALIDO\n")

            elif len(barco) == 3:
                '''ENTRADA DE LOS BARCOS DE 3 POSICIONES'''
                
                barco_ok = False    #inicio condicional del while, hasta no tener una posicion valida no saldrá
                while barco_ok == False:
                    
                    random_orientacion = random.choice(["v","h"])   # random de vertical (hacia abajo) u horizontal (hacia derecha) 

                    if random_orientacion == "v":                   # modo vertical
                        random_fila = random.randint(0,7)           # limito el randint para que en vertical no se salga del tablero
                        random_columna = random.randint(0,9)
                        barco_ok = chk_bar(self.matrix, random_fila,random_columna, "v", 3)
                        if barco_ok == True:
                            for i in range(len(barco)):
                                #print(f"fila_{random_fila + i}, columna_{random_columna}")# print temporal para ver como se comporta el programa
                                self.matrix[random_fila + i][random_columna] = "O"
                            print(f"SUBMARINO, coord : {random_fila},{random_columna} : {random_orientacion} : ACEPTADA")
                        #else:
                            #print(f" coord : {random_fila},{random_columna} {random_orientacion} :intento NO VALIDO\n")  
                        
                    elif random_orientacion =="h":                  # modo horizontal
                        random_fila = random.randint(0,9)           
                        random_columna = random.randint(0,7)        # limito el randint para que en horizontal no se salga del tablero
                        barco_ok = chk_bar(self.matrix,random_fila, random_columna, "h", 3)
                        if barco_ok == True:
                            for i in range(len(barco)):
                                #print(f"fila_{random_fila}, columna_{random_columna + i}")# print temporal para ver como se comporta el programa
                                self.matrix[random_fila][random_columna + i] = "O"
                            print(f"SUBMARINO, coord : {random_fila},{random_columna} : {random_orientacion} : ACEPTADA")
                        #else:
                            #print(f" coord : {random_fila},{random_columna} {random_orientacion} :intento NO VALIDO\n")
            
           
            elif len(barco) == 2:
                '''ENTRADA DE LOS BARCOS DE 2 POSICIONES'''
                
                barco_ok = False    #inicio condicional del while, hasta no tener una posicion valida no saldrá
                while barco_ok == False:
                    
                    random_orientacion = random.choice(["v","h"])   # random de vertical (hacia abajo) u horizontal (hacia derecha) 

                    if random_orientacion == "v":                   # modo vertical
                        random_fila = random.randint(0,8)           # limito el randint para que en vertical no se salga del tablero
                        random_columna = random.randint(0,9) 
                        barco_ok = chk_bar(self.matrix,random_fila,random_columna, "v", 2)  
                        if barco_ok == True:
                            for i in range(len(barco)):
                                #print(f"fila_{random_fila + i}, columna_{random_columna}")# print temporal para ver como se comporta el programa
                                self.matrix[random_fila + i][random_columna] = "O"
                            print(f"DESTRUCTOR, coord : {random_fila},{random_columna} : {random_orientacion} : ACEPTADA")
                        #else:
                            #print(f" coord : {random_fila},{random_columna} {random_orientacion} :intento NO VALIDO\n")    
                        
                    elif random_orientacion =="h":                                           # modo horizontal
                        random_fila = random.randint(0,9)           
                        random_columna = random.randint(0,8)        # limito el randint para que en horizontal no se salga del tablero
                        barco_ok = chk_bar(self.matrix,random_fila, random_columna, "h", 2)
                        if barco_ok == True:
                            for i in range(len(barco)):
                                #print(f"fila_{random_fila}, columna_{random_columna + i}")# print temporal para ver como se comporta el programa
                                self.matrix[random_fila][random_columna + i] = "O"
                            print(f"DESTRUCTOR, coord : {random_fila},{random_columna} : {random_orientacion} : ACEPTADA")
                        #else:
                            #print(f" coord : {random_fila},{random_columna} {random_orientacion} :intento NO VALIDO\n")

            elif len(barco) == 1:
                '''ENTRADA DE LOS BARCOS DE 1 POSICION'''

                barco_ok = False
                while barco_ok == False:
                    
                    random_fila = random.randint(0,9)
                    random_columna = random.randint(0,9)
                    barco_ok = chk_bar(self.matrix,random_fila,random_columna,"v", 1)

                    if barco_ok == True:
                        #print(f"fila_{random_fila}, columna_{random_columna}") #print temporal para ver como se comporta el programa
                        self.matrix[random_fila][random_columna] = "O"
                        print(f"FRAGATA, coord : {random_fila},{random_columna} : ACEPTADA")
                    #else:
                        #print(f" coord : {random_fila},{random_columna} :intento NO VALIDO\n")
        print()    
        print(self.nombre_jug +" - " + self.tipo)
        print(f"{self.matrix}\n")
       
