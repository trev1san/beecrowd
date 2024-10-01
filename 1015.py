import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
o = math.sqrt((x2 - x1 ) ** 2 + (y2 - y1) **2)
print(f"{o:.4f}")  


#se usa map por causa q ja fica tudo na mesma linha, sem precisar usa outras linhas no code, o float pode ser trocado por int numa boa.