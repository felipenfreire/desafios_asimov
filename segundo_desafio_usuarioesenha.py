# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
# variávies dentro do próprio código.

usuario_correto = 'Felipe123'
senha_correta  = 'Felipe321'

usuario = input('Digite seu nome de usuário: ')
senha = input('Digite a sua senha: ')

if usuario == usuario_correto:
    if senha == senha_correta:
        print(f'Bem vindo {usuario}, login feito com sucesso :) ')
    elif senha != senha_correta:
        print(f'Senha incorreta para o usuário {usuario}')
else:
    print(f'Usuário {usuario} não encontrado em nosso banco de dados ); ')

    
    

