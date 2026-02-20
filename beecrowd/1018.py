x = int(input())
print(x)
y = (100,50,20,10,5,2,1)
for y in y:
    z = x // y
    print(F"{z} nota(s) de R$ {y},00")
    x %= y