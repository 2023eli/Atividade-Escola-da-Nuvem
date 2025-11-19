print("=== Verificador de Senha ===")

senha = input("Digite sua senha: ")

# Verifica se tem pelo menos 8 caracteres
criterio_tamanho = len(senha) >= 8

# Verifica se contém pelo menos um número
criterio_numero = any(char.isdigit() for char in senha)

if criterio_tamanho and criterio_numero:
    print("Senha válida! ✔️")
else:
    print("Senha inválida! ❌")
    if not criterio_tamanho:
        print("- A senha deve ter pelo menos 8 caracteres.")
    if not criterio_numero:
        print("- A senha deve conter pelo menos um número.")
