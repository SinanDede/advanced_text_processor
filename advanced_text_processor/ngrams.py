def generate_ngrams(tokens, n=2):
    """
    Generates n-grams from a list of tokens.

    Args:
        tokens (list): List of tokens (words).
        n (int): The size of the n-grams.

    Returns:
        list: List of n-grams as tuples.
    """
    return [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
