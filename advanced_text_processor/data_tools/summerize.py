import statistics, collections, datetime

def summarize_table(rows: list[dict]) -> dict:
    """Return quick statistical summary of list-of-dicts dataset."""
    if not rows:
        return {}

    cols = rows[0].keys()
    summary = {}
    for col in cols:
        values = [r[col] for r in rows if r[col] not in ("", None)]
        types = [type(v).__name__ for v in values]
        type_counts = collections.Counter(types)
        summary[col] = {"count": len(values), "types": dict(type_counts)}

        nums = [v for v in values if isinstance(v, (int, float))]
        if nums:
            summary[col].update({
                "mean": round(statistics.mean(nums), 3),
                "stdev": round(statistics.pstdev(nums), 3),
                "min": min(nums),
                "max": max(nums)
            })
        dates = [v for v in values if isinstance(v, datetime.date)]
        if dates:
            summary[col].update({"date_range": [min(dates), max(dates)]})
    return summary
