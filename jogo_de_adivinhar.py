import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Estou pensando em um número entre 1 e 10. Você consegue adivinhar qual é?")

    while True:
        tentativa = int(input("Digite seu palpite: "))
        tentativas += 1

        if tentativa < numero_secreto:
            print(f"O numero {tentativa} é baixo.")
        elif tentativa > numero_secreto:
            print(f"O numero {tentativa} é alto.")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break
        
        diferenca = abs(numero_secreto - tentativa)
        if diferenca == 1:
            print("Mas você está muito perto!")
        elif diferenca <= 3:
            print("Mas você está perto!")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == 's':
        jogo_adivinhacao()
    else:
        print("Obrigado por jogar!")

jogo_adivinhacao()
