from __future__ import annotations


def normalize_quantity(value: float, source_unit: str, target_unit: str) -> float:
    converters = {
        "g": 1.0,
        "kg": 1000.0,
        "mg": 0.001,
        "mol": 1.0,
        "mmol": 0.001,
    }

    if source_unit not in converters or target_unit not in converters:
        raise ValueError(f"Unsupported unit conversion: {source_unit} -> {target_unit}")

    return value * converters[source_unit] / converters[target_unit]
