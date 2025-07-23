# Lê três valores inteiros
valores = list(map(int, input().split()))

# Guarda a sequência original
original = valores[:]

# Ordena os valores
valores.sort()

# Mostra os valores em ordem crescente
for v in valores:
    print(v)

print()

# Mostra os valores na ordem original
for v in original:
    print(v)
