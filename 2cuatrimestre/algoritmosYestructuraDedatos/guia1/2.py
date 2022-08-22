def verificar_fecha():
	dia = int(input("ingrese dia"))
	mes = int(input("ingrese mes"))
	anio = int(input("ingrese anio"))
	if dia>=1:
		if mes >=1 and mes<=12:
			if mes==2:
				if dia <= 28:
					print(f"{dia}/{mes}/{anio}")
			if mes < 8 and mes%2 != 0:
				if dia<=31:
					print(f"{dia}/{mes}/{anio}")
			elif mes >= 8 and mes%2 == 0:
				if dia<=31:
					print(f"{dia}/{mes}/{anio}")
			else:
				if dia<=30:
					print(f"{dia}/{mes}/{anio}")

def main():
	verificar_fecha()

main()

