import csv

compras = []

with open("compras.csv","r") as arq:
    produtos = csv.DictReader(arq)
    for produto in produtos:
        produto['codigo'] = int(produto['codigo'])
        produto['preco'] = float(produto['preco'])
        compras.append(produto)
    #print(compras)
        
def pesquisa():
    codigo = int(input("codigo do produto: "))     
    quant = int(input("quantidade do produto: "))     
    
    for produto in compras:
        if codigo == int(produto["codigo"]):
            print(f" codigo {produto["codigo"]}")        
            valor = float(produto['preco']) * quant
            print(f"{valor:.2f}")        
        
        
while True:
    pesquisa()    
        
        
        
        
        
        
        
        
        
        
        
        
        