#!/usr/bin/env python3
"""
Generate N anonymized CSV files with synthetic transaction data.

Usage
-----
python generate_anonymized_transactions.py \
       --n_files 5 \
       --base_rows 5_000 \
       --row_delta 500 \
       --out_dir ./data/generated

* Each file gets a different row count:
    rows_i = base_rows + random.uniform(-row_delta, +row_delta)
* Filenames follow: transactions_anonymized_<idx>_<rows>rows.csv
"""

import argparse
from pathlib import Path
import numpy as np
import pandas as pd

# --------------------------------------------------------------------------- #
# Schema helpers
# --------------------------------------------------------------------------- #

TRANSACTION_TYPES = ["deposit", "withdrawal", "transfer", "payment"]
LOCATIONS = ["NY", "CA", "TX", "FL", "IL"]

def make_dataframe(n_rows: int, seed: int | None = None) -> pd.DataFrame:
    """Return a DataFrame with `n_rows` rows of anonymized transaction data."""
    rng = np.random.default_rng(seed)
    data = {
        "transaction_id_anonymized": np.arange(1, n_rows + 1),
        "client_id_anonymized": rng.integers(1000, 1100, size=n_rows),
        "transaction_amount_anonymized": rng.uniform(10.0, 15_000.0, size=n_rows),
        "transaction_type_anonymized": rng.choice(TRANSACTION_TYPES, size=n_rows),
        "transaction_date_anonymized": pd.date_range(
            start="2023-01-01", periods=n_rows, freq="H"
        ),
        "compliance_flag_anonymized": rng.choice([True, False], size=n_rows, p=[0.9, 0.1]),
        "account_balance_anonymized": rng.uniform(100.0, 100_000.0, size=n_rows),
        "location_anonymized": rng.choice(LOCATIONS, size=n_rows),
    }
    return pd.DataFrame(data)


def parse_args() -> argparse.Namespace:
    """Parse script arguments."""
    
    parser = argparse.ArgumentParser(
        description="Generate anonymized CSV files for synthetic transactions."
    )
    parser.add_argument("--n_files", type=int, required=True, help="Number of CSV files.")
    parser.add_argument(
        "--base_rows",
        type=int,
        default=5_000,
        help="Approximate row count for the first file.",
    )
    parser.add_argument(
        "--row_delta",
        type=int,
        default=500,
        help="Maximum ±delta to vary row counts between files.",
    )
    parser.add_argument(
        "--out_dir",
        type=Path,
        default=Path("./data/generated"),
        help="Output directory for the CSV files.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional random seed for reproducibility.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)

    for i in range(1, args.n_files + 1):
        # Jitter the row count
        delta = rng.integers(-args.row_delta, args.row_delta + 1)
        n_rows = max(1, args.base_rows + delta)

        df = make_dataframe(n_rows, seed=rng.integers(0, 2**32 - 1))
        filename = args.out_dir / f"transactions_anonymized_{i}_{n_rows}rows.csv"
        df.to_csv(filename, index=False)
        print(f"Saved {filename} ({n_rows} rows)")

    print(f"\n✔ Generated {args.n_files} anonymized CSV file(s) in {args.out_dir.resolve()}")

if __name__ == "__main__":
    main()
