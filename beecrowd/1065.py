a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
positivos = 0
for n in [a, b, c, d, e]:
    if n > 0:
        positivos += 1
print(f"{positivos} valores positivos")