# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos


nome = input('Digite seu nome: ')
idade = int(input('Digite a sua idade: '))

print(f'Olá {nome}!')
print(f'seu nome tem {len(nome)} Letras.')
print(f'daqui a 5 anos vc terá {idade + 5} anos')
