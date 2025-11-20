import requests

def consultar_cep(cep: str):
    # Mantém só os números do CEP
    cep = ''.join(filter(str.isdigit, cep))

    # Validação simples do CEP (8 dígitos)
    if len(cep) != 8:
        print("CEP inválido. Digite um CEP com 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()  # lança erro se o status não for 200

        dados = resposta.json()

        # A API ViaCEP devolve {"erro": true} quando o CEP não existe
        if dados.get("erro"):
            print("CEP não encontrado.")
            return

        logradouro = dados.get("logradouro", "Não informado")
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "Não informado")
        estado = dados.get("uf", "Não informado")

        print("\nResultado da consulta:")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro:     {bairro}")
        print(f"Cidade:     {cidade}")
        print(f"Estado:     {estado}")

    except requests.RequestException:
        print("Falha na requisição. Verifique sua conexão ou tente novamente.")

def main():
    cep = input("Digite o CEP (apenas números): ")
    consultar_cep(cep)

if __name__ == "__main__":
    main()