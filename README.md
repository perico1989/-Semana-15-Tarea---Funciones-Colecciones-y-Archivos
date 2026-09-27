# Registro de Estudiantes

Programa sencillo en Python que utiliza una **lista** para registrar y consultar nombres de estudiantes.

## ¿Qué hace el programa?

1. Crea una lista vacía llamada `estudiantes`.
2. Agrega tres nombres de ejemplo a la lista (`Jesús`, `Pedro`, `Pablo`) usando `append()`.
3. Pide al usuario que escriba el nombre de un nuevo estudiante y lo agrega también a la lista.
4. Muestra en pantalla todos los estudiantes registrados, recorriendo la lista con un ciclo `for`.
5. Pide al usuario un nombre para buscar y verifica con `in` si ese nombre está o no en la lista, mostrando el resultado.

## Estructura de datos utilizada

- **Lista** (`list`): permite guardar varios nombres en orden y agregar nuevos elementos fácilmente.

## Cómo ejecutarlo

```bash
python registro_estudiantes.py
```

El programa pedirá:
- El nombre de un nuevo estudiante para agregar a la lista.
- Un nombre para buscar dentro de la lista.

## Ejemplo de salida

```
Escribe el nombre de un nuevo estudiante: Jimmy

Lista de estudiantes registrados:
- Jesús
- Pedro
- Pablo
- Jimmy

Escribe un nombre para buscar en la lista: Luis
'Luis' sí está registrado en la lista.
```
