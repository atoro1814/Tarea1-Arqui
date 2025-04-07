#INTEGRANTES
Nombre: Bárbara Camilo Gonzalez
Rol: 202304567-5
Parelelo: 201

Nombre: Alexander Toro Astudillo
Rol: 202304647-7
Paralelo: 201

#Especificación de algoritmos y desarrollo realizado 

convertirBinario, convertirOctal, convertirHexadecimal; Estas funciones están diseñadas para convertir números desde sus respectivas bases (binario, octal y hexadecimal)
a su equivalente en base decimal. Además, incluyen validaciones para asegurarse de que el número ingresado sea válido según la base correspondiente.

convertirDecimalBinario, convertirDecimalOctal, convertirDecimalHexadecimal; Estas 3 funciones están diseñadas para convertir un numero decimal en una de las base(Binario, octal o hexadecimal)
Cada función utiliza un p#INTEGRANTES
Nombre: Bárbara Camilo Gonzalez
Rol: 202304567-5
Parelelo: 201

Nombre: Alexander Toro Astudillo
Rol: 202304647-7
Paralelo: 201

#Especificación de algoritmos y desarrollo realizado 

convertirBinario, convertirOctal, convertirHexadecimal; Estas funciones están diseñadas para convertir números desde sus respectivas bases (binario, octal y hexadecimal)
a su equivalente en base decimal. Además, incluyen validaciones para asegurarse de que el número ingresado sea válido según la base correspondiente.

convertirDecimalBinario, convertirDecimalOctal, convertirDecimalHexadecimal; Estas 3 funciones están diseñadas para convertir un numero decimal en una de las base(Binario, octal o hexadecimal)
Cada función utiliza un proceso iterativo basado en divisiones sucesivas por la base correspondiente (2 para binario, 8 para octal y 16 para hexadecimal). Los residuos obtenidos en cada paso se concatenan para formar el número resultante en la nueva base.

construccionTablero; Esta funcion crea el tablero base del juego, llenandolo con 'X', según el largo que el jugador quiera. Se inicia la posicion del jugador en [0,5], se genera aleatoriamente la posicion del objetivo,
además con la cantidad de guardias entregada por el jugador, se generan las posiciones de estos aleatoriamente verificandose que estos no ocupen el lugar del jugador, objetivo u otro guardia

mostrarTablero; Esta función muestra el tablero actual, la ubicacion de los guardias, objetivo y del jugador 

moverjugador; Esta funcion toma la cantidad de espacios y hacia donde se quiere mover el jugador, actualizando su posicion dentro del tablero

opciones_validas; La función muestra un menú con las opciones disponibles y solicita al jugador que ingrese una dirección. Si el input no corresponde a ninguna de las opciones válidas, se notifica al jugador y se le pide que intente nuevamente. 
Esto asegura que solo se acepten movimientos o acciones permitidas por el juego.

movimiento; Esta funcion retorna el nombre del movimiento que hara el jugador 

verificacionMovimiento; Esta función verifica que el jugador realice un movimiento válido dentro del tablero, asegurándose de que no se salga de los límites establecidos. 
Además, valida que la cantidad de pasos ingresada por el jugador sea coherente con las dimensiones del tablero y la dirección del movimiento

ConvertirMovimiento; Esta función convierte la cantidad de pasos ingresada por el jugador en el sistema numérico correspondiente según el tamaño del tablero 

NumeroAleatorioHackeo; Esta función genera un número aleatorio en la base correspondiente al tamaño del tablero actual (binario, octal o hexadecimal)

Hackeo; Esta función es donde se realiza la fase de hackeo, donde toma el numero aleatorio generado segun el tamaño del tablero, para que el jugador convierta ese numero en decimal y determinar si gana o pierde

#Supuestos utilizados 
Suponemos que el jugador no ingresará una cantidad excesiva o irracional de guardias dentro del tablero, ya que esto podría generar problemas en la generación de posiciones aleatorias. 
Además, un número desmedido de guardias comprometería la jugabilidad al hacer prácticamente imposible moverse sin perder inmediatamente.

#Consideraciones adicionales (como ejecutar el programa)
paso 1: Abrir una terminal en la carpeta donde se ubica el archivo
paso 2: Escribir en la terminal lo siguiente
            python3 t1.py
Listo, Disfruta del juego!!a funcion crea el tablero base del juego, llenandolo con 'X', según el largo que el jugador quiera. Se inicia la posicion del jugador en [0,5], se genera aleatoriamente la posicion del objetivo,
además con la cantidad de guardias entregada por el jugador, se generan las posiciones de estos aleatoriamente verificandose que estos no ocupen el lugar del jugador, objetivo u otro guardia

mostrarTablero; Esta función muestra el tablero actual, la ubicacion de los guardias, objetivo y del jugador 

moverjugador; Esta funcion toma la cantidad de espacios y hacia donde se quiere mover el jugador, actualizando su posicion dentro del tablero

opciones_validas; La función muestra un menú con las opciones disponibles y solicita al jugador que ingrese una dirección. Si el input no corresponde a ninguna de las opciones válidas, se notifica al jugador y se le pide que intente nuevamente. 
Esto asegura que solo se acepten movimientos o acciones permitidas por el juego.

movimiento; Esta funcion retorna el nombre del movimiento que hara el jugador 

verificacionMovimiento; Esta función verifica que el jugador realice un movimiento válido dentro del tablero, asegurándose de que no se salga de los límites establecidos. 
Además, valida que la cantidad de pasos ingresada por el jugador sea coherente con las dimensiones del tablero y la dirección del movimiento

ConvertirMovimiento; Esta función convierte la cantidad de pasos ingresada por el jugador en el sistema numérico correspondiente según el tamaño del tablero 

NumeroAleatorioHackeo; Esta función genera un número aleatorio en la base correspondiente al tamaño del tablero actual (binario, octal o hexadecimal)

Hackeo; Esta función es donde se realiza la fase de hackeo, donde toma el numero aleatorio generado segun el tamaño del tablero, para que el jugador convierta ese numero en decimal y determinar si gana o pierde

#Supuestos utilizados 
Suponemos que el jugador no ingresará una cantidad excesiva o irracional de guardias dentro del tablero, ya que esto podría generar problemas en la generación de posiciones aleatorias. 
Además, un número desmedido de guardias comprometería la jugabilidad al hacer prácticamente imposible moverse sin perder inmediatamente.

#Consideraciones adicionales (como ejecutar el programa)
paso 1: Abrir una terminal en la carpeta donde se ubica el archivo
paso 2: Escribir en la terminal lo siguiente
            python3 t1.py
Listo, Disfruta del juego!!