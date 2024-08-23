while True:
  nome = input("Nome Completo: ")

  partes = nome.split(" ")

  if len(partes) == 1:
    print("Por favor, digite o nome completo")
  else:
    print(f"Nome no Crachá: {partes[0].upper()}")
    break
  