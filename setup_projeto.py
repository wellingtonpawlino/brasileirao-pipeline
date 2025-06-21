import os
import json

# Diretórios do projeto
dirs = [
    "brasileirao-pipeline/dags",
    "brasileirao-pipeline/etl",
    "brasileirao-pipeline/data/bronze",
    "brasileirao-pipeline/data/silver",
    "brasileirao-pipeline/data/gold",
    "brasileirao-pipeline/inputs",
    "brasileirao-pipeline/notebooks"
]

# Criar diretórios
for dir in dirs:
    os.makedirs(dir, exist_ok=True)

# Criar config.json com campo para a API key
config_content = {
    "api_key": "SUA_API_KEY_AQUI"
}
with open("brasileirao-pipeline/inputs/config.json", "w") as f:
    json.dump(config_content, f, indent=4)

# Criar README.md com descrição básica
readme_content = """
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
"""
with open("brasileirao-pipeline/README.md", "w") as f:
    f.write(readme_content)
