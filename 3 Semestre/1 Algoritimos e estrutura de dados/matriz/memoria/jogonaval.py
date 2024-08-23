import random
import time
import os

jogo = []
apostas = []
figuras = ["🔥"] * 16 + ["❌"] * 48  # 16 espaços para navios (4 navios de 4 posições)

def inicializa_matrizes():
    global jogo, apostas
    jogo = [["❌" for _ in range(8)] for _ in range(8)]
    apostas = [["🌊" for _ in range(8)] for _ in range(8)]

def posicionar_navios():
    navios = [4, 4, 4, 4]  # Quatro navios, cada um ocupando 4 posições
    for tamanho in navios:
        colocado = False
        while not colocado:
            orientacao = random.choice(['horizontal', 'vertical'])
            if orientacao == 'horizontal':
                linha = random.randint(0, 7)
                coluna = random.randint(0, 7 - tamanho)
                if all(jogo[linha][coluna + i] == "❌" for i in range(tamanho)):
                    for i in range(tamanho):
                        jogo[linha][coluna + i] = "🔥"
                    colocado = True
            else:  # vertical
                linha = random.randint(0, 7 - tamanho)
                coluna = random.randint(0, 7)
                if all(jogo[linha + i][coluna] == "❌" for i in range(tamanho)):
                    for i in range(tamanho):
                        jogo[linha + i][coluna] = "🔥"
                    colocado = True

def mostra_tabuleiro():
    os.system("cls" if os.name == "nt" else "clear")
    print("   1   2   3   4   5   6   7   8")
    for i in range(8):
        print(f"{i+1} ", end="")
        for j in range(8):
            print(f" {jogo[i][j]} ", end="")
        print()

def mostra_apostas():
    os.system("cls" if os.name == "nt" else "clear")
    print("   1   2   3   4   5   6   7   8")
    for i in range(8):
        print(f"{i+1} ", end="")
        for j in range(8):
            print(f" {apostas[i][j]} ", end="")
        print()

def faz_aposta(num):
    while True:
        mostra_apostas()
        aposta = input(f"{num}ª Coordenada (2 números: linha e coluna): ")
        if len(aposta) != 2 or not aposta.isdigit():
            print("Erro... Informe dois números para a coordenada.")
            time.sleep(2)
            continue
        x = int(aposta[0]) - 1
        y = int(aposta[1]) - 1
        try:
            if apostas[x][y] == "🌊":
                apostas[x][y] = jogo[x][y]
                break
            else:
                print("Coordenada já descoberta. Jogue novamente")
                time.sleep(2)
        except IndexError:
            print("Erro... Posição inválida. Informe novamente")
            time.sleep(2)
    return (x, y)

def verifica_tabuleiro():
    faltam = 0
    for i in range(8):
        for j in range(8):
            if apostas[i][j] == "🌊":
                faltam += 1
    return faltam

inicializa_matrizes()
posicionar_navios()
mostra_tabuleiro()

while True:
    x1, y1 = faz_aposta(1)
    x2, y2 = faz_aposta(2)
    mostra_apostas()

    if apostas[x1][y1] == apostas[x2][y2]:
        print("Parabéns! Você acertou! 🤩")
        if verifica_tabuleiro() == 0:
            print("Show! Você ganhou! 🏆🥇")
            break
        time.sleep(2)
    else:
        print("Ah... você errou. 😥")
        apostas[x1][y1] = "🌊"
        apostas[x2][y2] = "🌊"
        sair = input("Deseja Desistir (S/N): ").upper()
        if sair == "S":
            break
