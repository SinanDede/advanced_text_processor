import statistics

def detect_anomalies(values: list[float], z_thresh: float = 3.0) -> list[tuple[int, float]]:
    """Return indices and values where Z-score > threshold."""
    if not values:
        return []
    mean = statistics.mean(values)
    stdev = statistics.pstdev(values)
    if stdev == 0:
        return []
    anomalies = []
    for i, v in enumerate(values):
        z = abs((v - mean) / stdev)
        if z > z_thresh:
            anomalies.append((i, v))
    return anomalies
