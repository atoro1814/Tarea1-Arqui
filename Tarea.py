largoPasillo  = int(input("Ingrese el largo del pasillo: "))
cantidadGuardias = input("Ingrese la cantidad de guardias: ")
tablero = []

print("El largo del pasillo es: ", largoPasillo)
print("La cantidad de guardias es: ", cantidadGuardias)

def construccionTablero(largoPasillo,tablero):
    
    for i in range(largoPasillo):
        tablero.append(["X","X","X","X","X","X","X","X","X","X","X"])
    
    return tablero

def mostrarTablero(tablero):
    for fila in tablero:
        for elemento in fila:
            print(elemento, end="")
        print("\n")


print(construccionTablero(largoPasillo,tablero))
print(mostrarTablero(tablero))