from __future__ import annotations

from polymer_platform.db.sqlite_store import insert_material


def seed_default_materials() -> list[int]:
    materials = [
        {
            "name": "PEG-400",
            "category": "polyol",
            "formula": "H(OCH2CH2)9OH",
            "smiles": "OCCOCCOCCOCCOCCOCCOCCOCCOCCO",
            "molecular_weight": 400.0,
            "oh_equivalent": 82.0,
            "nco_equivalent": None,
            "source": "internal_seed",
            "notes": "Example polyol for polyurethane formulation checks.",
        },
        {
            "name": "MDI",
            "category": "diisocyanate",
            "formula": "C15H10N2O2",
            "smiles": "O=C=Nc1ccc(cc1)C(=N)c2ccc(N=C=O)cc2",
            "molecular_weight": 250.0,
            "oh_equivalent": None,
            "nco_equivalent": 125.0,
            "source": "internal_seed",
            "notes": "Example aromatic isocyanate.",
        },
        {
            "name": "PTMEG-1000",
            "category": "polyol",
            "formula": "C2H4O",
            "smiles": "OCCOCCOCCOCCOCCOCCOCCOCCOCCOCCO",
            "molecular_weight": 1000.0,
            "oh_equivalent": 56.1,
            "nco_equivalent": None,
            "source": "internal_seed",
            "notes": "High molecular weight polyether polyol.",
        },
    ]

    ids = []
    for material in materials:
        ids.append(insert_material(material))
    return ids
