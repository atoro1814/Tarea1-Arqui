import random

flag = True
# Construye el tablero segun el largo del pasillo que se ingrese
def construccionTablero(largoPasillo,tablero,cantidadGuardias,ultimaPosicion):
    for fila in tablero : 
        for columna in range(largoPasillo):
            fila.append("X");
    
    tablero[ultimaPosicion[0]][ultimaPosicion[1]] = "S"
    global flag

    if flag:
    
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
        flag = False
    

def generarPosicionObjetivo(tablero, largoPasillo):
    pos_columna_objetivo = random.randint(1, largoPasillo-1)
    tablero[10][pos_columna_objetivo] = "*"


def generarPosicionGuardias(tablero, cantidadGuardias):
    for i in range(cantidadGuardias):
        pos_fila = random.randint(0, 10)
        pos_columna = random.randint(0, largoPasillo-1)
        while tablero[pos_fila][pos_columna] == "S" or tablero[pos_fila][pos_columna] == "*":
            print ("Posicion Ocupada, vamos a generar una nueva posicion")
            pos_fila = random.randint(1, 11)
            pos_columna = random.randint(1, largoPasillo-1)

        tablero[pos_fila][pos_columna] = "!";

        print("La posicion del guardia ", i+1, " es: ", pos_columna + 1,",", pos_fila+ 1)



#Mover al jugador mas la actualizacion del tablero
def moverjugador(tablero, movimiento, cantidad, ultima_posicion):
    columna = ultima_posicion[1]
    fila = ultima_posicion[0]
    tablero[fila][columna] = "X" #actualiza la S a X 

    fila_valor = 0
    columna_valor = 0

    #hacia donde se movera
    if movimiento == "W":
        fila_valor = -1
    elif movimiento == "S":
        fila_valor = 1
    elif movimiento == "A":
        columna_valor = -1
    elif movimiento == "D":
        columna_valor = 1

    for _ in range(cantidad): #itera la cantidad de pasos que se ingreso
        fila += fila_valor
        columna += columna_valor

        if tablero[fila][columna] == "!":
            print("Has sido capturado por un guardia")
            print("La posicion actual del jugador es: ", columna + 1, ",", fila + 1)
            return 0
        elif tablero[fila][columna] == "*":
            print("Has llegado al objetivo, Iniciando hackeo")
            print("La posicion actual del jugador es: ", columna + 1, ",", fila + 1)
            return 1
        
    tablero[fila][columna] = "S" #actualizamos
    print("La posicion actual del jugador es: ", columna + 1, ",", fila + 1)
    ultimaPosicion[0] = fila #actualizamos
    ultimaPosicion[1] = columna #actualizamos
    print("La posicion actual del jugador es: !! ", ultimaPosicion[0] , ",", ultimaPosicion[1])
    print(tablero[ultimaPosicion[0]][ultimaPosicion[1]])
    
    

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
    
def verificarMovimiento(ultimaPosicion, accion, decimal):
    print("La cantidad de pasos a la ",movimiento(accion),"que vas a dar es: ", decimal)

    if decimal - ultimaPosicion[1] + 1 >  largoPasillo and accion == "D":
            
            raise ValueError("Error, la cantidad de pasos es mayor al largo del pasillo")
    elif decimal - ultimaPosicion[1] + 1 < 0 and accion == "A":
            
            raise ValueError("Error, la cantidad de pasos es mayor al largo del pasillo")
    elif decimal > 11 - ultimaPosicion[0] + 1 and accion == "S":
            
            raise ValueError("Error, la cantidad de pasos es mayor al largo del pasillo")
    elif decimal > 11 -  ultimaPosicion[0] + 1 < 0 and accion == "W":
            
            raise ValueError("Error, la cantidad de pasos es mayor al largo del pasillo")
    else:
        return True
    
    
    
def convertirMovimiento(accion,ultimaPosicion):
    try:
        if (largoPasillo < 20 ):
            print("Escribe la cantidad de pasos a ", movimiento(accion), " que quieres dar en formato binario: ")
            pasos = input()
            decimal = convertirBinario(pasos)
            verificarMovimiento(ultimaPosicion, accion, decimal)
            
            
            
        elif (largoPasillo > 20 and largoPasillo < 100):
            print("Escribe la cantidad de pasos a ", movimiento(accion), " que quieres dar en formato octal: ")
            pasos = input()
            decimal = convertirOctal(pasos)
            verificarMovimiento(ultimaPosicion, accion, decimal)
            
        elif (largoPasillo > 100):
            print("Escribe la cantidad de pasos a ", movimiento(accion), " que quieres dar en formato hexadecimal: ")
            pasos = input()
            convertirHexadecimal(pasos)
            decimal = convertirHexadecimal(pasos)
            verificarMovimiento(ultimaPosicion, accion, decimal)
        return decimal
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
            
    
    return decimal


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
    return octal


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
    return hexadecimal


#convierte de decimal a octal
def convertirDecimalOctal(numero):
    numero = int(numero)
    octal = ""
    while numero > 0:
        residuo = numero % 8
        numero = numero // 8
        octal += str(residuo)
    octal = int(octal[::-1])
    return octal


#convierte de decimal a binario
def convertirDecimalBinario(numero):
    num_binario = ""
    while numero > 0:
        if numero % 2 == 0:
            num_binario += '0'
        elif numero % 2 == 1:
            num_binario += '1'
        numero = numero // 2
    num_binario = int(num_binario[::-1])
    return num_binario


#convierte de decimal a hexade
def convertirDecimalHexadecimal(numero):
    diccionarioHexadecimal = {"10":"A", "11": "B", "12":"C","13":"D","14":"E","15":"F"}
    numero = int(numero)
    hexadecimal = ""
    while numero > 0:
        residuo = numero % 16
        numero = numero // 16
        if residuo > 9 :
            residuo = diccionarioHexadecimal[str(residuo)]
        hexadecimal += str(residuo)
    hexadecimal = hexadecimal[::-1]
    return hexadecimal


def numeroAleatorioHackeo (largoPasillo):
    

    if largoPasillo < 20:
        numero = random.randint(0, 20)
        
        numero = convertirDecimalBinario(numero)
    elif largoPasillo > 20 and largoPasillo < 100:
        numero = random.randint(0, 100)
        
        numero = convertirDecimalOctal(numero)
    elif largoPasillo > 100:
        numero = random.randint(0, 500)
        
        numero = convertirDecimalHexadecimal(numero)


    return numero

def hackeo(largoPasillo):
    print("Has ingresado a la ultima etapa del juego")
    numeroAleatorio = numeroAleatorioHackeo(largoPasillo)
    print("El numero que debes adivinar es: ", numeroAleatorio)

    respuesta = int(input("Ingresa el numero que crees que es: "))


    if largoPasillo < 20:
        if convertirDecimalBinario(respuesta) == numeroAleatorio:
            print("Has ganado")
        else:
            print("Has perdido")
    elif largoPasillo > 20 and largoPasillo < 100:
        if convertirDecimalOctal(respuesta) == numeroAleatorio:
            print("Has ganado")
        else:
            print("Has perdido")
    elif largoPasillo > 100:
        if convertirDecimalHexadecimal(respuesta) == numeroAleatorio:
            print("Has ganado")
        else:    
            print("Has perdido")    

#valida las opciones que se ingresan
def opciones_validas():
    opciones = ["W", "A", "S", "D", "Q"]
    while True:
        print("A jugar!")
        print("W: Arriba")
        print("A: Izquierda")
        print("S: Abajo")
        print("D: Derecha")
        print("Q: Salir")
        accion = input("Ingrese una direccion: ").strip()

        if accion in opciones:
            return accion
        else: 
            print("OPCION INVALIDA, INTENTE NUEVAMENTE!") 
            print("<---------------- ----------------->")
            



"""  
def actulizarposjugador(tablero,ultimaPosicion):
    for fila in range(len(tablero)):
        for columna in range(len(tablero[fila])):
            if tablero[fila][columna] == "S":
                ultimaPosicion[0] = fila
                ultimaPosicion[1] = columna
    print("La posicion actual del jugador es: !! ", ultimaPosicion[0] , ",", ultimaPosicion[1])
    return ultimaPosicion
"""  
    



bandera = input("Bienvenido al juego METAL GEAR SOLID 1010: BINARY SNAKE, presione S para comenzar: ")
ultimaPosicion = [5,0]

#generar tablero inicial 
#guardias y objetivo quedan en posiciones aleatorias y fijas!!


while bandera == "S":
    
        
    
    largoPasillo  = int(input("Ingrese el largo del pasillo: "))
    cantidadGuardias = int(input("Ingrese la cantidad de guardias: "))
    tablero = [[],
               [],
               [],
               [],
               [],
               [], 
               [],
               [],
               [],
               [],
               []]
    #ultimaPosicion = [5,0]
    

    print("Generando tablero...")
    construccionTablero(largoPasillo,tablero, cantidadGuardias,ultimaPosicion)
    mostrarTablero(tablero)

    
    accion = opciones_validas()
    if (accion == "Q"):
        print("Gracias por jugar!")
        break

    cantidad=convertirMovimiento(accion,ultimaPosicion)
    opcion = moverjugador(tablero, accion,cantidad , ultimaPosicion)
    if opcion == 1:
        hackeo(largoPasillo)
    elif opcion == 0:
        print("Has perdido")
        break
    
    mostrarTablero(tablero)
    

    




#hackeo(120)
   




    



    

    
   



    

    