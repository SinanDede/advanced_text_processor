from advanced_text_processor import clean_text, tokenize, generate_ngrams, vectorize_text

def test_pipeline():
    text = "Hello hello world!"
    tokens = tokenize(clean_text(text))
    ngrams = generate_ngrams(tokens, 2)
    vec = vectorize_text(ngrams)
    assert "hello world" in vec

