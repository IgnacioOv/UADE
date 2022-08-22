def maximo():
	maximo = 0
	repetido = 0
	for i in range(3):
		numero = int(input("Ingrese un numero"))
		if numero>maximo:
			maximo = numero
		elif numero == maximo:
			repetido = numero

	if repetido == maximo:
		return -1
	else:
		return maximo

def main():
	numero = maximo()
	print(numero)

main()

