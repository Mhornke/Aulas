import csv

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
    paises = list(set([x['Country'] for x in visitantes]))
    numeros = [0] * len(paises)

    for visitante in visitantes:
        indice = paises.index(visitante['Country'])
        numeros[indice] += int(visitante['Visitor'])

    juntos = sorted(zip(numeros, paises), reverse=True)
    numeros2, paises2 = zip(*juntos)

    titulo("Top 20: Países com Maior Nº de Visitantes no Japão")

    print("\nNº País.......................... Visitantes")    
    print("-------------------------------------------------------")
    for contador, (pais, num) in enumerate(zip(paises2, numeros2), start=1):
        print(f"{contador:2d} {pais:30s} {num:_.0f}".replace("_", "."))
        if contador == 20:
            break
        

def total_ano():
    # Ano NºVisitantes
    anos = list(set([x['Year'] for x in visitantes]))
    numeros = [0] * len(anos)

    for visitante in visitantes:
        indice = anos.index(visitante['Year'])
        numeros[indice] += int(visitante['Visitor'])

    juntos = sorted(zip(anos, numeros))
    anos2, numeros2 = zip(*juntos)

    titulo("Nº de Visitantes no Japão por Ano")

    print("\nAno: Visitantes")    
    print("-------------------")
    for ano, num in zip(anos2, numeros2):
        print(f"{ano} {num:_.0f}".replace("_", "."))


def top10_22_23():
    # Listar Pais e NºVisitantes dos 10+ de 2022
    # Listar Pais e NºVisitantes dos 10+ de 2023
    # Mostrar a união dos 10+ de cada ano
    # Mostrar a interseção dos 10+ de cada ano
    # Mostrar os que só apareceram em 2022
    # Mostrar os que só apareceram em 2023

    # --------------------------------------------- Números de 2022

    paises22 = list(set([x['Country'] for x in visitantes if x['Year'] == '2022']))
    numeros22 = [0] * len(paises22)

    visitantes22 = [x for x in visitantes if x['Year'] == '2022']

    for visitante in visitantes22:
        indice = paises22.index(visitante['Country'])
        numeros22[indice] += int(visitante['Visitor'])

    juntos = sorted(zip(numeros22, paises22), reverse=True)
    numeros2, paises2 = zip(*juntos)

    titulo("Top 10: Países com Maior Nº de Visitantes no Japão em 2022")

    conj22 = set()    

    print("\nNº País.......................... Visitantes")    
    print("-------------------------------------------------------")
    for contador, (pais, num) in enumerate(zip(paises2, numeros2), start=1):
        print(f"{contador:2d} {pais:30s} {num:_.0f}".replace("_", "."))
        conj22.add(pais)
        if contador == 10:
            break

    # --------------------------------------------- Números de 2023

    paises23 = list(set([x['Country'] for x in visitantes if x['Year'] == '2023']))
    numeros23 = [0] * len(paises23)

    visitantes23 = [x for x in visitantes if x['Year'] == '2023']

    for visitante in visitantes23:
        indice = paises23.index(visitante['Country'])
        numeros23[indice] += int(visitante['Visitor'])

    juntos = sorted(zip(numeros23, paises23), reverse=True)
    numeros2, paises2 = zip(*juntos)

    titulo("Top 10: Países com Maior Nº de Visitantes no Japão em 2023")

    conj23 = set()

    print("\nNº País.......................... Visitantes")    
    print("-------------------------------------------------------")
    for contador, (pais, num) in enumerate(zip(paises2, numeros2), start=1):
        print(f"{contador:2d} {pais:30s} {num:_.0f}".replace("_", "."))
        conj23.add(pais)
        if contador == 10:
            break

    print("\n------------------------------------------------")        
    print(f"União dos Países 22 e 23: {conj22.union(conj23)}")
    print(f"\nIntersecção dos Países 22 e 23: {conj22.intersection(conj23)}")
    print(f"\nPaís Exclusivo no Top 10 em 22: {conj22.difference(conj23)}")
    print(f"\nPaís Exclusivo no Top 10 em 23: {conj23.difference(conj22)}")


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
