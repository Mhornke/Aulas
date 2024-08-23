import csv
# from itertools import groupby
# from operator import itemgetter

visitantes = []

with open("Number of foreign visitors to Japan by month_ .csv") as arq:
    linhas = csv.DictReader(arq)
    for linha in linhas:
        visitantes.append(linha)


def titulo(texto):
    print()
    print(texto)
    print("="*40)

def top20():
    # Nº País NºVisitantes
    # criar um vetor 'paises' que percorra todos os elemestos " " desse objeto e cada item tu chama de X 
    # precisa só do pais [country]
    # precisa agrupar os paises, usasse set()  
    
    paises = list(set([x['Country'] for x in visitantes]))
    # agrupa os paises e faz um lista 
    numeros = [0] * len(paises)
    # cria uma lista de 0 

    for visitante in visitantes:
        indice = paises.index(visitante['Country'])
        numeros[indice] += int(visitante['Visitor'])
        # pega o indice "a posição" do pais e soma o atributo "Visitor"

    unirdados = sorted(zip(numeros, paises), reverse=True)
        # só o sorted mostra em decrecente por isso é add reverse=True
    numeros2, paises2 = zip(*unirdados)
        # para separa novamente 
    titulo('Top 20: Paises com Maior nº de Visitantes no Japão')
    print('\n Nº Pais........................ Visitantes')
    for contador, (pais, num) in enumerate(zip(paises2, numeros2), start=1):
        # o enumarate acresenta um contador para variavel "contador"
        print(f"{contador:2d} {pais:30s} {num:_.0f}".replace("_","."))
        if contador == 20:                  # _.0f . repace é para adicionar um ponto na casa dos milhares
            break
    print('..................................................')
   
def total_ano():
    # Ano NºVisitantes
    pass

def top10_22_23():
    # Listar Pais e NºVisitantes dos 10+ de 2022
    # Listar Pais e NºVisitantes dos 10+ de 2023
    # Mostrar a união dos 10+ de cada ano
    # Mostrar a interseção dos 10+ de cada ano
    # Mostrar os que só apareceram em 2022
    # Mostrar os que só apareceram em 2023
    pass
    

# ------------------------------------------------------ Programa Principal
while True:
    titulo("Visitantes Estrangeiros no Japão: 2017 à 2023")
    print("1. Top 20 - Países com maior número de visitantes")
    print("2. Total de Visitantes por ano")
    print("3. Top 10: Visitantes 2022 e 2023")
    print("4. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        top20()
    elif opcao == 2:
        total_ano()
    elif opcao == 3:
        top10_22_23()
    else:
        break
