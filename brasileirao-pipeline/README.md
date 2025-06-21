
# Brasileir�o Pipeline

Este projeto cria um pipeline de dados para o Campeonato Brasileiro S�rie A usando a API-Futebol.

## Estrutura do Projeto

- `dags/`: DAGs do Airflow
- `etl/`: Scripts de ETL
- `data/bronze/`: Dados brutos
- `data/silver/`: Dados transformados
- `data/gold/`: Dados enriquecidos
- `inputs/`: Arquivos de configura��o (ex: `config.json`)
- `notebooks/`: An�lises explorat�rias

## Instru��es

1. Adicione sua chave da API-Futebol no arquivo `inputs/config.json`.
2. Suba o projeto para o GitHub.
3. Crie os scripts de extra��o, transforma��o e carregamento.
4. Configure e execute os DAGs no Airflow.

## Depend�ncias

- Python 3.x
- Bibliotecas: requests, pandas, pyspark, airflow, etc.
