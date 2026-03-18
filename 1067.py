x = int(input())
quantidade_de_impares = 0

while quantidade_de_impares < 6:
    if x % 2 != 0:
        print(x)
        quantidade_de_impares += 1
    
    x += 1