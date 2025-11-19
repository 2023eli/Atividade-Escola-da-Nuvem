from datetime import datetime

print("=== Calculadora de Dias de Vida ===")

# Solicita a data de nascimento
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte para objeto de data
dia, mes, ano = map(int, data_nascimento.split("/"))
data_nascimento = datetime(ano, mes, dia)

# Data atual
data_atual = datetime.now()

# Calcula diferença em dias
dias_vivo = (data_atual - data_nascimento).days

print(f"\nVocê está vivo há aproximadamente {dias_vivo} dias.")
