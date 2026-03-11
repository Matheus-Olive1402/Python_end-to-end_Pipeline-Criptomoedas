import pandas as pd
from pathlib import Path

def transform():

    base_path = Path(__file__).resolve().parent.parent
    input_file = base_path / "data" / "raw" / "crypto_raw.csv"
    output_dir = base_path / "data" / "processed"
    output_file = output_dir / "crypto_processed.parquet"

    df = pd.read_csv(input_file)

    df["price_change_pct"] = df["price_change_percentage_24h"]
    df["volatility"] = df["high_24h"] - df["low_24h"]

    df.to_parquet(output_file, index=False)

    return df