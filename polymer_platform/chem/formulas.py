from __future__ import annotations

import re

ATOMIC_WEIGHTS = {
    "H": 1.008,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "S": 32.06,
    "Cl": 35.45,
    "Br": 79.904,
    "F": 18.998,
    "P": 30.974,
    "Si": 28.085,
    "Na": 22.99,
    "K": 22.99,
}


def parse_formula(formula: str) -> dict[str, int]:
    """Parse a simple molecular formula like C6H12O6 into {C:6,...}."""
    if not formula:
        raise ValueError("Formula must not be empty.")

    tokens = re.findall(r"([A-Z][a-z]?)(\d*)", formula)
    if not tokens:
        raise ValueError(f"Unsupported formula format: {formula}")

    parsed: dict[str, int] = {}
    for element, count in tokens:
        value = int(count) if count else 1
        parsed[element] = parsed.get(element, 0) + value
    return parsed


def molecular_weight_from_formula(formula: str) -> float:
    parsed = parse_formula(formula)
    total = 0.0
    for element, count in parsed.items():
        if element not in ATOMIC_WEIGHTS:
            raise ValueError(f"Unsupported element in formula: {element}")
        total += ATOMIC_WEIGHTS[element] * count
    return round(total, 3)


def calculate_equivalent_weight(molecular_weight: float, functionality: float) -> float:
    if functionality <= 0:
        raise ValueError("Functionality must be positive.")
    return molecular_weight / functionality


def calculate_oh_equivalent(molecular_weight: float, hydroxyl_number: float) -> float:
    if hydroxyl_number <= 0:
        raise ValueError("Hydroxyl number must be positive.")
    return 56100 / hydroxyl_number


def calculate_nco_equivalent(molecular_weight: float, functionality: float) -> float:
    if functionality <= 0:
        raise ValueError("Functionality must be positive.")
    return molecular_weight / functionality


def normalize_units(value: float, from_unit: str, to_unit: str) -> float:
    conversions = {
        "g": 1.0,
        "kg": 1000.0,
        "mg": 1e-3,
        "mol": 1.0,
        "mmol": 1e-3,
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Unsupported unit conversion: {from_unit} -> {to_unit}")
    return value * conversions[from_unit] / conversions[to_unit]
