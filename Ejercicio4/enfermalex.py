import random
import time
import os

# Lista de 10 colores distintos (3 medidas cada uno = 30 medidas)
COLORES = ["rojo", "verde", "azul", "amarillo", "naranja",
           "violeta", "blanco", "negro", "celeste", "marron"]

# Paso 1: crear la lista total de medidas (3 por color)
medidas = []
for color in COLORES:
    medidas.extend([color] * 3)  # 3 medidas por color

# Paso 2: crear tubos vacíos (10 tubos, cada uno puede tener hasta 4 medidas)
tubos = [[] for _ in range(10)]

# Paso 3: distribuir aleatoriamente las 30 medidas respetando el límite de 4 por tubo
random.shuffle(medidas)

for medida in medidas:
    while True:
        indice = random.randint(0, 9)
        if len(tubos[indice]) < 4:
            tubos[indice].append(medida)
            break

# Función para mostrar el estado de los tubos
def mostrar_tubos():
    print("\n=== Estado actual de los tubos ===")
    for i, tubo in enumerate(tubos):
        # Completamos con espacios vacíos si tiene menos de 4
        tubo_formateado = tubo + ["    "] * (4 - len(tubo))
        print(f"Tubo {i}: {tubo_formateado}")
    print()

# Función para verificar si el juego se completó
def fin_del_juego(tubos):
    if len(tubos) != 10:
        return False

    for tubo in tubos:
        if len(tubo) != 3:
            return False
        color_base = tubo[0]
        if any(color != color_base for color in tubo):
            return False

    return True

# Intro
print("""
╔══════════════════════════════════════════════╗
║        ▄████▄   ▄▄▄       ████▄ ▄███▄         ║
║       ███▀▀███ ▀▀██       ██ ██ ██ ██         ║
║       ██    ██   ██ ▄▄▄▄  ██ ██ ██ ██         ║
║       ▀██▄▄███   ██ ▀▀▀▀  ██ ██ ██ ██         ║
║         ▀▀▀ ▀▀  ▀▀▀       ▀▀  ▀▀  ▀▀          ║
║                                              ║
║         ENFERMALEX™ - LAB PUZZLE SYSTEM       ║
║                                              ║
║  Objetivo: separar los jarabes por color     ║
║  Cada tubo puede tener hasta 4 medidas       ║
║  Al final, deben quedar 10 tubos con:        ║
║     - 3 medidas del mismo color              ║
║     - 1 espacio vacío                        ║
║                                              ║
║  Instrucciones:                              ║
║   1. Elegí un tubo origen y uno destino      ║
║   2. Solo se mueve el tope                   ║
║   3. No podés llenar un tubo que está lleno  ║
╚══════════════════════════════════════════════╝
""")

print("Cargando...")  # mensaje de loading
time.sleep(10)  # espera de 2 segundos
os.system('cls' if os.name == 'nt' else 'clear')

# Bucle principal del juego
try:
    while True:
        mostrar_tubos()

        if fin_del_juego(tubos):
            print("🎉 ¡GANASTE CHAMP! 🎉")
            break

        try:
            origen = int(input("Ingrese el número del tubo de origen (0 a 9): "))
            if origen < 0 or origen > 9:
                print("\nNúmero inválido. Debe estar entre 0 y 9.")
                continue

            if not tubos[origen]:
                print("\nEse tubo está vacío. Intentá con otro.")
                continue

            destino = int(input("Ingrese el número del tubo de destino (0 a 9): "))
            if destino < 0 or destino > 9:
                print("\nNúmero inválido. Debe estar entre 0 y 9.")
                continue

            if len(tubos[destino]) == 4:
                print("\nEl tubo destino está lleno. Movimiento cancelado.")
                continue

            # Movimiento válido
            elemento = tubos[origen].pop()
            tubos[destino].append(elemento)
            print("\nMovimiento realizado.")

        except ValueError:
            print("Entrada inválida. Usá solo números enteros.")
except KeyboardInterrupt:
    print("\n\n⛔ Juego interrumpido. ¡Gracias por jugar ENFERMALEX™!")