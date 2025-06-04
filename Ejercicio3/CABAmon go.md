# Para resolver este problema, vamos a usar pilas (LIFO)
TIPO Carta:
  nombre: cadena,
  velocidad: entero,
  fuerza: entero,
  elemento: cadena,
  peso: entero,
  altura: entero

TIPO Nodo:
  carta: Carta
  siguiente: Nodo

TIPO Mazo: Nodo

TIPO Jugador:
  nombre: cadena,
  mazo: Mazo,
  puntaje: entero

TIPO Descarte:
  mazo: Mazo

# Definimos algunas variables

ENTERO tamanio_mazo = 250
LISTA elementos = ["agua","fuego","aire","tierra","electricidad"]
LISTA atributos = ["velocidad", "fuerza", "peso", "altura"]
mazo_total = None
ENTERO num_ronda = 1 
BOOLEANO juego_terminado = FALSO
# El enunciado pide máximo 250 rondas o hasta que un jugador se quede sin cartas 
ENTERO max_ronda = 250
ENTERO modo_juego = 1
ENTERO turno = 1

# Vamos a ejecutar paso a paso el juego

# Función para iniciar el menú del juego:

FUNCION menu_principal():
  LIMPIAR_PANTALLA  # Simula un cls
  MIENTRAS True
    IMPRIMIR "CABAMon Go!"
    IMPRIMIR "-----------------------------------------------------"
    IMPRIMIR "Elegí el modo de juego:"
    IMPRIMIR "1. PC vs PC"
    IMPRIMIR "2. Jugador vs PC"
    IMPRIMIR "3. Jugador vs Jugador"
    IMPRIMIR "-----------------------------------------------------"
    opcion = ESPERAR_ENTRADA()
    SI opcion == 1 OR opcion == 2 OR opcion == 3
      ENTONCES RETORNAR opcion 
    SINO
      ENTONCES IMPRIMIR("Tenés que elegir una opción válida.")
    FIN SI
  FIN MIENTRAS
FIN FUNCION


# Armar, mezclar, y repartir el mazo entre cada jugador
FUNCION armar_mazo():
  mazo_total = None
  PARA i = 1 HASTA tamanio_mazo:
    carta = Carta()
    carta.nombre="monstruito_"+CADENA(i)
    carta.velocidad=ALEATORIO(1,10)
    carta.fuerza=ALEATORIO(1,10)
    carta.elemento=ALEATORIO(elementos)
    carta.peso=ALEATORIO(1,10)
    carta.altura=ALEATORIO(1,10)

    nodo_nuevo = Nodo()
    nodo_nuevo.carta = carta

    # Reemplazamos el puntero para que esté en la cima de la pila
    nodo_nuevo.siguiente = mazo_total
    mazo_total = nodo_nuevo
    RETORNAR mazo_total
FIN FUNCION

FUNCION mezclar_mazo(mazo) : Mazo
  LISTA cartas = []
  Nodo actual = mazo
  MIENTRAS actual != NULO:
    AGREGAR actual.carta A cartas
    actual = actual.siguiente
  FINMIENTRAS
  MEZCLAR cartas  # Esto es el equivalente a shuffle en Python
  Mazo nuevo_mazo = NULO
  PARA cada carta EN cartas:
    Nodo nodo = Nodo()
    nodo.carta = carta
    nodo.siguiente = nuevo_mazo
    nuevo_mazo = nodo
  FINPARA
  RETORNAR nuevo_mazo
FIN FUNCION

FUNCION repartir_mazo(mazo_total, jugador_1, jugador_2):
  turno_jugador = 1
  MIENTRAS mazo_total != None:
    Nodo nodo_actual = Nodo()
    nodo_actual.carta = mazo_total.carta
    mazo_total = mazo_total.siguiente

    SI turno_jugador == 1:
      # Explicación de este paso más abajo
      nodo_actual.siguiente = jugador_1.mazo
      jugador_1.mazo = nodo_actual
      turno_jugador = 2
    SINO
      nodo_actual.siguiente = jugador_2.mazo
      jugador_2.mazo = nodo_actual
      turno_jugador = 1
    FIN SI
  FINMIENTRAS
FIN FUNCION

# Función para apilar las cartas
FUNCION apilar_al_fondo(mazo, nodo_nuevo) : Mazo
  SI mazo == NULO:
    RETORNAR nodo_nuevo
  SINO
    Nodo actual = mazo
    MIENTRAS actual.siguiente != NULO:
      actual = actual.siguiente
    FINMIENTRAS
    actual.siguiente = nodo_nuevo
    RETORNAR mazo
  FINSI
FIN FUNCION

# Esta función se encarga de decidir qué elemento gana en cada carta:
FUNCION comparar_elementos(carta_1, carta_2): ENTERO
  # Este segmento del código es mejorable. Por simplicidad, lo implemento así, pero en
  # una situación real usaría un diccionario (Python) o a más bajo nivel crearía una
  # estructura de datos que contengan "elementos" y "ventajas", y haría una lista de
  # esa estructura o tipo de dato propio.

  ENTERO ganador = 0
  SI carta_1.elemento == 'agua' Y carta_2.elemento == 'fuego'
    ENTONCES ganador = 1
  SINO Y SI carta_1.elemento == 'fuego' Y carta_2.elemento == 'agua'
    ENTONCES ganador = 2
  SINO Y SI carta_1.elemento == 'electricidad' Y carta_2.elemento == 'agua'
    ENTONCES ganador = 1
  SINO Y SI carta_1.elemento == 'agua' Y carta_2.elemento == 'electricidad'
    ENTONCES ganador = 2
  # En esta instancia podemos definir el resto de la lógica que queramos, por practicidad corto acá.
  REGRESAR ganador
FIN FUNCION

# Función para mostrar los resultados de las rondas y el juego en pantalla
FUNCION mostrar_estado(j1, j2, carta_j1, carta_j2, atributo, valor_j1, valor_j2, num_ronda, ganador):
  LIMPIAR_PANTALLA  # Simula os.system('cls' o 'clear')
  IMPRIMIR "Ronda ", num_ronda, " - Atributo elegido: ", MAYUSCULAS(atributo)
  IMPRIMIR "-----------------------------------------------------"
  IMPRIMIR j1.nombre, " - Puntaje acumulado: ", j1.puntaje
  IMPRIMIR "Carta: ", carta_j1.nombre, " | Vel: ", carta_j1.velocidad, " | Fue: ", carta_j1.fuerza, " | Elem: ", carta_j1.elemento, " | Pes: ", carta_j1.peso, " | Alt: ", carta_j1.altura
  IMPRIMIR "Valor: ", valor_j1
  IMPRIMIR "-----------------------------------------------------"
  IMPRIMIR j2.nombre, " - Puntaje acumulado: ", j2.puntaje
  IMPRIMIR "Carta: ", carta_j2.nombre, " | Vel: ", carta_j2.velocidad, " | Fue: ", carta_j2.fuerza, " | Elem: ", carta_j2.elemento, " | Pes: ", carta_j2.peso, " | Alt: ", carta_j2.altura
  IMPRIMIR "Valor: ", valor_j2
  IMPRIMIR "-----------------------------------------------------"
  SI ganador != None
    ENTONCES IMPRIMIR "Ganó el jugador {ganador}!"
  SINO
    ENTONCES IMPRIMIR "Empate! Las cartas van al descarte..."
  ESPERAR_ENTRADA("Presioná ENTER para continuar...")
FIN FUNCION

# Esta función se encarga de elegir el atributo, el jugador humano o la PC automáticamente
FUNCION elegir_atributo(turno, modo_juego): CADENA
    LIMPIAR_PANTALLA() # cls
    SI modo_juego == 1 O (modo_juego == 2 Y turno==2):
      ENTONCES
        atributo = ALEATORIO(ATRIBUTOS)
        IMPRIMIR("PC {turno} elige el atributo")
        IMPRIMIR("Presioná ENTER para continuar...")
        ENTRADA()
        RETORNAR atributo
    SINO Y SI (modo_juego == 2 and turno==1) O modo_juego == 3:
        MIENTRAS True:
            IMPRIMIR("Jugador {turno} elige un atributo:")
            PARA i, atributo EN ENUMERAR(ATRIBUTOS, comenznado=1):
                IMPRIMIR(i, MAYUSCULAS(atributo))
            FIN PARA
            opcion = ENTRADA("Seleccioná el número del atributo: ")
            SI ES_DIGITO(opcion) Y 1 <= opcion <= LONGITUD(ATRIBUTOS):
                RETORNAR ATRIBUTOS[int(opcion) - 1]
            SINO:
                IMPRIMIR("Opción inválida. Por favor, elegí un número válido.")
            FIN SI
        FIN MIENTRAS
    FIN SI
FIN FUNCION

# Función para calcular la ronda
FUNCION ronda(jugador_1, jugador_2, descarte, modo_juego, turno):
  atributo_elegido = elegir_atributo(turno, modo_juego)

  carta_j1 = jugador_1.mazo.carta
  carta_j2 = jugador_2.mazo.carta

  valor_j1 = carta_j1[atributo_elegido]
  valor_j2 = carta_j2[atributo_elegido]

  ENTERO elemento_ganador = 0 
  
  # Calculamos si hay un bonus por el elemento
  elemento_ganador = comparar_elementos(carta_j1, carta_j2)
  SI elemento_ganador == 1
    ENTONCES valor_j1 = valor_j1 + 1
  SINO Y SI elemento_ganador == 2
    ENTONCES valor_j2 = valor_j2 + 1
  FIN SI
  # En caso de que sea 0, los elementos son neutros

  # Desapilamos

  jugador_1.mazo = jugador_1.mazo.siguiente
  jugador_2.mazo = jugador_2.mazo.siguiente

  # Si J1 gana:
  SI valor_j1 > valor_j2:
    # Sumamos puntaje
    jugador_1.puntaje = jugador_1.puntaje + 1
    # Creamos los nodos para ambas cartas
    nodo1 = Nodo()
    nodo1.carta = carta_j1
    nodo1.siguiente = NULO

    nodo2 = Nodo()
    nodo2.carta = carta_j2
    nodo2.siguiente = nodo1

  # Apilar la última carta en el fondo
    jugador_1.mazo = apilar_al_fondo(jugador_1.mazo, nodo2)

  # Si hay cartas acumuladas en el descarte, dárselas también al ganador
    MIENTRAS descarte.mazo != NULO:
      Nodo nodo_desc = descarte.mazo
      descarte.mazo = descarte.mazo.siguiente
      nodo_desc.siguiente = NULO
      jugador_1.mazo = apilar_al_fondo(jugador_1.mazo, nodo_desc)
    FINMIENTRAS

    mostrar_estado(jugador_1, jugador_2, carta_j1, carta_j2, atributo_elegido, valor_j1, valor_j2, num_ronda,j1)

  # Lo mismo para J2
  SINO SI valor_j2 > valor_j1:
    jugador_2.puntaje = jugador_2.puntaje + 1
    nodo1 = Nodo()
    nodo1.carta = carta_j1
    nodo1.siguiente = NULO

    nodo2 = Nodo()
    nodo2.carta = carta_j2
    nodo2.siguiente = nodo1

    jugador_2.mazo = apilar_al_fondo(jugador_2.mazo, nodo2)

  # Si hay cartas acumuladas en el descarte, dárselas también al ganador
    MIENTRAS descarte.mazo != NULO:
      Nodo nodo_desc = descarte.mazo
      descarte.mazo = descarte.mazo.siguiente
      nodo_desc.siguiente = NULO
      jugador_1.mazo = apilar_al_fondo(jugador_1.mazo, nodo_desc)
    FINMIENTRAS

    mostrar_estado(jugador_1, jugador_2, carta_j1, carta_j2, atributo_elegido, valor_j1, valor_j2, num_ronda,None)

  #Si es empate, al descarte:
  SINO:
    nodo1 = Nodo()
    nodo1.carta = carta_j1
    nodo1.siguiente = descarte.mazo
    descarte.mazo = nodo1

    nodo2 = Nodo()
    nodo2.carta = carta_j2
    nodo2.siguiente = descarte.mazo
    descarte.mazo = nodo2
  FIN SI
FIN FUNCION

# Mostramos el menú inicial
modo_juego = menu_principal()

jugador_1 = Jugador()
jugador_1.nombre = "Jugador 1"
jugador_2 = Jugador()
jugador_2.nombre = "Jugador 2"
descarte = Descarte()

# Bucle principal del programa
MIENTRAS juego_terminado==Falso:
  SI jugador_1.mazo == NULO O jugador_2.mazo == NULO O num_ronda>max_ronda:
    juego_terminado=True
  SINO:
    ronda(jugador_1, jugador_2, descarte, modo_juego, turno)
    num_ronda = num_ronda + 1
    SI turno == 1
      ENTONCES turno = 2
    SINO turno = 1
    FIN SI
  FIN SI
FIN MIENTRAS
