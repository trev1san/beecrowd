total = int(input())
anos = total // 365
dias = total %365
mes = dias // 30
dia = dias %30
print(F"{anos:.0f} ano(s)")
print(F"{mes:.0f} mes(es)")
print (F"{dia:.0f} dia(s)")