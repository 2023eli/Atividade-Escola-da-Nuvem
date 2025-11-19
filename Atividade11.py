idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida. Digite um número positivo.")
elif idade <= 12:
    print("Você é uma Criança.")
elif idade <= 17:
    print("Você é um Adolescente.")
elif idade <= 59:
    print("Você é um Adulto.")
else:
    print("Você é um Idoso.")

