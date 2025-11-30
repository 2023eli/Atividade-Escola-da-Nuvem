import json

def salvar_dados_json(nome_arquivo, dados):
    """Salva um dicionário em um arquivo JSON."""
    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print("✔ Dados salvos com sucesso!")
    except Exception as erro:
        print(f"❌ Falha ao salvar o arquivo: {erro}")


def ler_dados_json(nome_arquivo):
    """Lê um arquivo JSON e retorna os dados."""
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        print("❌ Arquivo não encontrado!")
    except Exception as erro:
        print(f"❌ Erro ao ler o arquivo: {erro}")


# --- Programa principal ---

# Criando o dicionário com nome, idade e cidade
dados_pessoa = {
    "nome": "Elisangela",
    "idade": 32,
    "cidade": "Belém"
}

arquivo_json = "dados_pessoa.json"

# Salvando os dados no arquivo
salvar_dados_json(arquivo_json, dados_pessoa)

# Lendo os dados do arquivo
dados_lidos = ler_dados_json(arquivo_json)

# Exibindo os dados, caso tenham sido lidos com sucesso
if dados_lidos:
    print("\n📄 Dados encontrados no arquivo:")
    print(f"Nome: {dados_lidos['nome']}")
    print(f"Idade: {dados_lidos['idade']}")
    print(f"Cidade: {dados_lidos['cidade']}")

