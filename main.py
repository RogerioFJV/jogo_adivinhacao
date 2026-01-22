import random

print("Bem-vindo ao Jogo da Adivinhação!")

# O programa escolhe um número aleatório entre 1 e 20
numero_secreto = random.randint(1, 20)

tentativas = 0
acertou = False

while not acertou:
    palpite = int(input("Digite um número entre 1 e 20: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        acertou = True
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")