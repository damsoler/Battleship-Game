from os import system
import sys, time, random
import hf_variables


########################################
############# BIENVENIDA ###############
########################################


def texto_vintage(texto):
	for letra in texto:
		sys.stdout.write(letra)
		sys.stdout.flush()
		time.sleep(0.000025)	


def intro():
	texto_vintage(hf_variables.mensaje)
	time.sleep(1.5)
	print(f"Bienvenido a la {hf_variables.nombre_juego}!!!")
    

def clear():
    _ = system('cls')


def set_jugador():
	nombre_jugador = (input("\n\nIndique su nombre por favor:\n")).title()
	print(f"Es un gusto tenerlo aquí Capitán {nombre_jugador}.")
	return nombre_jugador


def set_dificultad():
	dificultad = input(f"indique un nivel de difucultad para el juego, (FACIL - 1 | MEDIO - 2 | DIFICIL - 3\nUsted Ha seleccionado: ")
	return dificultad


def chequear_coords_ady(matrix, indice, fila, columna, orientacion):
	if orientacion == "v":
		control_indice = (-1, 0)
	else:
		control_indice = (0, -1)
	for i in range(-1, 2):
		for j in range(-1, 2):
			if ((fila + i) <0) or ((fila + i) >9) or ((columna + j) < 0) or ((columna + j) > 9):
				continue
			else:
				if matrix[fila + i][columna + j] == "O":
					if (i == control_indice[0]) and (j == control_indice[1]) and (indice != 0):
						pass
					else:
						return False
	return True


def chequear_input_coord(texto, limite_superior):
	while True:
		coord_input = input(f"\nIndique la {texto} (ingrese un número entre 0 y {limite_superior}): ")
		try:
			if (int(coord_input) > -1) and (int(coord_input) <= limite_superior):
				return int(coord_input)
			else:
				print(f"El input '{coord_input}' ingresado no es válido.")
		except:
			print(f"El input '{coord_input}' ingresado no es válido.")


def chequear_disparos_anteriores(matriz, jugador_pc):
	while True:
		if jugador_pc == True:
			disparo_fila = random.randint(0, 9)
			disparo_columna = random.randint(0, 9)
		else:
			disparo_fila = chequear_input_coord("fila donde caerá su disparo", 9)
			disparo_columna = chequear_input_coord("columna donde caerá su disparo", 9)
		if (matriz[disparo_fila][disparo_columna] != "X") and (matriz[disparo_fila][disparo_columna] != "-"):
			return disparo_fila, disparo_columna
		elif jugador_pc != True:
			print(f"Ya habías elegido las coordenadas [{disparo_fila},{disparo_columna}] en otra ocasión.")
			print("Vuelve a intentarlo con otras coordenadas.\n")

#############################################
### checker choche y adjacentes de barcos ###
#############################################


def adj_finder(matrix, position): # Devuelve un listado de coordenadas adjacentes a una posicion
	
    adj = []
    
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            rangeX = range(0, matrix.shape[0])  # X bounds
            rangeY = range(0, matrix.shape[1])  # Y bounds
            
            (newX, newY) = (position[0]+dx, position[1]+dy)  # adjacent cell
            
            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adj.append((newX, newY))
    return adj


def chk_bar(matrix, fila, columna, orientacion, tamaño):
	if (matrix[fila][columna]!= "O"): # verifico que no haya un barco en esa posicion
		if orientacion == "v": # vertical
			adj2 = []
			for p in range(tamaño):
				adj2 += adj_finder((matrix),(fila + p , columna))
			#print (f"adjacents: {adj2}") # lista de adjacentes de todas las posiciones 
			
			for elemento in adj2:
				if matrix[elemento[0]][elemento[1]] == "O": #verifico que no haya barco en las posiciones adjacentes 
					return False
			return True

		elif orientacion == "h": # horizontal
			adj2 = []
			for p in range(tamaño):
				adj2 += adj_finder((matrix),(fila , columna + p))
			#print (f"adjacents: {adj2}") # lista de adjacentes de todas las posiciones 
			
			for elemento in adj2:
				if matrix[elemento[0]][elemento[1]] == "O": #verifico que no haya barco en las posiciones adjacentes 
					return False
			return True
	else:
		#print(" Ya se encuentra un barco aqui - NO VALIDO")
		return False
		

########################################
### checker para barcos de 1 posicion###
############# no utilizado #############
		
# def chk_bar_1(matrix, fila, columna, tamaño):
# 	adj1 = adj_finder(matrix,(fila,columna))
# 	if (matrix[fila][columna]!= "O"): # verifico que no haya un barco en esa posicion
# 		print(adj1)
# 		for elemento in adj1:
# 			if matrix[elemento[0]][elemento[1]] == "O": #verifico que no haya barco en las posiciones adjacentes 
# 				return False
# 		return True
# 	else:
# 		print(" Ya se encuentra un barco aqui - NO VALIDO")
# 		return False

