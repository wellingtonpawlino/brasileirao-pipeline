
# Brasileirão Pipeline

Este projeto cria um pipeline de dados para o Campeonato Brasileiro Série A usando a API-Futebol.

## Estrutura do Projeto

- `dags/`: DAGs do Airflow
- `etl/`: Scripts de ETL
- `data/bronze/`: Dados brutos
- `data/silver/`: Dados transformados
- `data/gold/`: Dados enriquecidos
- `inputs/`: Arquivos de configuração (ex: `config.json`)
- `notebooks/`: Análises exploratórias

## Instruções

1. Adicione sua chave da API-Futebol no arquivo `inputs/config.json`.
2. Suba o projeto para o GitHub.
3. Crie os scripts de extração, transformação e carregamento.
4. Configure e execute os DAGs no Airflow.

## Dependências

- Python 3.x
- Bibliotecas: requests, pandas, pyspark, airflow, etc.
