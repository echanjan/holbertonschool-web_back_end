
# Módulo de Paginación para Python

Este módulo proporciona una función simple para calcular el rango de índices de una lista paginada en Python.


## Instalación

Puedes instalar este módulo utilizando pip. Simplemente ejecuta el siguiente comando:

```bash
 pip install pagination-python
```


## Uso

Para usar la función de paginación en tu código Python, primero importa el módulo:

```bash
from pagination import index_range
```

Luego, llama a la función index_range con los parámetros de la página y el tamaño de la página para obtener el rango de índices:

```bash
page = 2
page_size = 10
start_index, end_index = index_range(page, page_size)
print(f"Rango de índices para la página {page}: {start_index} - {end_index}")
```
## Documentación de la Función

La función index_range toma dos argumentos:

- page (int): Número de la página (comenzando desde 1).
- page_size (int): Tamaño de la página.

Devuelve una tupla de dos elementos que contiene el índice de inicio y el índice final para la página especificada.

## Ejemplo

```bash
from pagination import index_range

page = 2
page_size = 10
start_index, end_index = index_range(page, page_size)
print(f"Rango de índices para la página {page}: {start_index} - {end_index}")
```

Salida:

```bash
Rango de índices para la página 2: 10 - 19
```
