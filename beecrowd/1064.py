a = []
for _ in range(6):
    a.append(float(input()))

positivos = 0
for n in a:
    if n > 0:
        positivos += 1

b = list(filter(lambda x: x > 0, a))

print(f"{positivos} valores positivos")

if positivos > 0:
    c = sum(b) / positivos
    print(f"{c:.1f}")
