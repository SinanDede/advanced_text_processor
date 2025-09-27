import os
import json
from advanced_text_processor.text_cleaner import clean_text
from advanced_text_processor.tokenizer import tokenize
from advanced_text_processor.ngrams import generate_ngrams
from advanced_text_processor.vectorizer import vectorize_text

def process_text_file(file_path, ngram_size=1):
    """
    Processes a single text file: cleans, tokenizes, generates n-grams, and vectorizes.

    Args:
        file_path (str): Path to the input text file.
        ngram_size (int): The size of the n-grams.

    Returns:
        dict: A dictionary containing tokens, n-grams, and the vectorized representation.
    """
    with open(file_path, "r") as file:
        raw_text = file.read()
    
    clean = clean_text(raw_text)
    tokens = tokenize(clean)
    ngrams = generate_ngrams(tokens, n=ngram_size)
    vector = vectorize_text(tokens)
    
    return {
        "tokens": tokens,
        "ngrams": ngrams,
        "vector": vector
    }

def process_dataset(input_dir, output_file, ngram_size=1):
    """
    Processes all text files in a directory and saves the dataset.

    Args:
        input_dir (str): Directory containing raw text files.
        output_file (str): Path to save the processed dataset.
        ngram_size (int): The size of the n-grams.
    """
    dataset = {}
    
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        if os.path.isfile(file_path) and file_name.endswith(".txt"):
            dataset[file_name] = process_text_file(file_path, ngram_size)
    
    with open(output_file, "w") as outfile:
        json.dump(dataset, outfile, indent=4)
    
    print(f"Dataset saved to {output_file}.")
