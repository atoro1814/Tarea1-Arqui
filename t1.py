import random


# Construye el tablero segun el largo del pasillo que se ingrese
def construccionTablero(largoPasillo,tablero,cantidadGuardias,ultimaPosicion):
    for fila in tablero : 
        for columna in range(largoPasillo):
            fila.append("X");
    
    tablero[5][0] = "S"
    
    pos_columna_objetivo = random.randint(1, largoPasillo-1)
    tablero[10][pos_columna_objetivo] = "*"

    for i in range(cantidadGuardias):
        pos_fila = random.randint(0, 10)
        pos_columna = random.randint(0, largoPasillo-1)
        while tablero[pos_fila][pos_columna] == "S" or tablero[pos_fila][pos_columna] == "*":
            print ("Posicion Ocupada, vamos a generar una nueva posicion")
            pos_fila = random.randint(1, 11)
            pos_columna = random.randint(1, largoPasillo-1)

        tablero[pos_fila][pos_columna] = "!";

        print("La posicion del guardia ", i+1, " es: ", pos_columna + 1,",", pos_fila+ 1)

    
# Muestra el tablero por consola ya con los valores ingresados
def mostrarTablero(tablero):
    for fila in tablero:
        for elemento in fila:
            print(elemento, end=" ")
        print()
        

# Retorna la direccion en la que se mueve el jugador
def movimiento(accion):
    if accion == "W":
        return "arriba"
    elif accion == "A":
        return "izquierda"
    elif accion == "S":
        return "abajo"
    elif accion == "D":
        return "derecha"
    else:
        return "error"
    
def convertirMovimiento(accion):
    try:
        if (largoPasillo < 20 ):
            print("Escribe la cantidad de pasos a ", movimiento(accion), " que quieres dar en formato binario: ")
            pasos = input()
            convertirBinario(pasos)
            
        elif (largoPasillo > 20 and largoPasillo < 100):
            print("Escribe la cantidad de pasos a ", movimiento(accion), " que quieres dar en formato octal: ")
            pasos = input()
            convertirOctal(pasos)
        elif (largoPasillo > 100):
            print("Escribe la cantidad de pasos a ", movimiento(accion), " que quieres dar en formato hexadecimal: ")
            pasos = input()
            convertirHexadecimal(pasos)
    except ValueError as e:
        print(e)
        convertirMovimiento(accion)


#binario usa 1 o 0
def convertirBinario(numero): 
    numero = numero[::-1]
    contador = 0
    decimal = 0
    for i in numero:
        if i == "0" or i == "1":
            
            decimal += int(i) * 2 ** contador
            contador += 1
        else:
            raise ValueError("Error, no es un numero binario")
            
    print("El numero en decimal es: ", decimal)


#octal usa numero del 0 al 7 
def convertirOctal(numero):
    numero = numero[::-1]
    contador = 0
    octal = 0
    for i in numero:
        if i.isdigit() and 0 <= int(i) <= 7:
            octal += int(i) * (8 ** contador)
            contador += 1
        else:
            raise ValueError("Error, no es un numero octal")
    print("El numero octal es: ", octal)


#usa del 0 al 9, A B C D E F
def convertirHexadecimal(numero): 
    numero = numero[::-1]
    diccionarioHexadecimal = {"1":1,"2":2 ,"3" :3, "4" :4, "5" : 5 , "6" :6 , "7":7 , "8" :8, "9" :9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    contador = 0
    hexadecimal = 0
    for i in numero:
        if i in diccionarioHexadecimal:
            hexadecimal += diccionarioHexadecimal[i] * (16 ** contador)
            contador += 1
        else: 
            raise ValueError("Error, no es un numero Hexadecimal")
    print("El numero hexadecimal es: ", hexadecimal)


bandera = input("Bienvenido al juego METAL GEAR SOLID 1010: BINARY SNAKE, presione S para comenzar: ")

while bandera == "S":
    
    largoPasillo  = int(input("Ingrese el largo del pasillo: "))
    cantidadGuardias = int(input("Ingrese la cantidad de guardias: "))
    tablero = [[],[],[],[],[],[],[],[],[],[],[]]
    ultimaPosicion = [5,0]

    print("Generando tablero...")
    construccionTablero(largoPasillo,tablero, cantidadGuardias,ultimaPosicion)
    
    mostrarTablero(tablero)
    print("A jugar!")
    print("W: Arriba")
    print("A: Izquierda")
    print("S: Abajo")
    print("D: Derecha")
    print("Q: Salir")
    accion = input("Ingrese una direccion: ")
    
    if (accion == "Q"):
        print("Gracias por jugar!")
        break

    convertirMovimiento(accion)

    

    
   



    

    