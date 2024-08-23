palavra = input("Palavra: ").upper()

print("Descubra a palavra: ", end="")

for letra in palavra:
  if letra == palavra[0]:
    print(letra, end=" ")
  else:
    print("_", end=" ")
