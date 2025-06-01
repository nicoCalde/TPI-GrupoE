import random
import os

# Definición de estructuras, para que funcione en Python usamos clases

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

# Constantes
TAMANIO_MAZO = 250
ELEMENTOS = ["agua", "fuego", "aire", "tierra", "electricidad"]
ATRIBUTOS = ["velocidad", "fuerza", "peso", "altura"]
MAX_RONDA=10

# Funciones (podrían ser métodos)

def armar_mazo():
    mazo = None
    for i in range(1, TAMANIO_MAZO + 1):
        carta = Carta(
            nombre=f"monstruito_{i}",
            velocidad=random.randint(1, 10),
            fuerza=random.randint(1, 10),
            elemento=random.choice(ELEMENTOS),
            peso=random.randint(1, 10),
            altura=random.randint(1, 10)
        )
        nodo = Nodo(carta)
        nodo.siguiente = mazo
        mazo = nodo
    return mazo


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
    turno = 1
    while mazo_total:
        nodo_actual = Nodo(mazo_total.carta)
        mazo_total = mazo_total.siguiente

        if turno == 1:
            nodo_actual.siguiente = jugador_1.mazo
            jugador_1.mazo = nodo_actual
            turno = 2
        else:
            nodo_actual.siguiente = jugador_2.mazo
            jugador_2.mazo = nodo_actual
            turno = 1


def apilar_al_fondo(mazo, nodo_nuevo):
    if not mazo:
        return nodo_nuevo
    actual = mazo
    while actual.siguiente:
        actual = actual.siguiente
    actual.siguiente = nodo_nuevo
    return mazo


def mostrar_estado(j1, j2, carta_j1, carta_j2, atributo, valor_j1, valor_j2, num_ronda,ganador):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Ronda {num_ronda} - Atributo elegido: {atributo.upper()}")
    print("-----------------------------------------------------")
    print(f"{j1.nombre} - Puntaje acumulado: {j1.puntaje}")
    print(f"Carta: {carta_j1}")
    print(f"Valor: {valor_j1}")
    print("-----------------------------------------------------")
    print(f"{j2.nombre} - Puntaje acumulado: {j2.puntaje}")
    print(f"Carta: {carta_j2}")
    print(f"Valor: {valor_j2}")
    print("-----------------------------------------------------")
    print(f"Ganador de la ronda: {ganador.nombre} 🎉")
    input("Presioná ENTER para continuar...\n")


def ronda(j1, j2, descarte, num_ronda):
    if not j1.mazo or not j2.mazo:
      # Podríamos ver de agregar try except, pero no sé si nos dejan
        return

    atributo = random.choice(ATRIBUTOS)
    carta_j1 = j1.mazo.carta
    carta_j2 = j2.mazo.carta
    valor_j1 = getattr(carta_j1, atributo)
    valor_j2 = getattr(carta_j2, atributo)


    j1.mazo = j1.mazo.siguiente
    j2.mazo = j2.mazo.siguiente

    if valor_j1 > valor_j2:
        j1.puntaje += 1
        nodo1 = Nodo(carta_j1)
        nodo2 = Nodo(carta_j2)
        nodo2.siguiente = nodo1
        j1.mazo = apilar_al_fondo(j1.mazo, nodo2)

        mostrar_estado(j1, j2, carta_j1, carta_j2, atributo, valor_j1, valor_j2, num_ronda, j1)

    elif valor_j2 > valor_j1:
        j2.puntaje += 1
        nodo1 = Nodo(carta_j1)
        nodo2 = Nodo(carta_j2)
        nodo2.siguiente = nodo1
        j2.mazo = apilar_al_fondo(j2.mazo, nodo2)

        mostrar_estado(j1, j2, carta_j1, carta_j2, atributo, valor_j1, valor_j2, num_ronda, j2)


    else:
        nodo1 = Nodo(carta_j1)
        nodo1.siguiente = descarte.mazo
        descarte.mazo = nodo1
        nodo2 = Nodo(carta_j2)
        nodo2.siguiente = descarte.mazo
        descarte.mazo = nodo2

# Definición del programa y loop principal

def main():
    jugador_1 = Jugador("Jugador 1")
    jugador_2 = Jugador("Jugador 2")
    descarte = Descarte()

    mazo_total = armar_mazo()
    mazo_total = mezclar_mazo(mazo_total)
    juego_terminado = False
    num_ronda = 1
    repartir_mazo(mazo_total, jugador_1, jugador_2)

    while juego_terminado==False:
        if num_ronda > MAX_RONDA or (jugador_1.mazo is None or jugador_2.mazo is None):
            juego_terminado = True
            break
        ronda(jugador_1, jugador_2, descarte, num_ronda)
        num_ronda=num_ronda+1

    print("¡Juego terminado!")
    if jugador_1.puntaje > jugador_2.puntaje:
        print("Ganó Jugador 1 🎉")
    elif jugador_2.puntaje > jugador_1.puntaje:
        print("Ganó Jugador 2 🎉")
    else:
        print("¡Empate! 🤝")

if __name__ == "__main__":
    main()

# Todavía no entiendo bien el funcionamiento de los turnos en la consigna. Quizás haya que adaptar el juego para que admita jugadores humanos también.