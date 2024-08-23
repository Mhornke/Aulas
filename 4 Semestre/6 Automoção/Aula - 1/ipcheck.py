
while True:
    num = input("digite um ip valido: ")
    checkIP = num.split(".")
    
    if len(checkIP) == 4:
        print("Ip Valido!")
        break
    else:
        print("ip invalido!")
        







#print(checkIP)