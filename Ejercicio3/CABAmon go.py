import random
import os

class Carta:
    def __init__(self, nombre, velocidad, fuerza, elemento, peso, altura):
        self.nombre = nombre
        self.velocidad = velocidad
        self.fuerza = fuerza
        self.elemento = elemento
        self.peso = peso
        self.altura = altura

    def __str__(self):
        return f"{self.nombre} | Vel: {self.velocidad} | Fue: {self.fuerza} | Elem: {self.elemento} | Pes: {self.peso} | Alt: {self.altura}"

class Nodo:
    def __init__(self, carta):
        self.carta = carta
        self.siguiente = None

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mazo = None
        self.puntaje = 0

class Descarte:
    def __init__(self):
        self.mazo = None

TAMANIO_MAZO = 250
ELEMENTOS = ["agua", "fuego", "aire", "tierra", "electricidad"]
ATRIBUTOS = ["velocidad", "fuerza", "peso", "altura"]
MAX_RONDA = 250

def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("CABAMon Go!")
        print("-----------------------------------------------------")
        print("Elegí el modo de juego:")
        print("1. PC vs PC")
        print("2. Jugador vs PC")
        print("3. Jugador vs Jugador")
        print("-----------------------------------------------------")
        
        opcion = input()
        if opcion in ['1', '2', '3']:
            return int(opcion)
        else:
            print("Tenés que elegir una opción válida.")

def armar_mazo():
    mazo_total = None
    for i in range(1, TAMANIO_MAZO + 1):
        carta = Carta(
            nombre=f"monstruito_{i}",
            velocidad=random.randint(1, 10),
            fuerza=random.randint(1, 10),
            elemento=random.choice(ELEMENTOS),
            peso=random.randint(1, 10),
            altura=random.randint(1, 10)
        )
        nodo_nuevo = Nodo(carta)
        nodo_nuevo.siguiente = mazo_total
        mazo_total = nodo_nuevo
    return mazo_total

def mezclar_mazo(mazo):
    cartas = []
    actual = mazo
    while actual:
        cartas.append(actual.carta)
        actual = actual.siguiente
    random.shuffle(cartas)
    nuevo_mazo = None
    for carta in cartas:
        nodo = Nodo(carta)
        nodo.siguiente = nuevo_mazo
        nuevo_mazo = nodo
    return nuevo_mazo

def repartir_mazo(mazo_total, jugador_1, jugador_2):
    turno_jugador = 1
    while mazo_total:
        nodo_actual = Nodo(mazo_total.carta)
        mazo_total = mazo_total.siguiente
        if turno_jugador == 1:
            nodo_actual.siguiente = jugador_1.mazo
            jugador_1.mazo = nodo_actual
            turno_jugador = 2
        else:
            nodo_actual.siguiente = jugador_2.mazo
            jugador_2.mazo = nodo_actual
            turno_jugador = 1

def apilar_al_fondo(mazo, nodo_nuevo):
    if not mazo:
        return nodo_nuevo
    actual = mazo
    while actual.siguiente:
        actual = actual.siguiente
    actual.siguiente = nodo_nuevo
    return mazo

def comparar_elementos(c1, c2):
    ganador = 0
    if c1.elemento == "agua" and c2.elemento == "fuego":
        ganador = 1
    elif c1.elemento == "fuego" and c2.elemento == "agua":
        ganador = 2
    elif c1.elemento == "electricidad" and c2.elemento == "agua":
        ganador = 1
    elif c1.elemento == "agua" and c2.elemento == "electricidad":
        ganador = 2
    return ganador

def mostrar_estado(j1, j2, c1, c2, atributo, v1, v2, ronda, ganador):
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Ronda {ronda} - Atributo elegido: {atributo.upper()}")
    print("-----------------------------------------------------")
    print(f"{j1.nombre} - Puntaje acumulado: {j1.puntaje}")
    print(f"Carta: {c1}")
    print(f"Valor: {v1}")
    print("-----------------------------------------------------")
    print(f"{j2.nombre} - Puntaje acumulado: {j2.puntaje}")
    print(f"Carta: {c2}")
    print(f"Valor: {v2}")
    print("-----------------------------------------------------")
    if ganador:
        print(f"Ganó el jugador {ganador.nombre}!")
    else:
        print("Empate! Las cartas se van al descarte.") 
    input("Presioná ENTER para continuar...")

def elegir_atributo(turno, modo_juego):
    os.system("cls" if os.name == "nt" else "clear")
    if modo_juego == 1 or (modo_juego == 2 and turno==2):
        atributo = random.choice(ATRIBUTOS)
        print(f"PC {turno} elige el atributo {atributo.upper()}")
        print ("Presioná ENTER para continuar...")
        input()
        return atributo
    elif (modo_juego == 2 and turno==1) or modo_juego == 3:
        while True:
            print(f"Jugador {turno} elige un atributo:")
            for i, atributo in enumerate(ATRIBUTOS, start=1):
                print(f"{i}. {atributo.capitalize()}")
            opcion = input("Seleccioná el número del atributo: ")
            if opcion.isdigit() and 1 <= int(opcion) <= len(ATRIBUTOS):
                return ATRIBUTOS[int(opcion) - 1]
            else:
                print("Opción inválida. Por favor, elegí un número válido.")

def ronda(j1, j2, descarte, num_ronda, modo_juego, turno):
    atributo = elegir_atributo(turno, modo_juego)
    carta_j1 = j1.mazo.carta
    carta_j2 = j2.mazo.carta
    valor_j1 = getattr(carta_j1, atributo)
    valor_j2 = getattr(carta_j2, atributo)
    elemento_ganador = comparar_elementos(carta_j1, carta_j2)
    if elemento_ganador == 1:
        valor_j1 += 1
    elif elemento_ganador == 2:
        valor_j2 += 1
    j1.mazo = j1.mazo.siguiente
    j2.mazo = j2.mazo.siguiente
    if valor_j1 > valor_j2:
        j1.puntaje += 1
        nodo1 = Nodo(carta_j1)
        nodo1.siguiente = None
        nodo2 = Nodo(carta_j2)
        nodo2.siguiente = nodo1
        j1.mazo = apilar_al_fondo(j1.mazo, nodo2)
        while descarte.mazo:
            nodo_desc = descarte.mazo
            descarte.mazo = descarte.mazo.siguiente
            nodo_desc.siguiente = None
            j1.mazo = apilar_al_fondo(j1.mazo, nodo_desc)
        mostrar_estado(j1, j2, carta_j1, carta_j2, atributo, valor_j1, valor_j2, num_ronda, j1)
    elif valor_j2 > valor_j1:
        j2.puntaje += 1
        nodo1 = Nodo(carta_j1)
        nodo1.siguiente = None
        nodo2 = Nodo(carta_j2)
        nodo2.siguiente = nodo1
        j2.mazo = apilar_al_fondo(j2.mazo, nodo2)
        while descarte.mazo:
            nodo_desc = descarte.mazo
            descarte.mazo = descarte.mazo.siguiente
            nodo_desc.siguiente = None
            j2.mazo = apilar_al_fondo(j2.mazo, nodo_desc)
        mostrar_estado(j1, j2, carta_j1, carta_j2, atributo, valor_j1, valor_j2, num_ronda, j2)
    else:
        nodo1 = Nodo(carta_j1)
        nodo1.siguiente = descarte.mazo
        descarte.mazo = nodo1
        nodo2 = Nodo(carta_j2)
        nodo2.siguiente = descarte.mazo
        descarte.mazo = nodo2
        mostrar_estado(j1, j2, carta_j1, carta_j2, atributo, valor_j1, valor_j2, num_ronda, None)

def main():
    modo_juego = menu_principal()
    jugador_1 = Jugador("Jugador 1")
    jugador_2 = Jugador("Jugador 2")
    descarte = Descarte()
    mazo_total = armar_mazo()
    mazo_total = mezclar_mazo(mazo_total)
    repartir_mazo(mazo_total, jugador_1, jugador_2)
    num_ronda = 1
    juego_terminado = False
    turno = 1
    while not juego_terminado:
        if jugador_1.mazo is None or jugador_2.mazo is None or num_ronda > MAX_RONDA:
            juego_terminado = True
        else:
            ronda(jugador_1, jugador_2, descarte, num_ronda, modo_juego, turno)
            num_ronda = num_ronda + 1
            # Turnamos jugadores
            if turno == 1:
                turno = 2
            else:
                turno = 1
    print("Juego terminado!")
    if jugador_1.puntaje > jugador_2.puntaje:
        print("Ganó Jugador 1 🎉")
    elif jugador_2.puntaje > jugador_1.puntaje:
        print("Ganó Jugador 2 🎉")
    else:
        print("Empate! 🤝")

if __name__ == "__main__":
    main()
