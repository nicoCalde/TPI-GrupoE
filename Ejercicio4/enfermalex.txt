INICIO

// Paso 1: Inicialización
colores ← ["rojo", "verde", "azul", "amarillo", "naranja", "violeta", "blanco", "negro", "celeste", "marron"]
medidas ← lista vacía

// Crear 3 medidas por cada color
PARA cada color EN colores
    REPETIR 3 VECES
        AGREGAR color A medidas
    FIN REPETIR
FIN PARA

// Mezclar aleatoriamente las medidas
mezclar(medidas)

// Crear 10 tubos vacíos (pilas con capacidad máxima de 4)
tubos ← lista vacía
PARA i DESDE 0 HASTA 9
    tubos[i] ← PILA VACÍA
FIN PARA

// Distribuir aleatoriamente las 30 medidas en los tubos (respetando el máximo de 4)
PARA cada medida EN medidas
    REPETIR
        indice ← número aleatorio entre 0 y 9
        SI LONGITUD(tubos[indice]) < 4 ENTONCES
            PUSH(medida, tubos[indice])
            SALIR DEL REPETIR
        FIN SI
    HASTA QUE se haya colocado la medida
FIN PARA

// Paso 2: Bucle principal del juego
REPETIR
    // Mostrar estado actual
    MOSTRAR "=== Estado actual de los tubos ==="
    PARA i DESDE 0 HASTA 9
        MOSTRAR "Tubo ", i, ": ", tubos[i]
    FIN PARA

    SI finDelJuego(tubos) ENTONCES
        MOSTRAR "¡Juego completado con éxito!"
        SALIR
    FIN SI

    MOSTRAR "Ingrese el número del tubo origen (0 a 9):"
    LEER origen

    SI tubos[origen] ESTÁ VACÍO ENTONCES
        MOSTRAR "Ese tubo está vacío. Intentá con otro."
        CONTINUAR
    FIN SI

    elemento ← POP(tubos[origen])

    MOSTRAR "Ingrese el número del tubo destino (0 a 9):"
    LEER destino

    SI LONGITUD(tubos[destino]) = 4 ENTONCES
        MOSTRAR "El tubo destino está lleno. Movimiento cancelado."
        PUSH(elemento, tubos[origen])  // Deshacer
        CONTINUAR
    FIN SI

    PUSH(elemento, tubos[destino])
    MOSTRAR "Movimiento realizado."

HASTA QUE finDelJuego(tubos)

FIN


// FUNCION: Validación del estado final del juego
FUNCION finDelJuego(tubos):
    contadorTubosCompletos ← 0

    PARA cada tubo EN tubos
        // Debe tener exactamente 3 medidas
        SI LONGITUD(tubo) ≠ 3 ENTONCES
            RETORNAR FALSO

        // Deben ser todas del mismo color
        colorBase ← tubo[0]
        PARA cada color EN tubo
            SI color ≠ colorBase ENTONCES
                RETORNAR FALSO
        FIN PARA

        contadorTubosCompletos ← contadorTubosCompletos + 1
    FIN PARA

    SI contadorTubosCompletos = 10 ENTONCES
        RETORNAR VERDADERO
    SINO
        RETORNAR FALSO
