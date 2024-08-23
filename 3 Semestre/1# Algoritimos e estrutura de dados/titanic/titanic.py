import csv
titanic = []

with open("train.csv", mode="r") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    titanic.append(linha)

# print(titanic[0])
# print(titanic[0]['Name'])

# for pessoa in titanic:
#   print(f"{pessoa['Name']} - {pessoa['Age']} anos")
  
def titulo(texto):
  print()
  print(texto)
  print("-"*40)

def dados_sexo():
  titulo("Passageiros por Sexo")

  masc = 0
  fem = 0

  for pessoa in titanic:
    if pessoa["Sex"] == "male":
      masc += 1
    else:
      fem += 1

  # -------------- outra forma: list comprehensions
  masc_sobre = len([pessoa for pessoa in titanic 
             if pessoa["Sex"] == "male" and pessoa["Survived"] == "1"])
  masc_mortos = len([pessoa for pessoa in titanic 
             if pessoa["Sex"] == "male" and pessoa["Survived"] == "0"])
  fem_sobre = len([pessoa for pessoa in titanic 
             if pessoa["Sex"] == "female" and pessoa["Survived"] == "1"])
  fem_mortos = len([pessoa for pessoa in titanic 
             if pessoa["Sex"] == "female" and pessoa["Survived"] == "0"])

  print(f"Nº Homens: {masc}")
  print(f"      - Sobreviventes: {masc_sobre}")
  print(f"      - Mortos: {masc_mortos}")
  print()
  print(f"Nº Mulheres: {fem}")
  print(f"      - Sobreviventes: {fem_sobre}")
  print(f"      - Mortos: {fem_mortos}")
  print()

def top_10():
  titulo("Top 10: Passageiros de maior idade")

  print("Idade Sexo.: Sobrevivente Nome...........................")
  print("---------------------------------------------------------")

  titanic2 = [pessoa for pessoa in titanic if pessoa['Age'] != ""]

  titanic3 = sorted(titanic2, 
                    key=lambda pessoa: float(pessoa['Age']), 
                    reverse=True)
  
  contador = 0
  for pessoa in titanic3:
    if pessoa["Survived"] == "0":
      sobre = "Não"
    else:
      sobre = "Sim"  
    print(f"  {pessoa['Age']}  {pessoa['Sex']:6} {sobre:12} {pessoa['Name']}")
    contador += 1
    if contador == 10:
      break

while True:
  titulo("Análise de Dados: Passageiros do Titanic")
  print("1. Dados por Sexo")
  print("2. Top 10 mais idosos")
  print("3. Idade Média (por sexo)")
  print("4. Total Arrecadado")
  print("5. Dados por Classe")
  print("6. Finalizar")
  opcao = int(input("Opção: "))
  if opcao == 1:
    dados_sexo()
  elif opcao == 2:
    top_10()
  elif opcao == 6:
    break