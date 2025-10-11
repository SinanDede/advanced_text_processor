import json, gzip, hashlib, datetime, os

def save_version(name: str, data: list[dict], folder: str = "versions") -> str:
    """Save dataset with timestamp, gzip and hash for integrity."""
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S")
    path = os.path.join(folder, f"{name}_{timestamp}.jsonl.gz")

    with gzip.open(path, "wt", encoding="utf-8") as f:
        for row in data:
            f.write(json.dumps(row) + "\n")

    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)

    meta = {"file": path, "sha256": hasher.hexdigest(), "created": timestamp}
    with open(path + ".meta.json", "w", encoding="utf-8") as mf:
        json.dump(meta, mf, indent=2)
    return path

def load_version(path: str) -> list[dict]:
    """Load gzip dataset and verify hash if metadata exists."""
    meta_path = path + ".meta.json"
    if os.path.exists(meta_path):
        meta = json.load(open(meta_path))
        hasher = hashlib.sha256()
        with open(path, "rb") as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        if meta.get("sha256") != hasher.hexdigest():
            raise ValueError("Hash mismatch — file may be corrupted.")
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return [json.loads(line) for line in f]
