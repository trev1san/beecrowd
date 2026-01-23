try:
    entrada = input().split()
    hora_inicial = int(entrada[0])
    minuto_inicial = int(entrada[1])
    hora_final = int(entrada[2])
    minuto_final = int(entrada[3])
    
except:
    hora_inicial = 0
    minuto_inicial = 0
    hora_final = 0
    minuto_final = 0
minutos_inicial =  ( (hora_inicial * 60) + minuto_inicial)
minutos_final = ( (hora_final * 60) + minuto_final)

if minutos_inicial >= minutos_final:
    duracao = (24 * 60 - minutos_inicial + minutos_final) // 60
else:
    duracao = (minutos_final - minutos_inicial) // 60

duracao_minuto = (minutos_final - minutos_inicial) % 60

print(f"O JOGO DUROU {duracao} HORA(S) E {duracao_minuto} MINUTO(S)")    