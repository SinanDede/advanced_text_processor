from collections import Counter

def vectorize_text(tokens):
    """
    Converts tokens into a frequency vector.

    Args:
        tokens (list): List of tokens (words).

    Returns:
        dict: A dictionary where keys are words and values are their frequencies.
    """
    return dict(Counter(tokens))
