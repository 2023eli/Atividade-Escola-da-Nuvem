print("=== Registro de Notas e Média da Turma ===")

notas = []  # lista para armazenar as notas

while True:
    nota = float(input("Digite a nota do aluno (0 a 10): "))
    
    # opcional: validação
    if nota < 0 or nota > 10:
        print("Nota inválida! Digite um valor entre 0 e 10.")
        continue

    notas.append(nota)

    continuar = input("Deseja adicionar outra nota? (s/n): ").lower()
    if continuar != "s":
        break

# Cálculo da média
media = sum(notas) / len(notas)

print(f"\nQuantidade de alunos: {len(notas)}")
print(f"Média da turma: {media:.2f}")
