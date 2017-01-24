#Programa en python de las tablas de multiplicar

for i in range(1,11):
	print("Tablas de multiplicar de " + str(i))
	for j in range(1,11):
		print(i * j)
	i = i + 1
