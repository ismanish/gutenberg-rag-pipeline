"""Data loading utilities for Gutenberg texts."""

import requests
from pathlib import Path


GUTENBERG_URLS = {
    "bible_kjv": "https://www.gutenberg.org/cache/epub/10/pg10.txt",
    "bible_asv": "https://www.gutenberg.org/cache/epub/8294/pg8294.txt",
}


def download_gutenberg_text(text_id: str, cache_dir: str = "./data") -> str:
    """Download text from Project Gutenberg."""
    if text_id not in GUTENBERG_URLS:
        raise ValueError(f"Unknown text_id: {text_id}")
    
    cache_path = Path(cache_dir)
    cache_path.mkdir(exist_ok=True)
    
    filepath = cache_path / f"{text_id}.txt"
    
    if filepath.exists():
        return filepath.read_text(encoding='utf-8')
    
    url = GUTENBERG_URLS[text_id]
    response = requests.get(url)
    response.raise_for_status()
    
    filepath.write_text(response.text, encoding='utf-8')
    return response.text
