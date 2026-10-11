from polymer_platform.chem.formulas import molecular_weight_from_formula
from polymer_platform.chem.validation import validate_polyurethane_batch
from polymer_platform.db.sqlite_store import init_database


def test_formula_weight() -> None:
    assert abs(molecular_weight_from_formula("H2O") - 18.015) < 1e-3


def test_polyurethane_batch_checks() -> None:
    result = validate_polyurethane_batch(
        polyol_formula="C3H8O2",
        polyol_mw=92.094,
        polyol_oh_eq=46.047,
        diisocyanate_formula="C8H8N2O2",
        diisocyanate_mw=164.16,
        diisocyanate_nco_eq=82.08,
        target_nco_oh_ratio=1.05,
    )
    assert result["status"] in {"ok", "needs_review"}


def test_init_database() -> None:
    init_database()
    assert True
