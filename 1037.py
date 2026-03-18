x = float(input())

# Check in which interval the value falls
if 0 <= x <= 25:
    print("Intervalo [0,25]")
elif 25 < x <= 50:
    print("Intervalo (25,50]")
elif 50 < x <= 75:
    print("Intervalo (50,75]")
elif 75 < x <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")










#Operadores de comparação (relacionais)
#OP      Significado         Exemplo (True)
#>     maior               2 > 1
#>=      maior ou igual      2 >= 2
#<       menor               1 < 2
#<=      menor ou igual      2 <= 2
#==      igual               'a' == 'a'
#!=      diferente           'a' != 'b'