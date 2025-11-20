import random
import string

print("=== Gerador de Senhas Aleatórias ===")

# Tamanho da senha
tamanho = int(input("Digite o tamanho desejado para a senha: "))

# Conjunto de caracteres permitidos
letras = string.ascii_letters     # a-z A-Z
numeros = string.digits           # 0-9
simbolos = string.punctuation     # !@#$%¨&*()

# Combina todos os caracteres
todos_caracteres = letras + numeros + simbolos

# Gera a senha
senha = "".join(random.choice(todos_caracteres) for _ in range(tamanho))

print(f"\nSua senha gerada é: {senha}")
