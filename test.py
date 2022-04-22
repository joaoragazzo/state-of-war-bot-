lista = ['2','10','15','1','3','2.5','2.333','14.9']
lista_int = []

for n in lista:
    n = float(n)
    lista_int.append(n)

lista_int.sort()
print(lista_int[:3])


