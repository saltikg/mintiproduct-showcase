"""
YouTube Transcript Parser (Safe Example)

This is a simplified and safe version of the transcript parsing logic 
used inside MintiProduct. It demonstrates the text cleaning and 
chunking approach without exposing production logic, API keys, 
rate limits, or proprietary filters.
"""

import re
from typing import List

def clean_transcript(text: str) -> str:
    """
    Remove timestamps, repeated noise markers, and normalize whitespace.
    """
    text = re.sub(r"\[.*?\]", "", text)          # remove [Music], [Laughter], etc.
    text = re.sub(r"\d{1,2}:\d{2}", "", text)    # remove timestamps
    text = re.sub(r"\s+", " ", text)             # collapse spaces
    return text.strip()


def chunk_text(text: str, max_length: int = 300) -> List[str]:
    """
    Split transcript into smaller semantic chunks for embeddings.
    """
    words = text.split()
    chunks = []
    buffer = []

    for word in words:
        buffer.append(word)
        if len(buffer) >= max_length:
            chunks.append(" ".join(buffer))
            buffer = []

    if buffer:
        chunks.append(" ".join(buffer))

    return chunks


if __name__ == "__main__":
    sample = """[Music] Hello everyone, today we talk about winter glow routines 
                and how to stay motivated. [Laughter] It is a gloomy day but 
                we will focus on habits and mindset..."""

    cleaned = clean_transcript(sample)
    chunks = chunk_text(cleaned, max_length=20)

    print("Cleaned transcript:")
    print(cleaned)
    print("\nChunks:")
    for c in chunks:
        print("-", c)
