INICIO

// Paso 1: Declaración de estructuras de datos
nota ← "Game Over"  // texto de la nota
letrasNota ← LISTA VACÍA  // lista para almacenar las letras de la nota

// Paso 2: Cargar letras de la nota en la lista
PARA i DESDE 0 HASTA longitud(nota) - 1
    SI nota[i] ≠ " " ENTONCES  // ignorar espacios
        AGREGAR nota[i] A letrasNota
    FIN SI
FIN PARA

// Paso 3: Declarar una cola para almacenar las revistas procesadas
colaRevistas ← COLA VACÍA

// Paso 4: Supongamos que tenemos una lista de revistas (nombre, lista de páginas)
revistas ← lista de revistas con páginas
// Cada página contiene letras y su posición, por ejemplo:
// revistas = [
//     {nombre: "Revista A", paginas: [página 1, página 2, ...]},
//     ...
// ]

// Paso 5: Identificar de qué revista y página salió cada letra
// Creamos una lista para almacenar resultados
resultados ← LISTA VACÍA

PARA cada letra EN letrasNota
    encontrado ← FALSO
    ENCOLAR todas las revistas EN colaRevistas  // procesamos las revistas como una cola
    MIENTRAS colaRevistas NO ESTÉ VACÍA Y encontrado = FALSO
        revista ← DESENCOLAR(colaRevistas)
        PARA cada página EN revista.paginas
            SI letra ESTÁ EN página ENTONCES
                AGREGAR (letra, revista.nombre, página.numero) A resultados
                encontrado ← VERDADERO
                SALIR DEL BUCLE DE PÁGINA
            FIN SI
        FIN PARA
    FIN MIENTRAS

    SI encontrado = FALSO ENTONCES
        MOSTRAR "No se encontró la letra ", letra
    FIN SI
FIN PARA

// Paso 6: Mostrar resultados
PARA cada resultado EN resultados
    MOSTRAR "Letra: ", resultado.letra, 
            " Revista: ", resultado.revista, 
            " Página: ", resultado.pagina
FIN PARA

// Paso 7: Filtrar sospechosos por historial de ventas
// historialVentas es una lista con registros de compras (revista, comprador)
sospechosos ← lista de TODOS los compradores del historial de ventas

// Para cada revista detectada en la nota:
PARA cada resultado EN resultados
    revistaActual ← resultado.revista
    // Filtrar sospechosos: solo los que compraron esta revista
    sospechosos ← lista de sospechosos QUE hayan comprado revistaActual
    // Si no queda ninguno, se interrumpe la búsqueda
    SI sospechosos ESTÁ VACÍA ENTONCES
        SALIR DEL BUCLE
    FIN SI
FIN PARA

// Paso 8: Mostrar lista de sospechosos
SI sospechosos NO ESTÁ VACÍA ENTONCES
    MOSTRAR "Posibles sospechosos: "
    MOSTRAR sospechosos
SINO
    MOSTRAR "No se encontraron sospechosos."
FIN SI

FIN
