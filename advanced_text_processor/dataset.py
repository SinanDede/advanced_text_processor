import csv
from .text_cleaner import clean_text
from .tokenizer import tokenize
from .ngrams import generate_ngrams
from .vectorizer import vectorize_text

def process_text_file(path: str, ngram_n: int = 2) -> dict[str, int]:
    """Read a text file, clean, tokenize, create ngrams, and vectorize."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    tokens = tokenize(clean_text(text))
    tokens = generate_ngrams(tokens, n=ngram_n)
    return vectorize_text(tokens)

def process_dataset(csv_path: str, text_col: str, ngram_n: int = 2) -> list[dict[str, int]]:
    """Process a CSV dataset column into token frequency dicts."""
    results = []
    with open(csv_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            text = row[text_col]
            tokens = tokenize(clean_text(text))
            tokens = generate_ngrams(tokens, n=ngram_n)
            results.append(vectorize_text(tokens))
    return results