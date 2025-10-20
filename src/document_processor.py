"""
Document Processor for Turkish Party Charter RAG System
======================================================

Handles loading and chunking of PDF, DOCX, and TXT documents
with Turkish language support.

Author: Baran Can Ercan
Date: October 20, 2025
"""

from typing import List, Optional
import os
from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader
)
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


class DocumentProcessor:
    """
    Process documents with Turkish language support.
    
    Features:
    - Multi-format support (PDF, DOCX, TXT)
    - Turkish character handling (UTF-8)
    - Recursive text splitting
    - Metadata extraction
    """
    
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 100,
        separators: Optional[List[str]] = None
    ):
        """
        Initialize document processor.
        
        Args:
            chunk_size: Target size of chunks in tokens
            chunk_overlap: Number of tokens to overlap between chunks
            separators: List of separators for splitting (default: ["\n\n", "\n", " ", ""])
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        # Default separators optimized for Turkish documents
        self.separators = separators or ["\n\n", "\n", " ", ""]
        
        # Initialize text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=self.separators,
            length_function=len,
            is_separator_regex=False,
        )
    
    def load_document(self, file_path: str) -> List[Document]:
        """
        Load a document from file.
        
        Args:
            file_path: Path to the document
            
        Returns:
            List of Document objects
            
        Raises:
            ValueError: If file format is not supported
            FileNotFoundError: If file doesn't exist
        """
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Determine loader based on file extension
        file_ext = Path(file_path).suffix.lower()
        
        try:
            if file_ext == '.pdf':
                loader = PyPDFLoader(file_path)
            elif file_ext == '.txt':
                # UTF-8 encoding for Turkish characters
                loader = TextLoader(file_path, encoding='utf-8')
            elif file_ext in ['.docx', '.doc']:
                loader = Docx2txtLoader(file_path)
            else:
                raise ValueError(
                    f"Unsupported file format: {file_ext}. "
                    f"Supported formats: .pdf, .txt, .docx, .doc"
                )
            
            documents = loader.load()
            return documents
            
        except Exception as e:
            raise Exception(f"Error loading {file_path}: {str(e)}")
    
    def chunk_documents(self, documents: List[Document]) -> List[Document]:
        """
        Split documents into chunks.
        
        Args:
            documents: List of Document objects to chunk
            
        Returns:
            List of chunked Document objects
        """
        return self.text_splitter.split_documents(documents)
    
    def process_file(self, file_path: str) -> List[Document]:
        """
        Complete processing pipeline for a single file.
        
        Args:
            file_path: Path to the document
            
        Returns:
            List of processed and chunked Document objects
        """
        # Load document
        documents = self.load_document(file_path)
        
        # Chunk documents
        chunks = self.chunk_documents(documents)
        
        # Add metadata
        filename = os.path.basename(file_path)
        for i, chunk in enumerate(chunks):
            # Add chunk-specific metadata
            chunk.metadata['chunk_id'] = i
            chunk.metadata['source_file'] = filename
            chunk.metadata['total_chunks'] = len(chunks)
            
            # Preserve existing metadata (page numbers, etc.)
            if 'page' not in chunk.metadata:
                chunk.metadata['page'] = None
        
        return chunks
    
    def process_directory(
        self,
        directory_path: str,
        extensions: Optional[List[str]] = None
    ) -> List[Document]:
        """
        Process all documents in a directory.
        
        Args:
            directory_path: Path to directory containing documents
            extensions: List of file extensions to process (default: ['.pdf', '.txt', '.docx'])
            
        Returns:
            List of all processed chunks from all documents
        """
        if extensions is None:
            extensions = ['.pdf', '.txt', '.docx', '.doc']
        
        all_chunks = []
        directory = Path(directory_path)
        
        if not directory.exists():
            raise FileNotFoundError(f"Directory not found: {directory_path}")
        
        # Process each file
        for file_path in directory.rglob('*'):
            if file_path.suffix.lower() in extensions:
                try:
                    chunks = self.process_file(str(file_path))
                    all_chunks.extend(chunks)
                    print(f"✅ Processed: {file_path.name} ({len(chunks)} chunks)")
                except Exception as e:
                    print(f"❌ Error processing {file_path.name}: {str(e)}")
                    continue
        
        return all_chunks
    
    def get_stats(self, chunks: List[Document]) -> dict:
        """
        Get statistics about processed chunks.
        
        Args:
            chunks: List of Document chunks
            
        Returns:
            Dictionary with statistics
        """
        if not chunks:
            return {
                'total_chunks': 0,
                'avg_chunk_length': 0,
                'min_chunk_length': 0,
                'max_chunk_length': 0,
                'unique_sources': 0
            }
        
        chunk_lengths = [len(chunk.page_content) for chunk in chunks]
        sources = set(chunk.metadata.get('source_file', 'unknown') for chunk in chunks)
        
        return {
            'total_chunks': len(chunks),
            'avg_chunk_length': sum(chunk_lengths) / len(chunk_lengths),
            'min_chunk_length': min(chunk_lengths),
            'max_chunk_length': max(chunk_lengths),
            'unique_sources': len(sources),
            'sources': list(sources)
        }


# Quick test function
if __name__ == "__main__":
    """Quick test of document processor"""
    
    print("=== Document Processor Test ===\n")
    
    # Initialize processor
    processor = DocumentProcessor(
        chunk_size=1000,
        chunk_overlap=100
    )
    
    # Test with a sample file
    test_file = f'.\Desktop\LLMProject\turkish-party-charter-rag\data\party_charters\chp.pdf'

    
    if os.path.exists(test_file):
        print(f"Processing: {test_file}\n")
        
        # Process file
        chunks = processor.process_file(test_file)
        
        # Get statistics
        stats = processor.get_stats(chunks)
        
        print(f"✅ Processing complete!")
        print(f"\nStatistics:")
        print(f"  Total chunks: {stats['total_chunks']}")
        print(f"  Avg chunk length: {stats['avg_chunk_length']:.0f} chars")
        print(f"  Min chunk length: {stats['min_chunk_length']} chars")
        print(f"  Max chunk length: {stats['max_chunk_length']} chars")
        
        # Show first chunk
        print(f"\n📄 First chunk preview:")
        print(f"  Content: {chunks[0].page_content[:200]}...")
        print(f"  Metadata: {chunks[0].metadata}")
    else:
        print(f"❌ Test file not found: {test_file}")
        print("Place a PDF file in data/party_charters/ to test")
