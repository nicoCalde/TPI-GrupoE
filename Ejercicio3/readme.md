# CABAMon Go!

Este proyecto es una simulación de un juego de cartas por turnos entre dos jugadores (o PC), basado en lógica de estructuras de datos tipo pila (LIFO), con bonificaciones según elementos (fuego, agua, electricidad, etc).

---

## 📋 Requisitos del juego

- 2 jugadores, 3 modos de juego: 
    - humano vs humano
    - humano vs PC
    - PC vs PC
- Mazos generados automáticamente.
- Se juega por turnos.
- Se compara un atributo por ronda.
- Gana quien tenga más puntaje o quien quede con cartas al final.

---

## 🔧 Tipos y estructuras usadas

- `Carta`: contiene `nombre`, `velocidad`, `fuerza`, `elemento`, `peso`, `altura`.
- `Nodo`: representa un nodo de la pila con una `Carta` y un puntero `siguiente`.
- `Mazo`: es una pila de `Nodos`.
- `Jugador`: contiene `nombre`, `mazo` y `puntaje`.
- `Descarte`: es otra pila donde se almacenan cartas en empate.

---

## ¿Cómo se reparten los mazos?

```plaintext
Supongamos que:

jugador_1.mazo = Nodo C -> Nodo B -> Nodo A -> Vacío
nodo_actual = Nodo D -> Vacío

Entonces cuando nodo_actual.siguiente = jugador_1.mazo:

nodo_actual = Nodo D -> Nodo C -> Nodo B -> Nodo A

Y para actualizar el mazo, hacemos el proceso inverso:

jugador_1.mazo = nodo_actual

Es equivalente a decir:

jugador_1.mazo = Nodo D -> Nodo C -> Nodo B -> Nodo A

```

Esto simula el comportamiento de una pila (Last In, First Out).

## Funcionamiento de la ronda


1. El jugador con el turno elige un atributo:
   - `Aleatorio` si es PC.
   - `Manual` si es humano.

2. Se `comparan` los valores del atributo entre ambas cartas.

3. Si un elemento tiene ventaja (por ejemplo, agua > fuego), `se suma +1` al valor del atributo.

4. Se `desapilan` las cartas de ambos jugadores.

5. Resultado:
   - Si un jugador gana: suma 1 punto y se queda con ambas cartas (y con las del descarte si hubiera).
   - Si hay empate: ambas cartas van al `descarte`.

## Lógica de comparación de elementos

La idea y para no expandir innecesariamente el código era realizar un esbozo funcional de al comparación de elementos. Se hizo a través de condicionales, pero que es ampliable cuando se defina un criterio específico, así que por ahora son poquitos. 

Los elementos que tienen jerarquía de momento son:

```
Agua > Fuego
Electricidad > Agua
```

Los demás elementos no tienen jerarquía, por ahora.


## Funcionamiento del descarte

Con el mismo principio explicado en cómo se reparten los mazos usando pilas, se sigue la siguiente lógica:

- Si una ronda `empata`, ambas cartas se agregan al descarte.
- Se apilan en orden: carta del jugador 2 queda arriba.
- En rondas futuras, el jugador ganador se lleva `todas las cartas` del descarte.


Esto funciona como un “`pozo acumulado`”, incentivando a ganar la siguiente ronda tras un empate.

## Bucle principal


Mientras:
  - Ningún jugador se quedó sin cartas.
  - No se llegó al máximo de 250 rondas.

Se sigue ejecutando el ciclo de rondas, alternando el turno entre jugadores.
