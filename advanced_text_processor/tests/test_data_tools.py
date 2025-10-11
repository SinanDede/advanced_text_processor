from advanced_text_processor import (
    summarize_table, fuzzy_merge, balanced_split,
    save_version, load_version, detect_anomalies
)

def test_summarize_table():
    rows = [{"x": 1, "y": 2}, {"x": 2, "y": 3}]
    s = summarize_table(rows)
    assert "x" in s and "mean" in s["x"]

def test_fuzzy_merge():
    a = [{"name": "Alice"}, {"name": "Bob"}]
    b = [{"Name": "Alicia"}, {"Name": "Bobby"}]
    merged = fuzzy_merge(a, b, threshold=0.5)
    assert merged

def test_balanced_split():
    data = [{"label": "a"}, {"label": "a"}, {"label": "b"}, {"label": "b"}]
    train, test = balanced_split(data, "label", 0.5, seed=1)
    assert len(train) == len(test)

def test_versioned_manager(tmp_path):
    data = [{"a": 1}, {"a": 2}]
    path = save_version("test", data, folder=tmp_path)
    loaded = load_version(path)
    assert loaded == data

def test_detect_anomalies():
    vals = [1, 2, 3, 100]
    anomalies = detect_anomalies(vals, z_thresh=2)
    assert anomalies and anomalies[0][1] == 100

