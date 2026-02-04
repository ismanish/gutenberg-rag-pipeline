# Gutenberg RAG Pipeline

A Retrieval-Augmented Generation (RAG) pipeline for querying Project Gutenberg texts.

## Features

- Download and cache Gutenberg texts
- Create vector embeddings using OpenAI
- Query texts using natural language

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from src.rag import GutenbergRAG
from src.rag.data_loader import download_gutenberg_text

# Load text
text = download_gutenberg_text("bible_kjv")

# Create RAG pipeline
rag = GutenbergRAG(api_key="your-openai-key")
rag.create_index(text)

# Query
answer = rag.query("What is the first verse of Genesis?")
print(answer)
```

## Project Structure

```
 src/
   └── rag/
       ├── __init__.py
       ├── pipeline.py
       └── data_loader.py
 tests/
       └── test_rag.py
requirements.txt
README.md
```

## License

MIT License
