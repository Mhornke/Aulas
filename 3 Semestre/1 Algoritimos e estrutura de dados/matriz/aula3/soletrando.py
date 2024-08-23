import time
palavra = input("Palavra: ")

# print("Soletrando a palavra...")

# for letra in palavra:
#   print(letra.upper())
#   time.sleep(1)           # aguarda 1 segundo 

# -------------------- outra forma
  
print("Soletrando a palavra..: ", end="")

for letra in palavra:
  # flush=True, evita que a saída fique em buffer e seja exibida
  # uma única vez
  print(letra.upper(), end=" ", flush=True)
  time.sleep(1)           # aguarda 1 segundo 
