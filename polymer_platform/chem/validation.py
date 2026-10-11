from __future__ import annotations

from polymer_platform.chem.formulas import calculate_equivalent_weight, molecular_weight_from_formula


def validate_material_formula(formula: str) -> dict:
    mass = molecular_weight_from_formula(formula)
    return {
        "formula": formula,
        "molecular_weight": mass,
        "status": "valid",
    }


def validate_polyurethane_batch(
    polyol_formula: str,
    polyol_mw: float,
    polyol_oh_eq: float,
    diisocyanate_formula: str,
    diisocyanate_mw: float,
    diisocyanate_nco_eq: float,
    target_nco_oh_ratio: float,
) -> dict:
    polyol_mw_checked = polyol_mw or molecular_weight_from_formula(polyol_formula)
    diisocyanate_mw_checked = diisocyanate_mw or molecular_weight_from_formula(diisocyanate_formula)

    polyol_eq = polyol_oh_eq or calculate_equivalent_weight(polyol_mw_checked, 2)
    diisocyanate_eq = diisocyanate_nco_eq or calculate_equivalent_weight(diisocyanate_mw_checked, 2)

    actual_ratio = diisocyanate_eq / polyol_eq if polyol_eq else 0.0
    delta = abs(actual_ratio - target_nco_oh_ratio)

    return {
        "polyol_molecular_weight": round(polyol_mw_checked, 3),
        "diisocyanate_molecular_weight": round(diisocyanate_mw_checked, 3),
        "polyol_equivalent": round(polyol_eq, 3),
        "diisocyanate_equivalent": round(diisocyanate_eq, 3),
        "actual_nco_oh_ratio": round(actual_ratio, 4),
        "target_nco_oh_ratio": target_nco_oh_ratio,
        "deviation": round(delta, 4),
        "status": "ok" if delta < 0.10 else "needs_review",
    }
