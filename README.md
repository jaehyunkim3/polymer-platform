# polymer-platform

A lightweight foundation for a polymer property prediction and experimental validation platform.

The initial version is intentionally conservative:
- core data modeling and DB bootstrap work on CPU
- chemistry validation is implemented with transparent calculations
- AI model integration is adapter-based and optional
- experimental records support prediction-error tracking without forcing any model to run

## Architecture summary

polymer_platform/
- chemistry, validation, and raw-material checks
- SQLite-backed raw material and experiment DB
- experiment record storage and error calculation
- optional AI model adapters (TransPolymer, PolymerGNN, custom models)
- PU example workflow for NCO/OH ratio and batch checks

## Quick start

### 1) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
# or .venv\Scripts\activate  # Windows
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Initialize the local database

```bash
python -m polymer_platform init-db
python -m polymer_platform seed-db
```

### 4) Run smoke test

```bash
python -m polymer_platform smoke-test
```

### 5) Run a polyurethane demo

```bash
python -m polymer_platform polyurethane-demo
```

## Supported early-stage features

- Raw material registry (name, category, molecular formula, OH/NCO equivalent info)
- SQLite database bootstrap
- Chemical validation heuristics:
  - molecular weight calculation from formula
  - OH equivalent and NCO equivalent estimation
  - NCO/OH ratio check for polyurethane recipes
  - unit normalization and batch sanity checks
- Experiment tracking:
  - measured values
  - predicted values
  - error metrics and flags
- AI model integration through adapter interfaces rather than hard dependencies

## Optional AI model adapters

The platform does not force model execution. Instead, adapters are registered and called only when the relevant model is available.

Planned adapters:
- TransPolymer
- PolymerGNN
- custom model adapters for internal lab datasets

## Important development principles

- Keep the base platform CPU-friendly and Jupyter-friendly.
- Do not fabricate predictions when data quality is insufficient.
- Use adapters so model dependency and input schemas remain explicit.
- Keep raw-material and experiment records traceable to sources and measurement conditions.

## Directory structure

```text
polymer-platform/
├── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── polymer_platform/
│   ├── __init__.py
│   ├── __main__.py
│   ├── cli.py
│   ├── config.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── sqlite_store.py
│   │   ├── seed.py
│   │   └── schema.sql
│   ├── chem/
│   │   ├── __init__.py
│   │   ├── formulas.py
│   │   └── validation.py
│   ├── experiments/
│   │   ├── __init__.py
│   │   ├── record.py
│   │   └── validation.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── adapters.py
│   │   └── registry.py
│   ├── examples/
│   │   ├── __init__.py
│   │   └── polyurethane_demo.py
│   └── utils/
│       ├── __init__.py
│       └── units.py
├── tests/
│   └── test_smoke.py
└── .venv/   # local only, not committed
```

## Next phases

This repository is intentionally the foundation.

Planned follow-ups:
1. B: material DB and chemistry module integration
2. D: experiment and validation records
3. C: optional model adapters and input schema wrappers
4. E: polyurethane example workflow and experiment recommendation logic

## License

This project is currently a research-oriented starter scaffold for internal use.

---

Project status: basic scaffold created and runnable.
