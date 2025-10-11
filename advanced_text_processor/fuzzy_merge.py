import difflib, itertools

def fuzzy_merge(a: list[dict], b: list[dict], on: str | None = None, threshold: float = 0.6) -> list[dict]:
    """Merge two list-of-dicts datasets on fuzzy key matches."""
    if not a or not b:
        return []

    keys_a = list(a[0].keys())
    keys_b = list(b[0].keys())

    if on is None:
        matches = []
        for ka in keys_a:
            best = difflib.get_close_matches(ka, keys_b, n=1, cutoff=threshold)
            if best:
                matches.append((ka, best[0]))
        on = matches[0][0] if matches else keys_a[0]

    result = []
    for r1, r2 in itertools.product(a, b):
        v1 = str(r1.get(on, "")).lower()
        v2 = str(r2.get(on, "")).lower()
        score = difflib.SequenceMatcher(None, v1, v2).ratio()
        if score >= threshold:
            merged = r1.copy()
            merged.update(r2)
            result.append(merged)
    return result