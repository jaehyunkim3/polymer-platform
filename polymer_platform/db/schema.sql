CREATE TABLE IF NOT EXISTS materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT,
    formula TEXT,
    smiles TEXT,
    molecular_weight REAL,
    oh_equivalent REAL,
    nco_equivalent REAL,
    source TEXT,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS experiments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    project_name TEXT,
    material_name TEXT,
    property_name TEXT,
    measured_value REAL,
    predicted_value REAL,
    error_value REAL,
    uncertainty REAL,
    notes TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
