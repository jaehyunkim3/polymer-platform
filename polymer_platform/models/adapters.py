from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class ModelAdapter(ABC):
    name: str = "base"

    @abstractmethod
    def predict(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        """Return prediction with uncertainty metadata."""


class TransPolymerAdapter(ModelAdapter):
    name = "TransPolymer"

    def predict(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        return {
            "model": self.name,
            "status": "not_enabled",
            "message": "TransPolymer dependency and input schema are not yet configured in this base scaffold.",
            "prediction": None,
            "uncertainty": None,
        }


class PolymerGNNAdapter(ModelAdapter):
    name = "PolymerGNN"

    def predict(self, *args: Any, **kwargs: Any) -> dict[str, Any]:
        return {
            "model": self.name,
            "status": "not_enabled",
            "message": "PolymerGNN dependency and graph conversion pipeline are not yet configured in this base scaffold.",
            "prediction": None,
            "uncertainty": None,
        }


class ModelRegistry:
    def __init__(self) -> None:
        self._models: dict[str, ModelAdapter] = {
            "TransPolymer": TransPolymerAdapter(),
            "PolymerGNN": PolymerGNNAdapter(),
        }

    def get(self, name: str) -> ModelAdapter:
        try:
            return self._models[name]
        except KeyError as exc:
            raise ValueError(f"Unknown model name: {name}") from exc

    def available(self) -> list[str]:
        return list(self._models.keys())
