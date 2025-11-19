print("=== Conversor de Temperatura ===")

temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Unidade de destino (C/F/K): ").upper()

# Converte a origem para Celsius primeiro
if origem == "C":
    temp_c = temp
elif origem == "F":
    temp_c = (temp - 32) * 5/9
elif origem == "K":
    temp_c = temp - 273.15
else:
    print("Unidade de origem inválida!")
    exit()

# Converte de Celsius para destino
if destino == "C":
    temp_convertida = temp_c
elif destino == "F":
    temp_convertida = (temp_c * 9/5) + 32
elif destino == "K":
    temp_convertida = temp_c + 273.15
else:
    print("Unidade de destino inválida!")
    exit()

print(f"\nResultado: {temp_convertida:.2f}°{destino}")
