import random

print("**********************************")
print("bem vindo ao jogo de adivinhação")
print("**********************************")

numero_secreto = random.randrange(1,1000)
total_de_tentativas = 0
pontos = 1000
pontos_perdidos = 0
rodada = 0
print('qual nivel de dificuldade?')
print('(1)facil (2)medio (3)dificil')
nivel = int(input('defina o nivel: '))

if(nivel == 1):
    total_de_tentativas=30
    pontos_perdidos=25
elif(nivel == 2):
    total_de_tentativas=20
    pontos_perdidos=50
else:
    total_de_tentativas=10
    pontos_perdidos=100

for rodada in range(total_de_tentativas):
    print('\nTentativa {} de {}'.format(rodada, total_de_tentativas))


    chute = int(input('digite um numero entre 1 e 1000: '))
    print('\nVoce digitou ', chute)

    if(chute < 1 or chute > 1000):
        print('voce deve digitar um numero entre 1 e 1000!')
        continue
    acertou = bool(chute == numero_secreto )
    maior = bool(chute > numero_secreto )
    menor = bool(chute < numero_secreto )


    if(acertou == True):
        print('voce acertou e fez {} pontos!'.format(pontos))
        break

    else:
        pontos = pontos - pontos_perdidos

        if(maior):
            print('voce errou!o seu chute foi maior do que o numero secreto')
        
        if (menor):
            print('voce errou!o seu chute foi menor do que o numero secreto')

        rodada = rodada + 1 

if (rodada == total_de_tentativas):
    print('o numero secreto era : ', numero_secreto )
print('fim de jogo')