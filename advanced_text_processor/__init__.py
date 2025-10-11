"""
Advanced Text Processor Library

This package provides utilities for:
- Text cleaning
- Tokenization
- N-grams generation
- Frequency vectorization
- Dataset processing
"""

from .text_cleaner import clean_text
from .tokenizer import tokenize
from .ngrams import generate_ngrams
from .vectorizer import vectorize_text
from .dataset import process_text_file, process_dataset

from .data_tools.summarize import summarize_table
from .data_tools.fuzzy_merge import fuzzy_merge
from .data_tools.balanced_split import balanced_split
from .data_tools.versioned_manager import save_version, load_version
from .data_tools.anomalies import detect_anomalies

__all__ = [
    "clean_text", "tokenize", "generate_ngrams", "vectorize_text",
    "process_text_file", "process_dataset",
    "summarize_table", "fuzzy_merge", "balanced_split",
    "save_version", "load_version", "detect_anomalies"
]
