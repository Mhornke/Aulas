import time
import random

print("Jogo do Caça-Níquel")
print("-"*30)

nome = input("Nome do Apostador: ")
valor = float(input("Valor da Aposta R$: "))

input("Pressione Enter para Girar a Roleta...")

figuras = "🥝🍇🍓"
jogo = ""

print("\nRolando..: ", end="")

for _ in range(3):
  num = random.randint(0, 2)
  print(figuras[num], end=" ", flush=True)
  jogo = jogo + figuras[num]
  time.sleep(1)

if jogo[0] == jogo[1] and jogo[0] == jogo[2]:
  print(f"\n\n🏆🏆 Parabéns ${nome}! Você ganhou R$: {valor*3}")
elif jogo[0] == jogo[1] or jogo[1] == jogo[2] or jogo[0] == jogo[2]:
  print(f"\n\nQuase {nome}! Continue apostando... 🧨🧨")
else:
  print(f"\n\nBah... {nome}! Na próxima vai... 😂😂")


