import string

def eh_palindromo(texto: str) -> str:
    # Remove espaços e pontuação, e coloca tudo em minúsculas
    texto_limpo = "".join(
        char.lower() for char in texto if char.isalnum()
    )

    # Verifica se é igual de frente pra trás
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"


# Exemplo de uso:
frase = input("Digite uma palavra ou frase: ")
resultado = eh_palindromo(frase)
print("É palíndromo? ", resultado)
