from __future__ import annotations

import sqlite3
from pathlib import Path

from polymer_platform.config import DATABASE_PATH

SCHEMA_PATH = Path(__file__).with_name("schema.sql")


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_database() -> None:
    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = get_connection()
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()


def insert_material(material: dict) -> int:
    conn = get_connection()
    cur = conn.execute(
        """
        INSERT INTO materials (
            name, category, formula, smiles, molecular_weight,
            oh_equivalent, nco_equivalent, source, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            material.get("name"),
            material.get("category"),
            material.get("formula"),
            material.get("smiles"),
            material.get("molecular_weight"),
            material.get("oh_equivalent"),
            material.get("nco_equivalent"),
            material.get("source"),
            material.get("notes"),
        ),
    )
    conn.commit()
    material_id = cur.lastrowid
    conn.close()
    return material_id


def list_materials() -> list[dict]:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM materials ORDER BY id").fetchall()
    conn.close()
    return [dict(row) for row in rows]


def insert_experiment(record: dict) -> int:
    conn = get_connection()
    cur = conn.execute(
        """
        INSERT INTO experiments (
            project_name, material_name, property_name,
            measured_value, predicted_value, error_value,
            uncertainty, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            record.get("project_name"),
            record.get("material_name"),
            record.get("property_name"),
            record.get("measured_value"),
            record.get("predicted_value"),
            record.get("error_value"),
            record.get("uncertainty"),
            record.get("notes"),
        ),
    )
    conn.commit()
    exp_id = cur.lastrowid
    conn.close()
    return exp_id


def list_experiments() -> list[dict]:
    conn = get_connection()
    rows = conn.execute("SELECT * FROM experiments ORDER BY id").fetchall()
    conn.close()
    return [dict(row) for row in rows]
