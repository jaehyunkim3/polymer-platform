from __future__ import annotations


def summarize_error_distribution(values: list[float]) -> dict:
    if not values:
        return {"count": 0, "mean_abs_error": None, "max_abs_error": None}
    mean_abs_error = sum(abs(v) for v in values) / len(values)
    max_abs_error = max(abs(v) for v in values)
    return {
        "count": len(values),
        "mean_abs_error": round(mean_abs_error, 4),
        "max_abs_error": round(max_abs_error, 4),
    }
