"""Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""
# Conversor de Moeda
# Converte um valor em reais para dólares e euros

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolar = valor_reais / taxa_dolar
valor_em_euro = valor_reais / taxa_euro

print("Valor em reais: R$", valor_reais)
print("Em dólares: US$ {:.2f}".format(valor_em_dolar))
print("Em euros: € {:.2f}".format(valor_em_euro))