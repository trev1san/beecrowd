a = float(input())
imposto = 0.0

if a <= 2000:
    print("Isento")

elif a <= 3000:
    imposto = (a - 2000) * 0.08
    print(f"R$ {imposto:.2f}")

elif a <= 4500:
    imposto = (1000 * 0.08) + (a - 3000) * 0.18
    print(f"R$ {imposto:.2f}")

else:
    imposto = (1000 * 0.08) + (1500 * 0.18) + (a - 4500) * 0.28
    print(f"R$ {imposto:.2f}")
