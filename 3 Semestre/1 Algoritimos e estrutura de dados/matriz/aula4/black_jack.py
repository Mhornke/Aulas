import random
import time

naipes = "♠♣♥♦"
extras = "JQKA"
baralho = []

# def (equivalente ao function): cria uma função em Python
def monta_baralho():
  for i in range(2, 11):
    for naipe in naipes:
      baralho.append(str(i)+naipe)

  for extra in extras:
    for naipe in naipes:
      baralho.append(extra+naipe)

monta_baralho()
#print(baralho)

def obtem_pontos(carta):
  if len(carta) == 3:
    return 10
  else:
    if carta[0].isdigit():
      return int(carta[0])
    elif carta[0] == "A":
      return 11
    else:
      return 10

contador = 0
pontos_jogador = 0

while True:
  contador += 1
  num = random.randint(0, len(baralho)-1)
  carta = baralho.pop(num)
  print(f"Sua {contador}ª Carta é: {carta}")
  time.sleep(2)     # aguarda 2 segundos

  pontos_jogador += obtem_pontos(carta)
  if pontos_jogador >= 21:
    break

  if contador >= 2:
    continua = input("Deseja outra carta(S/N): ").upper()
    if continua == "N":
      break

print(f"\nTotal de Pontos do Jogador: {pontos_jogador}")

if pontos_jogador > 21:
  print("\nXiii... você perdeu! 🤣🤣")
else:
  input("Pressione Enter para Desafiar o Computador")
  contador = 0
  pontos_pc = 0

  while True:
    contador += 1
    num = random.randint(0, len(baralho)-1)
    carta = baralho.pop(num)
    print(f"{contador}ª Carta do Computador é: {carta}")
    time.sleep(2)     # aguarda 2 segundos

    pontos_pc += obtem_pontos(carta)

    if pontos_pc >= pontos_jogador:
      break

  print(f"\nTotal de Pontos do Computador: {pontos_pc}")

  if pontos_pc > 21:
    print("Show! Você venceu! 🏆🏆")
  elif pontos_pc == pontos_jogador:
    print("Ah... Deu empate! 🤔")
  else:
    print("Xiii... Você perdeu! 😂😂")
  