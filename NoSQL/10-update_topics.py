#!/usr/bin/env python3
"""Actualiza todos los temas de un documento"""


def update_topics(mongo_collection, name, topics):
    """
    Actualiza los topics en una colección.

    Args:
        mongo_collection(Collection): Una colección de MongoDB
        name(str): Nombre de la school.
        topics(list): Lista de tareas.
    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
