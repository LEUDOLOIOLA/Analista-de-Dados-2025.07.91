#pedindo usuario e senha
usuario = input("Digite seu usuário: ")
senha = input("Digite sua senha: ")
#verificando se usuario e senha estao corretos
if usuario == "admin" and senha == "password":
    print("Login bem-sucedido!")
else:
    print("Usuário ou senha incorretos.")

if usuario != "admin":
    print("Aceso negado: usuário inválido.")
elif senha != "password":
    print("Acesso negado: senha incorreta.")

#fim do programa




