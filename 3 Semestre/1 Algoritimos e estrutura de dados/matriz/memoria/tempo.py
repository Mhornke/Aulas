import time
from datetime import datetime
def capitura_hora():
    global hora_inicial, hora_final
    min_inicio = datetime.now()
    time.sleep(10)
    hora_inicial = min_inicio.strftime("%H:%M:%S")
# print(str_hora)

# minutos = str_hora.split(":")
# print(minutos)
# print(minutos[0])
    min_final = datetime.now()
    hora_final = min_final.strftime("%H:%M:%S")
# print(minutos[1])

    minutos, segundos = tempo()
    print(f" min {minutos}: seg{segundos}")
# print(int(minutos[1]))

# minuto = int(minutos[1])
# seg = int(minutos[2])
# tempo = (minuto*60) - seg
# print(tempo)


# time.sleep(10)
# time2 = datetime.now()
# str_hora2 = time2.strftime("%H:%M:%S")
# print(str_hora)

# print(str_hora2)

# minutos2 = str_hora2.split(":")
# minuto2 = int(minutos2[1])
# seg2 = int(minutos2[2])

# calseg = int(minuto2[2] - minuto[1])
# if calseg <0 :
#     calminuto = (minuto2 - minuto) -1
#     calseg = (seg2 - seg) + 60
#     print(f"min:{calminuto} e seg: {calseg}")
# else:
#     calminuto = (minuto2 - minuto)  
#     calseg = (seg2 - seg)  
#     print(f"min:{calminuto} e seg: {calseg}")
def tempo():  
    min_inicio = hora_inicial.split(":")
    min_final = hora_final.split(":")
    print(min_final)
    print(min_inicio)

    min1 = int(min_inicio[1])  
    seg1 = int(min_inicio[2])
    print(f"min{min1} seg{seg1}")  
   
    min2 = int(min_final[1])  
    seg2 = int(min_final[2]) 
    print(f"min{min2} seg{seg2}")  

    segundos = seg2 - seg1
    if segundos <0:
        minutos = (min1 - min2) -1
        segundos = segundos - 60
    else:
        minutos = min1 - min2
        segundos = segundos 

    
    return minutos, segundos

capitura_hora()    
tempo()