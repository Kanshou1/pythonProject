import random

print('------------------------------------------------------')
print('                 Jogo Advinha o Numero')
print('------------------------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('jogador qual e o seu nome? ')

while guess != the_number:
    guess_text = input('advinha um numero entre 1 e 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('desculpe {}, seu chute de {} foi muito BAIXO.'.format(name, guess))

    elif guess > the_number:
        print('desculpe {}, seu chute de {} foi muito ALTO.'.format(name, guess))
    else:
        print('Otimo {}, voce acertou! o numero era {}'.format(name, guess))

