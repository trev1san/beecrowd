dia_inicio = int(input().split()[1])
h_i, m_i, s_i = map(int, input().split(" : "))

dia_fim = int(input().split()[1])
h_f, m_f, s_f = map(int, input().split(" : "))

inicio_em_segundos = s_i + (m_i * 60) + (h_i * 3600) + (dia_inicio * 86400)
fim_em_segundos = s_f + (m_f * 60) + (h_f * 3600) + (dia_fim * 86400)

duracao_total = fim_em_segundos - inicio_em_segundos

dias = duracao_total // 86400
duracao_total = duracao_total % 86400

horas = duracao_total // 3600
duracao_total = duracao_total % 3600

minutos = duracao_total // 60
segundos = duracao_total % 60

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")