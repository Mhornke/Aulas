palavra = input("Palavra: ").upper()

inverso = ""

for letra in palavra:
  inverso = letra + inverso

if palavra == inverso:
  print(f"{palavra} é uma palíndrome")
else:
  print(f"Erro... {palavra} não é uma palíndrome")

