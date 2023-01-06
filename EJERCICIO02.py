notas = [20, 15, 12, 11, 8, 4, 1]
print(notas)
minimo=notas[0]
for i in range(len(notas)):
    if minimo>notas[i]:
        minimo=notas[i]
print(minimo)

for j in range(len(notas)):
    if minimo==notas[j]:
        notas.remove(minimo)
print(notas)