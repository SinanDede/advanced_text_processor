import random, collections

def balanced_split(rows: list[dict], label: str, test_ratio: float = 0.2, seed: int = 0):
    """Split dataset keeping class balance."""
    random.seed(seed)
    by_class = collections.defaultdict(list)
    for r in rows:
        by_class[r[label]].append(r)

    train, test = [], []
    for c, items in by_class.items():
        k = int(len(items) * (1 - test_ratio))
        random.shuffle(items)
        train.extend(items[:k])
        test.extend(items[k:])
    return train, test
