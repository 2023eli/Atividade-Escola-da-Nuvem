print("=== Calculadora de Desconto ===")

# Entrada dos dados
preco = float(input("Digite o preço do produto (R$): "))
porcentagem = float(input("Digite a porcentagem de desconto (%): "))

# Cálculo do valor do desconto
valor_desconto = preco * (porcentagem / 100)

# Cálculo do preço final
preco_final = preco - valor_desconto

# Saída formatada
print(f"\nValor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final do produto: R$ {preco_final:.2f}")
