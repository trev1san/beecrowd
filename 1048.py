a = float(input())
salario = 0
Reajuste = 0
percentual = 0
if a <= 400.00:
    percentual = 15
    Reajuste = (a * 15) / 100
    salario = a + Reajuste
elif a <= 800.00:
    percentual = 12
    Reajuste = (a * 12) / 100
    salario = a + Reajuste
elif a <= 1200.00:
    percentual = 10
    Reajuste = (a * 10) / 100
    salario = a + Reajuste
elif a <= 2000.00:
    percentual = 7
    Reajuste = (a * 7) / 100
    salario = a + Reajuste
elif a > 2000.00:
    percentual = 4
    Reajuste = (a * 4) / 100
    salario = a + Reajuste
print(f"Novo salario: {salario:.2f}")
print(f"Reajuste ganho: {Reajuste:.2f}") 
print(f"Em percentual: {percentual} %")