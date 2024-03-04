#!/usr/bin/env python3
"""Inserta un nuevo doc python."""


def insert_school(mongo_collection, **kwargs):
    """
    Inserta un nuevo documento en una colección

    Args:
        mongo_colecttion(Colecttion): Colección

    Returns:
        str_id generado para ese documento
    """

    id = mongo_collection.insert_one(kwargs).inserted.id
    return id
