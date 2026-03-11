import requests
import pandas as pd
from pathlib import Path

url = "https://api.coingecko.com/api/v3/coins/markets"

# diretorio
script_path = Path(__file__).resolve()
project_root = script_path.parent.parent
output_dir = project_root / "data" / "raw"
output_file = output_dir / "crypto_raw.csv"


params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

response = requests.get(url, params=params)

data = pd.DataFrame(response.json())

data.to_csv(output_file, index=False)