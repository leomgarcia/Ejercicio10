import stats.data as s_d

lista = []
while True:
    numero = input("numeros para estadisticas: ")
    if numero == "fin":
        break
    numero = float(numero)
    lista.append(numero)
calculo_stats = s_d.StatsData(lista)

print("Lista numeros: ", calculo_stats.l_data)
print("Media: ", calculo_stats.mean)
print("Mediana: ", calculo_stats.median)
print("Varianza: ", calculo_stats.variance)