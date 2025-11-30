import csv

# Dados das pessoas
pessoas = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 28, "Belém"],
    ["Carlos", 35, "Ananindeua"],
    ["Mariana", 22, "Castanhal"]
]

try:
    # Usuário escolhe o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")

    # Abre o arquivo e escreve em formato tabular
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as file:
        escritor = csv.writer(file)
        escritor.writerows(pessoas)

    print(f"Arquivo '{nome_arquivo}' salvo com sucesso!")

except Exception as e:
    print(f"Falha ao salvar o arquivo: {e}")
