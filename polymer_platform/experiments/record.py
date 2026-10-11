from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from polymer_platform.db.sqlite_store import insert_experiment


@dataclass
class ExperimentRecord:
    project_name: str
    material_name: str
    property_name: str
    measured_value: float
    predicted_value: float | None = None
    error_value: float | None = None
    uncertainty: float | None = None
    notes: str = ""

    def to_db_row(self) -> dict[str, Any]:
        if self.predicted_value is not None:
            self.error_value = calculate_prediction_error(self.measured_value, self.predicted_value)
        return {
            "project_name": self.project_name,
            "material_name": self.material_name,
            "property_name": self.property_name,
            "measured_value": self.measured_value,
            "predicted_value": self.predicted_value,
            "error_value": self.error_value,
            "uncertainty": self.uncertainty,
            "notes": self.notes,
        }


def calculate_prediction_error(measured_value: float, predicted_value: float) -> float:
    return abs(measured_value - predicted_value)


def add_experiment_record(record: ExperimentRecord) -> int:
    row = record.to_db_row()
    return insert_experiment(row)
