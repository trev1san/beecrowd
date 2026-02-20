try:
    entrada = input().split()
    hora_inicial = int(entrada[0])
    hora_final = int(entrada[1])
except:
    hora_inicial = 0
    hora_final = 0
    
duracao = 0

if hora_inicial > hora_final:
    duracao = (24 - hora_inicial) + hora_final

elif hora_inicial < hora_final:
    duracao = hora_final - hora_inicial
    duracao = 24
    
print(f"O JOGO DUROU {duracao} HORA(S)")