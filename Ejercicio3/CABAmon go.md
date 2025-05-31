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
  mazo: Mazo

TIPO Descarte:
  mazo: Mazo

# Definimos algunas variables

ENTERO tamanio_mazo = 250
LISTA elementos = ["agua","fuego","aire","tierra","electricidad"]
LISTA atributos = ["velocidad", "fuerza", "peso", "altura"]
mazo_total = None
ENTERO num_ronda = 1 
BOOLEANO juego_terminado = FALSO

# Vamos a ejecutar paso a paso el juego

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
FINFUNCION

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
      FINSI
  FINMIENTRAS
FINFUNCION

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
FINFUNCION

# Función para mostrar los resultados de las rondas y el juego en pantalla

FUNCION mostrar_estado(j1, j2, carta_j1, carta_j2, atributo, valor_j1, valor_j2, num_ronda):
  LIMPIAR_PANTALLA  # Simula os.system('cls' o 'clear')

  IMPRIMIR "Ronda ", num_ronda, " - Atributo elegido: ", MAYUSCULAS(atributo)
  IMPRIMIR "-----------------------------------------------------"
  IMPRIMIR j1.nombre, " - Puntaje: ", j1.puntaje
  IMPRIMIR "Carta: ", carta_j1.nombre, " | Vel: ", carta_j1.velocidad, " | Fue: ", carta_j1.fuerza, " | Elem: ", carta_j1.elemento, " | Pes: ", carta_j1.peso, " | Alt: ", carta_j1.altura
  IMPRIMIR "Valor: ", valor_j1
  IMPRIMIR "-----------------------------------------------------"
  IMPRIMIR j2.nombre, " - Puntaje: ", j2.puntaje
  IMPRIMIR "Carta: ", carta_j2.nombre, " | Vel: ", carta_j2.velocidad, " | Fue: ", carta_j2.fuerza, " | Elem: ", carta_j2.elemento, " | Pes: ", carta_j2.peso, " | Alt: ", carta_j2.altura
  IMPRIMIR "Valor: ", valor_j2
  IMPRIMIR "-----------------------------------------------------"
  ESPERAR_ENTRADA("Presioná ENTER para continuar...")
FINFUNCION

# Función para calcular la ronda
FUNCION ronda(jugador_1, jugador_2, descarte):
  atributo_elegido = ALEATORIO(atributos)

  carta_j1 = jugador_1.mazo.carta
  carta_j2 = jugador_2.mazo.carta

  valor_j1 = carta_j1[atributo_elegido]
  valor_j2 = carta_j2[atributo_elegido]

  mostrar_estado(jugador_1, jugador_2, carta_j1, carta_j2, atributo_elegido, valor_j1, valor_j2, num_ronda)

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

MIENTRAS juego_terminado==Falso:
  ronda(jugador_1, jugador_2, descarte)
  num_ronda = num_ronda + 1
  SI jugador_1.mazo == NULO O jugador_2.mazo == NULO:
    juego_terminado=True
  FIN SI
