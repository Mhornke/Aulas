def validar_ip(ip):
    blocos = ip.split(".")

    if len(blocos) != 4:
        return False
    
    for bloco in blocos:

        if not bloco.isdigit():
            return False
        
        numero = int(bloco)

        if numero < 0 or numero > 255:
            return False
        
    return True


while True:
    ip = input("Digite seu IP: ")

    if validar_ip(ip):
        print("O IP é válido!")
        break
    else:
        print("O IP é inválid!")