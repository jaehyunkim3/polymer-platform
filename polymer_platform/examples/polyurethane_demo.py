from __future__ import annotations

from polymer_platform.chem.validation import validate_polyurethane_batch


def run_demo() -> dict:
    result = validate_polyurethane_batch(
        polyol_formula="C3H8O2",
        polyol_mw=92.094,
        polyol_oh_eq=46.047,
        diisocyanate_formula="C8H8N2O2",
        diisocyanate_mw=164.16,
        diisocyanate_nco_eq=82.08,
        target_nco_oh_ratio=1.05,
    )
    print("Polyurethane batch validation demo")
    print(result)
    return result
