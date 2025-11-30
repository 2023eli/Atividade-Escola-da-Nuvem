try:
    # Usuário informa o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo para leitura: ")

    # Abre o arquivo e percorre cada linha
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            print(linha.strip())  # strip remove quebras de linha extras

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao ler o arquivo: {e}")
