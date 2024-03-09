#!/usr/bin/env python3

def index_range(page, page_size):
    """
    Calcula el rango de índices para una página específica en una paginación.

    Args:
        page (int): Número de la página (comenzando desde 1).
        page_size (int): Tamaño de la página.

    Returns:
        tuple: Una tupla de dos elementos que contiene el índice de inicio
               y el índice final para la página especificada.
    """
    # Calcula el índice de inicio
    start_index = (page - 1) * page_size
    
    # Calcula el índice final
    end_index = start_index + page_size - 1
    
    # Devuelve una tupla que contiene el índice de inicio y el índice final
    return (start_index, end_index)
