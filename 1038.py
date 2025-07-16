precos = {
    1: 4.00,  # Cachorro Quente
    2: 4.50,  # X-Salada
    3: 5.00,  # X-Bacon
    4: 2.00,  # Torrada simples
    5: 1.50   # Refrigerante
}

codigo, quantidade = map(int, input().split())

total = precos[codigo] * quantidade

print(f"Total: R$ {total:.2f}")

#(ajuda com gpt)
