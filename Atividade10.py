while True:
    senha = input("Digite a sua senha: ")
    
    if senha.lower() == "sair":
        
        print("Programa encerrado")
        break
    tem_oito_caracteres = len(senha) >= 8
    
    tem_numero = any(caractere.isdigit() for caractere in senha)
    
    eh_forte = tem_oito_caracteres and tem_numero
    
    if eh_forte:
        print("Parabéns. Sua senha é muito forte")
        break
    else:
        print("Que pena. Sua senha está muito fraca")
        
    if not tem_oito_caracteres:
        print("A senha tem que ter pelo menos 8 caracteres")
    if not tem_numero:
        print("A senha tem que ter pelo menos 1 número")
        
         
    
    
    
    