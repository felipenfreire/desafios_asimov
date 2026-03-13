numero_secreto = 16
descobriu = False

for n in range(3):
    if not descobriu:
        chute = int(input('tente acertar o número secreto: '))
        if chute < numero_secreto:
            print('Chute muito abaixo!')
        elif chute > numero_secreto:
            print('Chute muito acima!')
        else:
            print('Descobriu!')
            descobriu = True

if descobriu:
    print('Parabéns, você acertou o múmero da sorte')
else:
    print(f'Que pana, você errou as 3 tentativas o numero secreto era {numero_secreto}')
    