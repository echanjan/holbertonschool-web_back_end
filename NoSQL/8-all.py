#!/usr/bin/env python3
"""Este módulo usa pymongo para listar los documentos."""


def list_all(mongo_collection):
    """
    Documentos de una colección

    Args:
        mongo_collection(Colecttion): Objeto de colección

    Returns:
        List[Dict[str, Any]]: Una lista de documentos de la colección recibida
    """

    documents = []

    cursor = mongo_collection.find()
    documents = [document for document in cursor]
    return documents
