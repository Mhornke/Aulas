import csv

programas = []

with open("netflix_titles.csv", encoding="utf-8") as arq:
    linhas = csv.DictReader(arq)
    for linha in linhas:
        programas.append(linha)

def titulo(texto):
    print()
    print(texto)
    print("="*40)

def totais_filmes_series():
    pass
    # Nº Total de Filmes:
    # Nº Total de Séries:
    nfilmes = len([x for x in programas if x['type'] == "Movie"])
    nseries = len([x for x in programas if x['type'] == "TV Show"])
    titulo("Total de Filmes e Séries")
    print(f"Total de Filmes: {nfilmes}")
    print(f"Total de Séries: {nseries}")


def obtemMinutos(tempo):
    # "126 min" => 126
    partes = tempo.split(" ")
    # partes[0] => 126
    # partes[1] => min
    return int(partes[0])

def duracao_filmes():
    pass
    # Duração Média dos Filmes:
    # Menor Duração: __
    # Filme(s):
    # Maior Duração: __
    # Filme(s):
    soma = sum([obtemMinutos(x['duration']) for x in programas if x['type'] == "Movie" and x['duration'] != ""])
    nfilmes = len([x for x in programas if x['type'] == "Movie"])
    media = soma / nfilmes
    print(f"Duração Média dos Filmes: {media:6.2f}")

    menor = min([obtemMinutos(x['duration']) for x in programas if x['type'] == "Movie" and x['duration'] != ""])
    print(f"Menor Duração: {menor} min")

    menores = [x['title'] for x in programas if x['type'] == "Movie" and x['duration'] == str(menor) + " min"]
    print('\n'.join(menores))

    maior = max([obtemMinutos(x['duration']) for x in programas if x['type'] == "Movie" and x['duration'] != ""])
    print(f"Maior Duração: {maior} min")

    maiores = [x['title'] for x in programas if x['type'] == "Movie" and x['duration'] == str(maior) + " min"]
    print('\n'.join(maiores))


def temporadas_series():
    pass
    # Séries com 1 Temporada: ___
    # Séries com 2 Temporadas: ___
    # Séries com 3 Temporadas: ___
    # Séries com 4 Temporadas: ___
    # ............

    # Série com 18 Temporadas: 2
    # Nome das séries

def total_ano():
    pass
    # Ano: NºFilmes NºSéries
    # 2005   34        12
    # 2006 ................
    anos = list(set([x['release_year'] for x in programas]))
    filmes = [0] * len(anos)
    series = [0] * len(anos)

    for prog in programas:
        indice = anos.index(prog['release_year'])
        if prog['type'] == "Movie":
            filmes[indice] += 1
        elif prog['type'] == "TV Show":
            series[indice] += 1
    
    juntos = sorted(zip(anos, filmes, series))
    anos2, filmes2, series2 = zip(*juntos)

    print("Ano: NºFilmes NºSéries")
    for ano, filme, serie in zip(anos2, filmes2, series2):
        print(f"{ano}   {filme:5d}  {serie:5d}")


def pesquisa_ator_atriz():
    pass
    # Lê nome
    # Mostra Ano, Filme, Elenco (em ordem de ano)

# ------------------------------------------------------ Programa Principal
while True:
    titulo("Filmes e Séries da NetFlix")
    print("1. Total de Filmes e Séries")
    print("2. Duração Média dos Filmes e Destaques (maior e menor duração)")
    print("3. Nº de Temporadas das Séries e Destaques (séries com maior temporadas)")
    print("4. Total de Filmes e Séries lançadas por Ano")
    print("5. Pesquisa de Filmes por Ator/Atriz")
    print("6. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        totais_filmes_series()
    elif opcao == 2:
        duracao_filmes()
    elif opcao == 3:
        temporadas_series()
    elif opcao == 4:
        total_ano()
    elif opcao == 5:
        pesquisa_ator_atriz()
    else:
        break
