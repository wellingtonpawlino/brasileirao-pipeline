import os
import pandas as pd

# Caminhos
input_path = os.path.join("..", "data", "silver", "partidas_serie_a_2025.csv")
csv_output = os.path.join("..", "data", "gold", "tabela_classificacao.csv")
parquet_output = csv_output.replace(".csv", ".parquet")

# Carregar partidas transformadas
df = pd.read_csv(input_path)

# Criar tabela base com colunas: time, jogos, vitorias, empates, derrotas, pontos
tabela = {}

for _, row in df.iterrows():
    mandante = row['time_mandante']
    visitante = row['time_visitante']
    
    # Simulação de status (você pode adaptar depois para incluir placares reais)
    status = row.get('status', '').lower()
    
    for time in [mandante, visitante]:
        if time not in tabela:
            tabela[time] = {"jogos": 0, "vitorias": 0, "empates": 0, "derrotas": 0, "pontos": 0}
        tabela[time]["jogos"] += 1

    # Exemplo de distribuição de pontos fictícia (você pode ajustar com placares reais)
    if status == "finalizado":
        # Simulação aleatória: mandante venceu
        tabela[mandante]["vitorias"] += 1
        tabela[visitante]["derrotas"] += 1
        tabela[mandante]["pontos"] += 3
    else:
        tabela[mandante]["empates"] += 1
        tabela[visitante]["empates"] += 1
        tabela[mandante]["pontos"] += 1
        tabela[visitante]["pontos"] += 1

# Criar DataFrame final e ordenar
df_tabela = pd.DataFrame.from_dict(tabela, orient="index").reset_index()
df_tabela = df_tabela.rename(columns={"index": "time"}).sort_values(by=["pontos", "vitorias"], ascending=False)

# Salvar
os.makedirs(os.path.dirname(csv_output), exist_ok=True)
df_tabela.to_csv(csv_output, index=False, encoding="utf-8")
df_tabela.to_parquet(parquet_output, index=False)

print("🏆 Tabela de classificação criada e salva na camada gold!")