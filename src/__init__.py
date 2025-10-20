"""
Turkish Party Charter RAG System
================================

A Retrieval Augmented Generation (RAG) system for Turkish political party charters.
"""

__version__ = "0.1.0"
__author__ = "Baran Can Ercan"

from src.document_processor import DocumentProcessor
from src.vector_store import VectorStoreManager

__all__ = [
    "DocumentProcessor",
    "VectorStoreManager",
]
