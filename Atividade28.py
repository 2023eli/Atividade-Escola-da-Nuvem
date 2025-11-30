import pandas as pd

try:
    # Lê o arquivo CSV
    df = pd.read_csv("dados.csv")  # substitua por outro nome se necessário

    # Calcula média e mediana da coluna tempo_execucao
    media = df["tempo_execucao"].mean()
    mediana = df["tempo_execucao"].median()

    # Exibe resultados
    print(f"Média do tempo de execução: {media}")
    print(f"Mediana do tempo de execução: {mediana}")

except FileNotFoundError:
    print("Erro: Arquivo CSV não encontrado.")
except Exception as e:
    print(f"Erro ao ler o arquivo: {e}")
