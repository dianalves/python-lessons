"""
Seção 7 - Exercicio 5

Faça um algoritmo que leia um nome de usuario e a sua senha
e não aceite a senha igual ao nome do usuario, mostrando uma
mensagem de erro e voltando a pedir as informações.

"""

usuario = input("Digite seu usuario: ")
senha = input("Digite sua senha: ")
while usuario == senha:
    print("Erro: Nome de usuario e senha devem ser diferentes")
    usuario = input("Digite seu usuario:")
    senha = input("Digite sua senha: ")
