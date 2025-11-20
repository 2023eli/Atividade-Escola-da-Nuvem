import requests

print("=== Consulta de Cotação em relação ao Real (BRL) ===")

moeda = input("Digite o código da moeda (ex: USD, EUR, ARS): ").upper()

url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

try:
    resposta = requests.get(url, timeout=5)

    if resposta.status_code == 200:
        dados = resposta.json()
        
        # A chave vem no formato "USDBRL", "EURBRL", etc.
        chave = f"{moeda}BRL"

        if chave in dados:
            info = dados[chave]

            valor_atual = float(info["bid"])
            maxima = float(info["high"])
            minima = float(info["low"])
            data_hora = info["create_date"]

            print("\n=== Informações da Moeda ===")
            print(f"Moeda consultada: {moeda}/BRL")
            print(f"Valor atual : R$ {valor_atual:.4f}")
            print(f"Máximo dia : R$ {maxima:.4f}")
            print(f"Mínimo dia : R$ {minima:.4f}")
            print(f"Última atualização: {data_hora}")
        else:
            print("\n❌ Moeda não encontrada. Verifique o código informado.")
    else:
        print("\n❌ Erro na requisição. Código HTTP:", resposta.status_code)

except requests.exceptions.RequestException:
    print("\n❌ Erro na conexão com a API. Verifique sua internet e tente novamente.")
