senha = input("Senha: ")

if len(senha) < 8 or len(senha) > 12:
  print("Senha inválida: deve possuir entre 8 e 12 caracteres")
else:
  pequenas = 0
  grandes = 0
  numeros = 0

  for letra in senha:
    if letra.isupper():
      grandes += 1
    elif letra.islower():
      pequenas += 1
    elif letra.isdigit():
      numeros += 1

  if grandes > 0 and pequenas > 0 and numeros > 0:
    print("Ok! Senha válida")  
  else:
    print("Erro... Use letras maiúsculas, minúsculas e números")
