import csv
from itertools import groupby
from operator import itemgetter

ricos = []

with open("Billionaires Statistics Dataset.csv") as arq:
    linhas = csv.DictReader(arq)
    for linha in linhas:
        ricos.append(linha)


def titulo(texto):
    print()
    print(texto)
    print("="*40)


def top20():
    # Nº, Nome, País, Fortuna
    titulo("Top 20 dos maiores bilionários")

    print("\nNº Nome...................................: Pais...............: Fortuna U$")    

    for i, rico in enumerate(ricos[:20], start=1):
        print(f"{i:2d} {rico['personName']:40s} {rico['country']:20s} {rico['finalWorth']}")


def compara_paises():
    # Ler 2 países. Após, exibir a lista com nome e fortuna dos
    # bilionários de cada país. Ao final, exibir a quantidade de
    # bilionário de cada país
    titulo("Compara bilionários de 2 países")

    pais1 = input("1º País: ").upper()
    pais2 = input("2º País: ").upper()

    contador1 = 0
    print(f"\nBilionários: {pais1}")
    print("-"*40)

    for rico in ricos:
        if rico['country'].upper() == pais1:
            print(f"{rico['personName']} - U$ {rico['finalWorth']}")
            contador1 += 1
  
    contador2 = 0
    print(f"\nBilionários: {pais2}")
    print("-"*40)

    for rico in ricos:
        if rico['country'].upper() == pais2:
            print(f"{rico['personName']} - U$ {rico['finalWorth']}")
            contador2 += 1

    print("\n===================================================")
    print(f"Nº Bilionários {pais1}: {contador1}")
    print(f"Nº Bilionários {pais2}: {contador2}")
    

def pesquisa_cidade():
    # Ler o nome de uma cidade. Pesquisar e exibir o nome e categoria
    # dos bilionários desta cidade. Exibir mensagem, caso não tenha
    # bilionários na cidade informada
    titulo("Pesquisa bilionários por cidade")

    cidade = input("Cidade: ").upper()

    contador = 0
    print(f"\nBilionários da Cidade: {cidade}")
    print("-"*40)

    for rico in ricos:
        if rico['city'].upper() == cidade:
            print(f"{rico['personName']}: {rico['category']}")
            contador += 1

    if contador == 0:
        print(f"*Obs.: Não há bilionários na cidade de: {cidade}")


def agrupa_atividade():
    titulo("Bilionários por Ramo de Atividade")

    ricos2 = sorted(ricos, key=itemgetter("category"))

    print("Atividade.........................: NºPessoas")

    lista = []
    for categoria, dados in groupby(ricos2, key=itemgetter("category")):
        #    print(f"{categoria:35s} {len(list(dados))}")
        lista.append({"categoria": categoria, "num": len(list(dados))})

    lista2 = sorted(lista, key=itemgetter("num"), reverse=True)

    for item in lista2:
        print(f"{item['categoria']:35s}   {item['num']}")

def agrupa_pais():
    # Agrupar os bilionários por país. Exibir país, número de bilionários
    # e a soma das suas fortunas (de cada país). Em ordem de número
    titulo("Bilionários Agrupados por País")

    ricos2 = sorted(ricos, key=itemgetter("country"))

    print("País.........................: NºPessoas Fortuna U$.:")    

    lista = []
    for pais, dados in groupby(ricos2, key=itemgetter("country")):
        num = 0
        total = 0
        for dado in dados:
            num += 1
            total += int(dado['finalWorth'])        
        lista.append({"pais": pais, "num": num, "total": total})

    lista2 = sorted(lista, key=itemgetter("num"), reverse=True)

    for item in lista2:
        print(f"{item['pais']:30s} {item['num']:9d} {item['total']:12d}")


# -------------------------------- Programa Principal
while True:
    titulo("Bilionários: Análise dos Dados")
    print("1. Top 20 maiores bilionários")
    print("2. Comparativo entre 2 países")
    print("3. Pesquisa bilionário por cidade")
    print("4. Agrupar por Atividade")
    print("5. Agrupar por País")
    print("6. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        top20()
    elif opcao == 2:
        compara_paises()
    elif opcao == 3:
        pesquisa_cidade()
    elif opcao == 4:
        agrupa_atividade()
    elif opcao == 5:
        agrupa_pais()
    else:
        break
