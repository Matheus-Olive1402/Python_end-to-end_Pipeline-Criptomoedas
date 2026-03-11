import streamlit as st
import duckdb
import pandas as pd

st.title("Crypto Data Pipeline Dashboard")

con = duckdb.connect("data/warehouse/crypto.db")

df = con.execute("""
SELECT name,
       market_cap,
       price_change_percentage_24h
FROM crypto
ORDER BY market_cap DESC
LIMIT 10
""").df()

st.subheader("Top 10 Criptomoedas por Market Cap")

st.dataframe(df)

st.bar_chart(
    df.set_index("name")["market_cap"]
)