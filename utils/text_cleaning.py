"""
Text Cleaning Utilities (Safe Version)

These helper functions are used across ingestion and content-generation
pipelines to normalize text before embeddings or LLM prompts.
This is a simplified and safe subset of the production version.
"""

import re
from typing import List


def remove_noise(text: str) -> str:
    """Remove HTML tags, brackets, and excessive punctuation."""
    text = re.sub(r"<.*?>", "", text)       # remove HTML
    text = re.sub(r"\[.*?\]", "", text)     # remove [Music]
    text = re.sub(r"[{}|\^~`]", "", text)   # remove random symbols
    return text


def normalize_whitespace(text: str) -> str:
    """Collapse whitespace and trim."""
    return re.sub(r"\s+", " ", text).strip()


def split_sentences(text: str) -> List[str]:
    """Lightweight sentence splitter."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return [s for s in sentences if s]


def clean_text(text: str) -> str:
    """Full cleaning pipeline."""
    text = remove_noise(text)
    text = normalize_whitespace(text)
    return text
