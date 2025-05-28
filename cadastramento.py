def cadastramento():
    nome = input("crie um nome de usuário:")
    senha = input("crie uma senha:")
    cadastro = input("digite novamente o nome de usuário:")
    senha1 = input("digite novamente a senha:")

    while cadastro != nome or senha1 != senha:
        print ("Tente Novamente")

    cadastro = input("digite novamente o nome de usuário:")
    
    senha1 = input("digite novamente a senha:")
    print ("login bem-sucedido.") 

cadastramento()