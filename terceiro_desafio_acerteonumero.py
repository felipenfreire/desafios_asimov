numero_secreto = 16
descobriu = False

if not descobriu:
    chute_usuario = int(input('Tente adivinhar o número secreto: '))
    if chute_usuario < numero_secreto:
        print('Chute abaixo do número secreto ); ')
    elif chute_usuario > numero_secreto:
        print('Chute acima do número secreto ); ')
    else:
        print('Parabéns você acertou o número da sorte (: ')
        descobriu = True

if not descobriu:
    chute_usuario = int(input('Tente adivinhar o número secreto: '))
    if chute_usuario < numero_secreto:
        print('Chute abaixo do número secreto ); ')
    elif chute_usuario > numero_secreto:
        print('Chute acima do número secreto ); ')
    else:
        print('Parabéns você acertou o número da sorte (: ')
        descobriu = True
    

if not descobriu:
    chute_usuario = int(input('Tente adivinhar o número secreto: '))
    if chute_usuario < numero_secreto:
        print('Chute abaixo do número secreto ); ')
    elif chute_usuario > numero_secreto:
        print('Chute acima do número secreto ); ')
    else:
        print('Parabéns você acertou o número da sorte (: ')
        descobriu = True



if descobriu:
    print('Parabens você ganhou')
else:
    print(f'Que pena você erros as 3 tentativas, o número secreto era {numero_secreto}')
   



