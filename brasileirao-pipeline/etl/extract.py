import requests
import json
import os

# Caminho para o config.json
config_path = os.path.join("..", "inputs", "config.json")

# Carregar a chave da API
with open(config_path, encoding="utf-8") as f:
    config = json.load(f)

api_key = config.get("api_key")
if not api_key:
    raise ValueError("❌ 'api_key' não encontrada no config.json")

# Cabeçalho da requisição
headers = {
    "Authorization": f"Bearer {api_key}"
}

# Endpoint da Série A
url = "https://api.api-futebol.com.br/v1/campeonatos/10/partidas"

# Requisição com tratamento de erros
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print(f"❌ Erro na requisição: {e}")
    exit()

# Dados retornados
partidas = response.json()

# Caminho de saída
output_path = os.path.join("..", "data", "bronze", "partidas_serie_a_2025.json")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Salvar como JSON formatado
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(partidas, f, indent=4, ensure_ascii=False)

print("✅ Dados das partidas da Série A 2025 extraídos com sucesso.")