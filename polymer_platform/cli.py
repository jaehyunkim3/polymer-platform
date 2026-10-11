from __future__ import annotations

import argparse

from polymer_platform.db.seed import seed_default_materials
from polymer_platform.db.sqlite_store import init_database, list_materials, list_experiments
from polymer_platform.examples.polyurethane_demo import run_demo


def cmd_init_db(_: argparse.Namespace) -> int:
    init_database()
    print("Database initialized at polymer_platform.db")
    return 0


def cmd_seed_db(_: argparse.Namespace) -> int:
    seed_default_materials()
    print("Seed materials inserted.")
    return 0


def cmd_smoke_test(_: argparse.Namespace) -> int:
    from polymer_platform.chem.formulas import molecular_weight_from_formula
    from polymer_platform.chem.validation import validate_polyurethane_batch

    mw = molecular_weight_from_formula("C3H8O2")
    result = validate_polyurethane_batch(
        polyol_formula="C3H8O2",
        polyol_mw=mw,
        polyol_oh_eq=1.0,
        diisocyanate_formula="C8H8N2O2",
        diisocyanate_mw=164.0,
        diisocyanate_nco_eq=1.0,
        target_nco_oh_ratio=1.05,
    )

    print(f"Example formula molecular weight: {mw}")
    print(result)
    print("Smoke test passed.")
    return 0


def cmd_polyurethane_demo(_: argparse.Namespace) -> int:
    run_demo()
    return 0


def cmd_show_materials(_: argparse.Namespace) -> int:
    for row in list_materials():
        print(row)
    return 0


def cmd_show_experiments(_: argparse.Namespace) -> int:
    for row in list_experiments():
        print(row)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Polymer platform CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init-db", help="Initialize the SQLite DB")
    init_parser.set_defaults(func=cmd_init_db)

    seed_parser = subparsers.add_parser("seed-db", help="Insert default materials")
    seed_parser.set_defaults(func=cmd_seed_db)

    smoke_parser = subparsers.add_parser("smoke-test", help="Run a basic chemistry smoke test")
    smoke_parser.set_defaults(func=cmd_smoke_test)

    demo_parser = subparsers.add_parser("polyurethane-demo", help="Run a polyurethane example")
    demo_parser.set_defaults(func=cmd_polyurethane_demo)

    materials_parser = subparsers.add_parser("show-materials", help="List registered materials")
    materials_parser.set_defaults(func=cmd_show_materials)

    experiments_parser = subparsers.add_parser("show-experiments", help="List experiment records")
    experiments_parser.set_defaults(func=cmd_show_experiments)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)
