import csv

with open('cardapio.csv', mode='w') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['CODIGO', 'ESPECIFICACAO', 'PRECO'])
    escritor.writerow([1, 'Cachorro Quente', 4.00])
    escritor.writerow([2, 'Cachorro Quente', 4.50])
    escritor.writerow([3, 'Cachorro Quente', 5.00])
    escritor.writerow([4, 'Cachorro Quente', 2.00])
    escritor.writerow([5, 'Cachorro Quente', 1.50])

item, quantidade = map(int, input("Digite o item e a quantidade: ").split())

total = 0.0

with open('cardapio.csv', mode='r') as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        if item == int(linha['CODIGO']):
            preco = float(linha['PRECO'])
            total = preco * quantidade
            break

print(f"Total: R$ {total:.2f}")