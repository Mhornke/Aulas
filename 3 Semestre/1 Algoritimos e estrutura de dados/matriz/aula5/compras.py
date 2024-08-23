import os

compras = []
precos = []

def titulo(texto, sublinhado="="):
  print()
  print(texto)
  print(sublinhado*40)

def incluir():
  titulo("Inclusão de Compra", "-")

  compra = input("Descrição da Compra: ")
  preco = float(input("Valor Previsto R$..: "))

  compras.append(compra)  
  precos.append(preco)
  print("Ok. Compra Cadastrada com Sucesso!")

def listar():
  titulo("Compras Cadastradas", "-")

  print("Nº Descrição da Compra..........: R$ Previsto:")
  print("----------------------------------------------")

  total = 0
  for num, (compra, preco) in enumerate(zip(compras, precos), start=1):
    print(f"{num:2d} {compra:30s} {preco:12.2f}")
    total += preco

  # total2 = sum(precos)
  print("----------------------------------------------")
  print(f"{'Total R$:':33s} {total:12.2f}")

def listar_ordem():
  titulo("Compras Cadastradas em Ordem", "-")

  print("Descrição da Compra..........: R$ Previsto:")
  print("-------------------------------------------")

  juntas = sorted(zip(compras, precos))
  compras2, precos2 = zip(*juntas)

  for compra, preco in zip(compras2, precos2):
    print(f"{compra:30s} {preco:12.2f}")

def excluir():
  listar()

  num = int(input("Qual Nº da Compra Excluir? "))

  if num == 0 or num > len(compras):
    print("Número inválido...")
    return
  
  compras.pop(num-1)
  precos.pop(num-1)

def grava_compras():
  with open("compras.txt", "w") as arq:
    for compra, preco in zip(compras, precos):
      arq.write(f"{compra};{preco}\n")

def carrega_compras():
  if not os.path.isfile("compras.txt"):
    return
  
  with open("compras.txt", "r") as arq:
    dados = arq.readlines()

    for linha in dados:
      partes = linha.split(";")
      compras.append(partes[0])
      precos.append(float(partes[1]))

# --------------------------- Programa Principal
carrega_compras()
while True:
  titulo("Lista de Compras da Semana")  
  print("1. Incluir Compra")
  print("2. Listar Compras")
  print("3. Listar Compras em Ordem")
  print("4. Excluir Compra")
  print("5. Finalizar")
  opcao = int(input("Opção: "))  
  if opcao == 1:
    incluir()
  elif opcao == 2:
    listar()
  elif opcao == 3:
    listar_ordem()
  elif opcao == 4:
    excluir()
  else:
    grava_compras()
    break