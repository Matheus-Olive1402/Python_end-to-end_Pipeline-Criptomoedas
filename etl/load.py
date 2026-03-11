import duckdb
import pandas as pd
from pathlib import Path

# 
base_path = Path(__file__).resolve().parent.parent
input_file = base_path / "data" / "processed" / "crypto_processed.parquet"
db_path = base_path / "crypto.db"

# Leitura do dado processado
df = pd.read_parquet(input_file)

# Conexão com o DuckDB
with duckdb.connect(str(db_path)) as con:

    con.execute("""
        CREATE TABLE IF NOT EXISTS crypto AS 
        SELECT * FROM df
    """)
    
    # verrificar o sucesso
    result = con.execute("SELECT count(*) FROM crypto").fetchone()
    print(f"Sucesso! {result[0]} linhas inseridas no banco {db_path.name}")