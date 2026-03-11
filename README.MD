# Objetivo

Esse projeto tem como objetivo primario um reforço a minha aprendizagem com eng. dados, no caso a ideia foi criar um pipeline de dados de criptomoedas, ele vai trazer os valores das moedas criptos e exibir em um dash.
No caso além de um pipeline de data-driven e valido reforçar a utilização do git para subir projetos.

## Execução
execute no terminal 'python3 main.py' para realizar o pipeline primeiro vai extrair os dados de uma API e enviara para um dataframe, vai realizar a transformação para parquet e por fim vai carregar os dados para um banco de dados no caso o DuckDB.

execute no terminal 'streamlit run dashboard/app.py' para criar no seu localhost o dashboard de forma simples.


## Arquitetura

```mermaid
graph LR
A[API] --> B(ETL)
B --> C(Data Lake)
C --> D(Data Warehouse)
D --> E[Dashboard]
```

## Stack

<h4> Python
<h4> Pandas
<h4> Parquet
<h4> DuckDB
<h4> streamlit


## lib
Pandas == 2.3.3<br>
pip-tools == 7.5.3<br>
requests == 2.32.5<br>
duckdb==1.5.0<br>
pyarrow==23.0.1<br>
streamlit==1.55.0


## linux
Criação de ambiente<br>
sudo apt update, sudo apt install python3-venv, python3 -m venv .venv, source .venv/bin/activate<br>
pip-compile requirements.in