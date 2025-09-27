import re

def clean_text(text, remove_stopwords=True):
    """
    Cleans text by removing special characters, punctuation, and stopwords.

    Args:
        text (str): Input text.
        remove_stopwords (bool): Whether to remove stopwords or not.

    Returns:
        str: Cleaned text.
    """
    stopwords = {"a", "an", "the", "and", "is", "it", "to", "in", "of", "for", "on", "with", "this"}
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Remove special characters
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    text = text.lower()  # Convert to lowercase

    if remove_stopwords:
        words = text.split()
        text = " ".join(word for word in words if word not in stopwords)

    return text
