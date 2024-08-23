import random
import time

# Definindo as listas e os símbolos
navio = "💥"
temp = ["🌊"] * 100
figuras = list(temp)

def titulo(texto, linha="_"):
    print()
    print(f"{texto:}")
    print(linha*40)

def inicializa_matrizes():
    jogo = [["🌊"] * 10 for _ in range(10)]
    apostas = [["🌊"] * 10 for _ in range(10)]
    return jogo, apostas

def posiciona_navio(jogo, tamanho):
    navio_posicionado = False
    while not navio_posicionado:
        orientacao = random.choice(["horizontal", "vertical"])
        if orientacao == "horizontal":
            linha = random.randint(0, 9)
            coluna = random.randint(0, 10 - tamanho)
            if all(jogo[linha][col + coluna] == "🌊" for col in range(tamanho)):
                for col in range(tamanho):
                    jogo[linha][col + coluna] = navio
                navio_posicionado = True
        elif orientacao == "vertical":
            linha = random.randint(0, 10 - tamanho)
            coluna = random.randint(0, 9)
            if all(jogo[lin + linha][coluna] == "🌊" for lin in range(tamanho)):
                for lin in range(tamanho):
                    jogo[lin + linha][coluna] = navio
                navio_posicionado = True

def posiciona_navios(jogo):
    posiciona_navio(jogo, 3)  # Navio de 3 posições
    posiciona_navio(jogo, 4)  # Navio de 4 posições
    posiciona_navio(jogo, 5)  # Navio de 5 posições

def preenche_matriz(jogo):
    for i in range(10):
        for j in range(10):
            if jogo[i][j] == "🌊" and figuras:
                num = random.randint(0, len(figuras) - 1)
                jogo[i][j] = figuras[num]
                figuras.pop(num)

def posicao_aposta(apostas, jogo):
    print("\nMatriz 'apostas':")
    for linha in apostas:
        print('  '.join(linha))
    while True:
        aposta = input("Coordenada (2 Números: linha e coluna): ")
        if len(aposta) != 2:
            print("Erro ... Informe uma dezena, com a coordenada do navio")
            time.sleep(0.5)
            continue

        x = int(aposta[0]) - 1
        y = int(aposta[1]) - 1

        try:
            if apostas[x][y] == "🌊":
                if jogo[x][y] == navio:
                    apostas[x][y] = navio
                else:
                    apostas[x][y] = "❌"
                return jogo[x][y] == navio
            else:
                print("Coordenada já descoberta, digite novas coordenadas")
            time.sleep(0.5)
        except IndexError:
            print("Erro ... Posição inválida")
            time.sleep(0.5)

def verificar_tabuleiro(jogo, apostas):
    faltam = 0
    for i in range(10):
        for j in range(10):
            if jogo[i][j] == navio and apostas[i][j] != navio:
                faltam += 1
    return faltam

def iniciar_jogo():
    jogo, apostas = inicializa_matrizes()
    posiciona_navios(jogo)
    preenche_matriz(jogo)

    pontuacao = 0
    tentativas_restantes = 4

    while True:
        acertou = posicao_aposta(apostas, jogo)
        print("Matriz 'jogo':")
        for linha in jogo:
            print(' '.join(linha))
        print("\nMatriz 'apostas':")
        for linha in apostas:
            print('  '.join(linha))

        if acertou:
            pontuacao += 1
            print(f"Parabéns! Você acertou uma parte do navio! Pontuação: {pontuacao}")
            tentativas_restantes = 4  # Reinicia as tentativas após um acerto
        else:
            tentativas_restantes -= 1
            print(f"Você errou. Tentativas restantes: {tentativas_restantes}")

        if verificar_tabuleiro(jogo, apostas) == 0:
            print("Parabéns! Você ganhou! 🏆🥇")
            break

        if tentativas_restantes == 0:
            print("Você perdeu! Suas tentativas acabaram.")
            break

        sair = input("Você está preparado? (S/N): ").upper()
        if sair == "N":
            break

while True:
    titulo("Guerra Naval\n")
    print("1. Jogar")
    print("6. Sair")
    opcao = int(input("Opção N°? "))
    if opcao == 1:
        iniciar_jogo()
    elif opcao == 6:
        break
    else:
        break
