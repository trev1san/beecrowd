# Exemplo rápido do que o 1064 geralmente pede:
positivos = 0
soma = 0

for _ in range(6):
    n = float(input())
    if n > 0:
        positivos += 1
        soma += n

print(f"{positivos} valores positivos")
if positivos > 0:
    print(f"{soma/positivos:.1f}")
#arrumar para o 1065, que é o próximo exercício, e tem a mesma estrutura, mas pede os pares, não os positivos.