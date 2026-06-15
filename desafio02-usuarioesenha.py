# Desafio - Crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se amobs forem corretos, exibir uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mesnsagem
#quando o usuário está correto, e quando a senha esá incorreta
# - O usuário/senha 'corretos' podem ser definidos como
# variáveis dentro do próprio código.

usuario_cadastrado = 'Felipe@123'
senha_cadastrada = 'Felipe321'

usuario = input('Digite seu nome de usuário: ')
senha = input('Digite a sua senha: ')

if usuario == usuario_cadastrado:
    if senha == senha_cadastrada:
        print(f'Bem vindo {usuario}, Login realizado com sucesso!! ')
    else:
        print(f'Senha incorreta para o usuário {usuario}')
else:
    print(f'Usuário {usuario} não encontrado em nosso banco de dados!')
    
