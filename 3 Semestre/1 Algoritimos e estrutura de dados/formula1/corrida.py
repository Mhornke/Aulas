import csv

corridas = []

with open("winners.csv", encoding="utf-8") as arq:
    linhas = csv.DictReader(arq)
    for linha in linhas:
        corridas.append(linha)

def titulo(texto):
    print()
    print(texto)
    print("="*40)


#- Top 10 pilotos com maior número de vitórias
#- Compara Equipes (ler 2 equipes e mostrar total de vitórias de cada uma)
#- Top 5 vitórias com menor tempo 
#   Tempo, Piloto, Grande Prêmio e Data
#- Pesquisa por Piloto (corrida, ano, local das vitórias)
#- Novos vencedores nos últimos 3 anos (Vencedores novos em 2022, em 2023 e em 2024).

def  top_10():
    #- Top 10 pilotos com maior número de vitórias 
    piloto = list(set(x['Winner'] for x in corridas))
    numeros = [0] * len(piloto)

    for vencida in corridas:
       i = piloto.index(vencida['Winner'])
       numeros[i] += len(vencida['Winner'])
       
    juntos = sorted(zip(numeros, piloto), reverse=True)
    numeros2, piloto2 = zip(*juntos)     

    titulo("top 10 pilotos com maior vitoria ")
    print("\n Nome do piloto..............vencidas")
    for contador, (piloto, num) in enumerate(zip(piloto2, numeros2), start=1):
      print(f"{contador:2d} {piloto:25s} {num}")
      if contador == 10:
         break
    print(" "*40)

def total_vitorias_por_equipe():
    
    #- Compara Equipes (ler 2 equipes e mostrar total de vitórias de cada uma)
    equipes = list(set(x['Car'] for x in corridas))
    numeros = [0] *len(equipes)
    equipe1 = input("Equipe 1:")
    equipe2 = input("Equipe 2:")
    
    # for vencida in corridas:
    #     i = equipes.index(vencida['Car'])
    #     numeros[i] += len(vencida['Car'])
        
    # juntos =sorted(zip(numeros, equipes), reverse=True) 
    # numeros2, equipes2 = zip(*juntos)  
    primeira = len([x for x in corridas if x['Car'] == equipe1])
    segunda = len([x for x in corridas if x['Car'] == equipe2])
    
    titulo("Comparação de Equipes")
    print(f"Equipe: {equipe1} {primeira}")
    print(f"Equipe: {equipe2} {segunda}")



def top_5_vitorias():
    #- Top 5 vitórias com menor tempo 
#   Tempo, Piloto, Grande Prêmio e Data

   

       
    titulo("top 10 pilotos com maior vitoria ")
    print("\n Nome do piloto..............vencidas")
    for contador, corrida in enumerate(tempo2[:5], start=1):
         print(f"{contador:2d} {menor['Time']:15s} {corrida['Winner']:10} {corrida['Grand Prix']:10s} {corrida['Date']}")
     
    print(" "*40)




while True:
    titulo("Historico de Corridas da Formula 1")
    print("1. Top 10 pilotos com maior vitoria")
    print("2. Comparação de equipes")
    print("3. Top 5 menores tempos")
    print("4. x")
    print("5. x")
    print("6. Finalizar")
    opcao = int(input("Opção: "))
    if opcao == 1:
        top_10()  
    elif opcao == 2:
        total_vitorias_por_equipe()  
    elif opcao == 3:
        top_5_vitorias() 
        

    elif opcao == 6:
        break  
    else:
        break
