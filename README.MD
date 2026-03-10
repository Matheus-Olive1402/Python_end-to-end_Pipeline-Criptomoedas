# Objetivo

Esse projeto tem como objetivo primario um reforço a minha aprendizagem com eng. dados, no caso a ideia foi criar um pipeline de dados de criptomoedas.
No caso além de um pipeline de data-driven e valido reforçar a utilização do git para subir projetos.


## Arquitetura

```mermaid
graph LR
A[API] --> B(Round Rect)'
B[ETL] --> C(Round Rect)
C[Data Lake] --> D(Round Rect)
D[Warehouse] --> E(Round Rect)
E[Dashboard]
```

## Stack

Python
Pandas
Docker
PostgreSQL
Power BI (a pensar)