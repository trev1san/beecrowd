a = int(input())

horas = (a // 3600)
segr = (a % 3600)
min = (segr // 60)
seg = (segr % 60)

print(F"{horas:.0f}:{min:.0f}:{seg:.0f}")
#segr = segundos restantes, min = minutos, seg = segundos