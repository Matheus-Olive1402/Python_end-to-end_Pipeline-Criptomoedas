# Objetivo

Esse projeto tem como objetivo primario um reforço a minha aprendizagem com eng. dados, no caso a ideia foi criar um pipeline de dados de criptomoedas.
No caso além de um pipeline de data-driven e valido reforçar a utilização do git para subir projetos.


## Arquitetura

```mermaid
graph LR
A[API] --> B(ETL)
B --> C(Data Lake)
C --> D(Data Warehouse)
D --> E[Dashboard]
```

## Stack

-Python
-Pandas
-Docker
-PostgreSQL
-Power BI (a pensar)