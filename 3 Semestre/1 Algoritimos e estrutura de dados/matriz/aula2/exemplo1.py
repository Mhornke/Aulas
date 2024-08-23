# Exemplos de Entrada de Dados e conversões de tipo
nome = input("Nome: ")
idade = int(input("Idade: "))
salario = float(input("Salário R$: "))

# Saída de Dados
print("="*30)
# ^ alinha ao centro
# > alinha à direita
# < alinha à esquerda
print(f"Seu nome é: {nome:10s}. Bem-vindo(a)!")
print(f"Seu nome é: {nome:^10s}. Bem-vindo(a)!")
print(f"Seu nome é: {nome:>10s}. Bem-vindo(a)!")
print(f"Você possui: {idade:3d} anos")
print(f"Você possui: {idade:<3d} anos")
print(f"E recebe um salário de R$: {salario:9.2f} por mês")

if idade >= 18:
  print("Você é maior de idade")
  print("---------------------")
else:
  print("Você é menor de idade")
  print("=====================")

if salario < 1000:
  print("Você recebe até 1k")
elif salario <= 10000:
  print("Você recebe até 10k")
else:
  print("Bom salário!!")

