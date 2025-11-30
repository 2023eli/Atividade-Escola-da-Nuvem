import csv

arquivo = input("Digite o nome do arquivo CSV: ")

try:
    with open(arquivo, "r", encoding="utf-8") as f:
        leitor = csv.DictReader(f)

        tempos = []

        for linha in leitor:
            try:
                tempo = float(linha["tempo_execucao"])
                tempos.append(tempo)
            except ValueError:
                print("Aviso: valor inválido ignorado:", linha["tempo_execucao"])

        if len(tempos) == 0:
            print("Nenhum valor válido encontrado na coluna 'tempo_execucao'.")
        else:
            media = sum(tempos) / len(tempos)
            maior = max(tempos)

            print(f"\nMédia da coluna tempo_execucao: {media:.2f}")
            print(f"Maior valor da coluna tempo_execucao: {maior:.2f}")

except FileNotFoundError:
    print("Erro: O arquivo informado não foi encontrado.")
except Exception as e:
    print("Erro ao ler o arquivo:", e)
