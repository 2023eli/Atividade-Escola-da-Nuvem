import requests

print("=== Busca de Usuário Fictício Aleatório ===")

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url)

    # Verifica se a resposta foi OK (código 200)
    if resposta.status_code == 200:
        dados = resposta.json()

        usuario = dados["results"][0]

        nome_completo = f'{usuario["name"]["title"]} {usuario["name"]["first"]} {usuario["name"]["last"]}'
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print("\n=== Usuário Encontrado ===")
        print(f"Nome : {nome_completo}")
        print(f"E-mail: {email}")
        print(f"País : {pais}")
    else:
        print("Falha ao buscar usuário. Código de status:", resposta.status_code)

except requests.exceptions.RequestException:
    print("Falha na conexão com a API. Verifique sua internet e tente novamente.")
