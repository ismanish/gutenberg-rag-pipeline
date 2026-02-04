"""Tests for RAG pipeline."""

import pytest
from unittest.mock import Mock, patch


def test_data_loader_urls():
    """Test that Gutenberg URLs are defined."""
    from src.rag.data_loader import GUTENBERG_URLS
    
    assert "bible_kjv" in GUTENBERG_URLS
    assert GUTENBERG_URLS["bible_kjv"].startswith("https://")


def test_rag_initialization():
    """Test RAG pipeline initialization."""
    with patch('src.rag.pipeline.OpenAIEmbeddings'):
        with patch('src.rag.pipeline.ChatOpenAI'):
            from src.rag.pipeline import GutenbergRAG
            rag = GutenbergRAG(api_key="test-key")
            assert rag.vectorstore is None
            assert rag.qa_chain is None
