print("=== Classificador de Números ===")

pares = 0
impares = 0

while True:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("→ Esse número é PAR.")
        pares += 1
    else:
        print("→ Esse número é ÍMPAR.")
        impares += 1

    continuar = input("Deseja digitar outro número? (s/n): ").lower()
    if continuar != "s":
        break

print("\n=== Resultado Final ===")
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
