#!/usr/bin/env python3
"""Paginación simple."""

import csv
import math
from typing import List
from typing import Dict, Union

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Obtiene una página específica de la base de datos paginada.

        Args:
            page (int): Número de la página (por defecto 1).
            page_size (int): Tamaño de la página (por defecto 10).

        Returns:
            List[List]: Lista de filas de la página especificada.
        """

        # Verifica que los argumentos sean enteros mayores que 0
        assert isinstance(page, int) and page > 0, "Debe ser > 0"
        assert isinstance(page_size, int) and page_size > 0, "Debe ser > 0"

        dataset = self.dataset()

        start_index, end_index = index_range(page, page_size)

        if start_index >= len(dataset):
            return []

        if end_index < len(dataset):
            return dataset[start_index:end_index]
        else:
            return dataset[start_index:]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, any]:
        """Obtiene los metadatos de la página y el conjunto de datos paginado.

        Args:
            page (int): Número de la página (por defecto 1).
            page_size (int): Tamaño de la página (por defecto 10).

        Returns:
            dict: Diccionario que datos de la página y el conjunto de datos.
        """
        data_page = self.get_page(page, page_size)

        page_size_current = len(data_page)

        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None

        prev_page = page - 1 if page > 1 else None

        hypermedia = {
            "page_size": page_size_current,
            "page": page,
            "data": data_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return hypermedia
