import requests
import csv 

nomesValidos= []

# Criação do arquivo .csv
with open('nomes.csv', mode='w') as arq:
    escritor = csv.writer(arq)
    escritor.writerow(['NOME', 'SEXO', 'LOCALIDADE', 'VALIDO' ])
    escritor.writerow(['JOAO', 'M', 'BR', 1 ])
    escritor.writerow(['JOAO', 'M', 'BR', 1 ])
    escritor.writerow(['JOAO', 'M', 'BR', 1 ])
    escritor.writerow(['MARIA', 'F', 'BR', 1 ])
    escritor.writerow(['MARIA', 'F', 'BR', 1 ])
    escritor.writerow(['MARIA', 'F', 'BR', 1 ])
    escritor.writerow(['MARIA', 'F', 'BR', 1 ])
    escritor.writerow(['MARIA', 'F', 'BR', 1 ])
    escritor.writerow(['ueshiuaui', 'M', 'BR', 0] )

#Função pra válidar nome 
def valida_nome():
    with open('nomes.csv', mode='r') as arq:
        leitor = csv.DictReader(arq)
        
        for linha in leitor:
            if linha['VALIDO'] != 0:
                nomesValidos.append(linha)
                response = requests.get('https://servicodados.ibge.gov.br/api/v2/censos/nomes{nome}')
            elif len(nomesValidos) == 0:
                print("Lista não contém nomes válidos!!")                
  
    print(response) # Esta retornando o status 200(dados não encontrados)
       
valida_nome()    
            
  
