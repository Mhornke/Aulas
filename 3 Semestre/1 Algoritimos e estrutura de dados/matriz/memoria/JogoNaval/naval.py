import random
import os
import time
from datetime import datetime, timedelta


jogo = []
apostas = []
pontuacao_total = []
acertos_multiplos = []
tiros_errados = []
gamerTag = []
vezesJogadas = []
tempo_jogando = []
resultado = []



navio = "💥"
temp = "🌊"
figuras = list(temp)
acertos = False

def titulo(texto, linha = "_"):
    print()
    print(f"{texto:}")
    print(linha*40)

def inicializa_matrizes():
    global jogo, apostas
    jogo = [["🌊"] * 9 for _ in range(9)]
    apostas = [["🌊"] * 9 for _ in range(9)]
    print(jogo, end="" )

def posiciona_navio():
    for i in range(5):
        navio_posicionado = False
        while not navio_posicionado:
        #   tamanho_navio= random.randint(3, 5 -1)
            navios = 0
            orientacao = random.choice(["horizontal", "vertical"])
            #orientacao2 = random.choice(["horizontal", "vertical"])  
            if orientacao == "horizontal":
                linha = random.randint(0, 9 - 1)
                coluna = random.randint(0, 9 - 3)
                if jogo[linha][coluna] == "🌊" and jogo[linha][coluna + 1] == "🌊" and jogo[linha][coluna + 2] == "🌊":
                    jogo[linha][coluna] = navio
                    jogo[linha][coluna + 1] = navio
                    jogo[linha][coluna + 2] = navio
                    navio_posicionado = True
                    navios +=1
            elif orientacao == "vertical":
                linha = random.randint(0, 9 - 3)
                coluna = random.randint(0, 9 - 1)
                if jogo[linha][coluna] == "🌊" and jogo[linha + 1][coluna] == "🌊" and jogo[linha + 2][coluna] == "🌊":
                    jogo[linha][coluna] = navio
                    jogo[linha + 1][coluna] = navio
                    jogo[linha + 2][coluna] = navio
                    navio_posicionado = True
                    navios +=1
        if navios == 4:
            break
            # if navio_posicionado:
            #     navio_posicionado = False
            #     if orientacao == "horizontal":
            #         linha = random.randint(0, 10 - 1)
            #         coluna = random.randint(0, 10 - 4)
            #         if jogo[linha][coluna] == "🌊" and jogo[linha][coluna + 1] == "🌊" and jogo[linha][coluna + 2] == "🌊" and jogo[linha][coluna + 3] == "🌊":
            #             jogo[linha][coluna] = navio
            #             jogo[linha][coluna + 1] = navio
            #             jogo[linha][coluna + 2] = navio
            #             jogo[linha][coluna + 3] = navio
            #             navio_posicionado = True
            #             navios +=1
            #     elif orientacao == "vertical":
            #         linha = random.randint(0, 10 - 4)
            #         coluna = random.randint(0, 10 - 1)
            #         if jogo[linha][coluna] == "🌊" and jogo[linha + 1][coluna] == "🌊" and jogo[linha + 2][coluna] == "🌊" and jogo[linha + 3][coluna] == "🌊":
            #             jogo[linha][coluna] = navio
            #             jogo[linha + 1][coluna] = navio
            #             jogo[linha + 2][coluna] = navio
            #             jogo[linha + 3][coluna] = navio
            #             navio_posicionado = True
            #             navios +=1
            
            # if navio_posicionado:
            #     navio_posicionado = False
            #     if orientacao == "horizontal":
            #         linha = random.randint(0, 10 - 1)
            #         coluna = random.randint(0, 10 - 5)
            #         if jogo[linha][coluna] == "🌊" and jogo[linha][coluna + 1] == "🌊" and jogo[linha][coluna + 2] == "🌊" and jogo[linha][coluna + 3] == "🌊" and jogo[linha][coluna + 3] == "🌊":
            #             jogo[linha][coluna] = navio
            #             jogo[linha][coluna + 1] = navio
            #             jogo[linha][coluna + 2] = navio
            #             jogo[linha][coluna + 3] = navio
            #             jogo[linha][coluna + 4] = navio
            #             navio_posicionado = True
            #             navios +=1
            #     elif orientacao == "vertical":
            #         linha = random.randint(0, 10 - 5)
            #         coluna = random.randint(0, 10 - 1)
            #         if jogo[linha][coluna] == "🌊" and jogo[linha + 1][coluna] == "🌊" and jogo[linha + 2][coluna] == "🌊" and jogo[linha + 3][coluna] == "🌊" and jogo[linha][coluna + 3] == "🌊":
            #             jogo[linha][coluna] = navio
            #             jogo[linha + 1][coluna] = navio
            #             jogo[linha + 2][coluna] = navio
            #             jogo[linha + 3][coluna] = navio
            #             jogo[linha + 4][coluna] = navio
            #             navio_posicionado = True
            #             navios +=1
        

def preenche_matriz():
    for i in range(9):
        for j in range(9):
            if jogo[i][j] == "🌊" and figuras:
                num = random.randint(0, len(figuras) - 1)
                jogo[i][j] = figuras[num]
                figuras.pop(num)

def posicao_aposta():
    global acertos, erros
                
    # for i in range(9):
    #     print(f"{i+1} ", end="")
    #     for j in range(9):
    #         print(f" {apostas[i][j]} ", end="")
    #     print()

    
    while True:
        aposta = input(f"Coordenada (2 Números: linha e coluna): ")
        if len(aposta) != 2:
            print("Erro ... Informe um Dezena, com a coordenada do Navio")
            time.sleep(0.5)
            continue
        acerto = False
        erros = False
        x = int(aposta[0]) - 1
        y = int(aposta[1]) - 1
        try:
            
            acertos = False
            erros = False    
            if apostas[x][y] == "🌊":
                if jogo[x][y] == navio:
                    apostas[x][y] = navio
                    print("voce acertou o navio adversario")
                    print("Essa foi a sua oportunidade de recarregar")                              
                    acertos = True
                    
                else:
                    acertosSeguidos = 1
                    print("Erroo o tiro")                    
                    apostas[x][y] = "❌"
                    erros = True
                                                
                break                 
            else:
                print("Coordenada já descoberta, digite novas coordenadas")
            time.sleep(0.5)
        except IndexError:
            print("Erro ... Posição invalida")
            time.sleep(0.5) 

def mostra_tabuleiro():
    print("\nMatriz 'apostas':")
    print(" 1   2   3   4   5   6   7   8   9")
    contador = 0
    for linha in apostas:
        contador += 1
        print(f"{contador}", end="")
        print('  '.join(linha)) 

def verificar_tabuleiro():
    faltam = 0
    for i in range(9):
        for j in range(9):
            if jogo[i][j] == navio and apostas[i][j] != navio:
                faltam += 1
    return faltam




def tempo():  
    min_inicio = hora_inicial.split(":")
    min_final = hora_final.split(":")

    min_1 = int(min_inicio[1])  
    seg_1 = int(min_inicio[2])  
   
    min_2 = int(min_final[1])  
    seg_2 = int(min_final[2]) 

    segundos = seg_2 - seg_1
    
    if seg_1 > seg_2: 
        minutos = min_2 - min_1 
        segundos = seg_1 - seg_2   

    elif seg_1< seg_2: 
        minutos = min_1 - min_2
        segundos = seg_1 - seg_2 
        if segundos <0 and minutos > 1: 
            minutos = minutos - 1
            segundos = 60 - segundos 
        else:
            segundos = (seg_1 - seg_2 ) * -1     

    tempo_salvar = str(f"{minutos:2d}:{segundos:2d}")
    tempo_jogando.append(tempo_salvar)
    
    return minutos, segundos






def gravar_jogo():    
    with open("partidas.txt", "a") as arq:
        for nome, pontos, tempo, jogadas, resultado1 in zip(gamerTag, pontuacao_total, tempo_jogando, vezesJogadas, resultado):
            arq.write(f"{nome};{int(pontos)};{tempo};{jogadas};{resultado1}\n")

def carregar_partidas():
    if not os.path.isfile("partidas.txt"):
        return

    with open("partidas.txt", "r") as arq:
        dados = arq.readlines()

        for linha in dados:

            #print(f"Lendo linha: {dados}")
            partes = linha.split(";")
            #print(f"Lendo linha: {linha.strip()}")
            #print(f"Partes: {partes} (Quantidade: {len(partes)})")

            gamerTag.append(partes[0])
            pontuacao_total.append(partes[1])
            tempo_jogando.append(partes[2])
            vezesJogadas.append(partes[3])
            resultado.append(partes[4])
           




def iniciar_jogo():
    global acertos, erros, hora_inicial, hora_final, venceu

    inicializa_matrizes()
    posiciona_navio()
    preenche_matriz()
    mostra_tabuleiro()

    tentativas = 0
    pontuacao = 0
    municao = 4
    acertosMultipos = 0
    quantMultiplos = 0
    Tiros_erros = 0   
    
    print(f"nome armazenamento teste {gamerTag}") # ------------------
    #time_inicio = time.time()
    time_inicial = datetime.now()
    hora_inicial = time_inicial.strftime("%H:%M:%S")

        
    while True:
                         # 1@ conta quantas vezes jogou até perder ou ganhar

        #agora = time.time()
        #elapsed = agora - time_inicio

        posicao_aposta()
        
        os.system("cls")
        print("\nMatriz 'apostas':")
        print(" 1   2   3   4   5   6   7   8   9")
        contador = 0
        for linha in apostas:
            contador += 1
            print(f"{contador}", end="")
            print('  '.join(linha))

        # posição navios ----------------------------
        print("Hack ligado':")
        for linha in jogo:
            print(' '.join(linha))
        
        if acertos == True:
            pontuacao +=3
            print(f"Voce acertou seu inimigo")
            print(f"Agora tera tempo para recarregar")
            municao = 4  # Reinicia as tentativas após um acerto
            acertosMultipos += 1
            tentativas +=1
            for i in range(4):
                print("   ___  ")
                print("", end="")

                time.sleep(0.4) 
            if acertosMultipos >2: 
                pontuacao += 2.2
                quantMultiplos += 1

        if erros == True:
            Tiros_erros +=1
            # pontuacao -= 1
            municao -=1
            tentativas +=1 
            print("\n")
            print(f"🚨         Errou o navio        🚨")          


        if verificar_tabuleiro() == 0:
            venceu = "Vitória"
            resultado.append(venceu)
            vezesJogadas.append(tentativas)
            pontuacao_total.append(pontuacao)

            time_final = datetime.now()
            hora_final = time_final.strftime("%H:%M:%S")
            
            minutos, segundos = tempo()
            print(f"Tempo jogado: {minutos} min e {segundos} seg")
            
            print("Parabéns! Você venceu a batalha")
            salvar = input("Deseja salvar o seu jogo? s/n: ").upper()
            if salvar== "S":
                nome = input("Nome do jogador: ")    
                gamerTag.append(nome)
                gravar_jogo()
                break
            break
        
        
        print(f"Munição: {municao}")
        print(f"Pontuação: {pontuacao:.2f}")

       
        if municao == 0:
            time_final = datetime.now()
            hora_final = time_final.strftime("%H:%M:%S")
            venceu = "Derrota"
            resultado.append(venceu)
            vezesJogadas.append(tentativas)
            pontuacao_total.append(int(pontuacao))

            print(f"Pontuação: {pontuacao_total}")


            print("                                       ")
            print("         Acabou a sua munição          ")
            print("O adversario teve tempo de acertar você")
            print("")
            print("          _____________________              ")
            print("         /                     \              ")
            print("        |         R.I.P         |             ")
            print("        |                       |             ")
            print(f"        |  {hora_inicial} - {hora_final}  |")
            print("        |                       |             ")
            print("        |                       |             ")
            print("///////\\\/////\//\/////////////\///////\//// ")
            minutos, segundos = tempo()
            print(f"Tempo jogado: {minutos} minutos e {segundos} segundos")
            print("\n")
            salvar = input("Deseja salvar o seu jogo? s/n: ").upper()
            if salvar== "S":
                nome = input("Nome do jogador: ")    
                gamerTag.append(nome)
                gravar_jogo()
                break
            
            break

        
def listar_partidas_jogadas():
    carregar_partidas()
    print("                             Rank                                       ")
   
    print("Jogador              |      Pontos     |   Tempo de partida   |  Resultado   ")    #rq.write(f"{nome};{pontos:.1f};{tempo};{jogadas};{resultado1}\n")
        #zip(gamerTag, pontuacao_total, tempo_jogando, vezesJogadas, resultado)
    juntos = sorted(zip(gamerTag, pontuacao_total, tempo_jogando, vezesJogadas, resultado)) 
    gamerTag2, pontuacao_total2, tempo_jogando2, vezesJogadas2, resultado2 = zip(*juntos)

    for jogador, pontos, tempo, vezes, resultado_partida in juntos:
        print(f"{jogador:20s} |    {pontos:^10s}   |{tempo:^22s}|{resultado_partida:^15s}")  
    print("_"*69)



def top():
    carregar_partidas()
    juntos = sorted(zip(gamerTag, pontuacao_total, tempo_jogando, vezesJogadas, resultado),
                   key=lambda x: float(x[1]), reverse=True)[:3]  # Ordena pelo segundo elemento (pontuação_total) em ordem decrescente e pega os top 3
    gamerTag_top, pontuacao_total_top, tempo_jogando_top, vezesJogadas_top, resultado_top = zip(*juntos)

    titulo("Top 3 Jogadores com Maior Pontuação")
    print("\n Jogador..........................Pontuação")
    for contador, (jogador, pontos) in enumerate(zip(gamerTag_top, pontuacao_total_top), start=1):
        print(f"{contador:2d} {jogador:30s} {pontos}")         



while True:
    titulo("Guerra Naval\n")
    print("1. Jogar")
    print("2. Lista de partidas ")
    print("3. Top 3")
    print("6. Sair")
    opcao = int(input("Opção N°? "))
    if opcao == 1:
        iniciar_jogo()
    elif opcao == 2:
        listar_partidas_jogadas()      
    elif opcao == 3:
        top()
    elif opcao == 6:
        break
    else:
        break
