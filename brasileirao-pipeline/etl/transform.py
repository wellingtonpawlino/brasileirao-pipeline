import os
import json
import pandas as pd

# Função para extrair dados de partidas de um JSON aninhado
def extract_match_data(partidas):
    match_data = []
    for fase, chaves in partidas.items():
        for chave, jogos in chaves.items():
            for tipo_jogo, detalhes in jogos.items():
                match_info = {
                    'partida_id': detalhes.get('partida_id'),
                    'data_realizacao': detalhes.get('data_realizacao'),
                    'hora_realizacao': detalhes.get('hora_realizacao'),
                    'time_mandante': detalhes.get('time_mandante', {}).get('nome_popular'),
                    'time_visitante': detalhes.get('time_visitante', {}).get('nome_popular'),
                    'status': detalhes.get('status')
                }
                match_data.append(match_info)
    return match_data

# Caminhos de entrada e saída
input_path = os.path.join("..", "data", "bronze", "partidas_serie_a_2025.json")
output_path = os.path.join("..", "data", "silver", "partidas_serie_a_2025.csv")

try:
    # Carregar os dados brutos (JSON)
    with open(input_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)
    
    # Extrair dados das partidas
    partidas = raw_data.get('partidas', {}).get('partidas', {})
    match_data = extract_match_data(partidas)
    
    # Criar DataFrame
    df = pd.DataFrame(match_data)
    
    # Padronizar nomes das colunas
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    
    # Converter tipos de dados
    df['data_realizacao'] = pd.to_datetime(df['data_realizacao'], errors='coerce')
    df['hora_realizacao'] = pd.to_datetime(df['hora_realizacao'], format='%H:%M', errors='coerce').dt.time
    
    # Limpeza de dados
    df.dropna(inplace=True)           # Remove registros com dados ausentes
    df.drop_duplicates(inplace=True)  # Remove duplicatas
    
    # Salvar os dados transformados
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False, encoding="utf-8")
    
    print("✅ Transformação concluída com sucesso.")
except Exception as e:
    print(f"❌ Erro na transformação: {e}")