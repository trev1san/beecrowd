import sys
valores = [float(linha) for linha in sys.stdin]
positivos = sum(1 for valor in valores if valor > 0)
print(f"{positivos} valores positivos")