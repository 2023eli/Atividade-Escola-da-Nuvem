"""1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).""" 
Idade = input("escreva a sua Idade")

Idade = int(Idade)

if Idade  < 12:
    print("Você é criança")
elif ((Idade > 13) & (Idade <17)):
    print("você é adolescente")
elif ((Idade >17) & (Idade < 59)):
    print("Você é um adulto")
else :
    print("Você é idoso")         
