## Guía para la presentación:

### Observaciones

- ¿Cómo se reparten los mazos?

```
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

- Funcionamiento de la ronda

```

```

- Funcionamiento del descarte

```

```

##ToDo

Todavía no entiendo bien el funcionamiento de los turnos en la consigna. Quizás haya que adaptar el juego para que admita jugadores humanos también.