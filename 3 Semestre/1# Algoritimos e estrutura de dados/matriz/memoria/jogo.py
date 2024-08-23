import random         # para gerar números aleatórios
import time           # para gerar paradas temporárias
import os             # para executar funções do sistema operacional

jogo = []
apostas = []
temp = "🐶🐶🐵🐵🐸🐸🐟🐟🐘🐘🐪🐪🦊🦊🐔🐔"
figuras = list(temp)    

def preenche_matriz():
  for i in range(4):
    jogo.append([])
    apostas.append([])
    for _ in range(4):
      num = random.randint(0, len(figuras)-1)
      jogo[i].append(figuras[num])
      apostas[i].append("🟥")
      figuras.pop(num)

def mostra_tabuleiro():
  os.system("cls")
  print("   1   2   3   4")
  for i in range(4):
    print(f"{i+1}", end="")
    for j in range(4):
      print(f" {jogo[i][j]} ", end="")
    print("\n")

  print("Memorize a posição dos bichos...")
  time.sleep(2)

  print("Contagem Regressiva: ", end="") 
  for i in range(10, 0, -1):
    print(i, end=" ", flush=True)
    time.sleep(1)
    
def mostra_apostas():
  os.system("cls")
  print("   1   2   3   4")
  for i in range(4):
    print(f"{i+1}", end="")
    for j in range(4):
      print(f" {apostas[i][j]} ", end="")
    print("\n")

def faz_aposta(num): #posição aposta-------------------------------------------------
  while True:
    mostra_apostas()
    aposta = input(f"{num}ª Coordenada (2 números: linha e coluna): ")
    if len(aposta) != 2:
      print("Erro... Informe uma dezena, com a coordenada do bicho")
      time.sleep(2)
      continue
    x = int(aposta[0])-1
    y = int(aposta[1])-1
    try:
      if apostas[x][y] == "🟥":
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
  for i in range(4):
    for j in range(4):
      if apostas[i][j] == "🟥":
        faltam += 1
  return faltam

preenche_matriz()
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
    apostas[x1][y1] = "🟥"
    apostas[x2][y2] = "🟥"
    sair = input("Deseja Desistir (S/N): ").upper()
    if sair == "S":
      break
