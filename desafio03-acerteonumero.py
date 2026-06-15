# Desafio - Crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#  - se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

numero_secreto = 16
descobriu = False

if not descobriu:
    chute = int(input('Tente adivinhar o número secreto: '))
    if chute < numero_secreto:
        print('Chute foi baixo!')
    elif chute > numero_secreto:
        print('Chute foi alto')
    else:
        print('Vc acertou!!')
    descobriu = True

if not descobriu:
    chute = int(input('Tente adivinhar o número secreto: '))
    if chute < numero_secreto:
        print('Chute foi baixo!')
    elif chute > numero_secreto:
        print('Chute foi alto')
    else:
        print('Vc acertou!!')
    descobriu = True

if not descobriu:
    chute = int(input('Tente adivinhar o número secreto: '))
    if chute < numero_secreto:
        print('Chute foi baixo!')
    elif chute > numero_secreto:
        print('Chute foi alto')
    else:
        print('Vc acertou!!')
    descobriu = True


if descobriu:
    print('Parabens, você acertou o número secreto!')
else:
    print(f'Que pena você errou as 3 tentativas, o número secreto era {numero_secreto}')