"""
Simple helpers for consistent file IO.
"""
from pathlib import Path
import pandas as pd
import polars as pl

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

def raw_path(*parts) -> Path:
    return DATA_DIR / "raw" / Path(*parts)

def external_path(*parts) -> Path:
    return DATA_DIR / "external" / Path(*parts)

def processed_path(*parts) -> Path:
    p = DATA_DIR / "processed" / Path(*parts)
    p.parent.mkdir(parents=True, exist_ok=True)
    return p

def read_csv(path: Path, engine: str = "pandas"):
    if engine == "pandas":
        return pd.read_csv(path)
    elif engine == "polars":
        return pl.read_csv(path)
    else:
        raise ValueError("engine must be 'pandas' or 'polars'")

def to_csv(df, path: Path):
    if hasattr(df, "to_pandas"):
        df = df.to_pandas()
    df.to_csv(path, index=False)
