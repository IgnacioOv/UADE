import math as m
import random

MAX_TRANSPORTE = 500 
MAX_NARANJAS_CAJON = 100

def verificar_peso(naranjas):
	naranjas_cajon = []
	naranjas_jugo = 0
	for i in range(naranjas):
		peso_naranja = random.randint(150,350)

		if peso_naranja >= 200 and peso_naranja <= 300:
			naranjas_cajon.append(peso_naranja)
		else:
			naranjas_jugo = naranjas_jugo + 1

	cant_naranjas = len(naranjas_cajon)

	return naranjas_cajon,naranjas_jugo,cant_naranjas


def contar_camiones(cajones,naranjas_cajon,cant_naranjas):
	camiones = 0
	total_kilos = sum(naranjas_cajon)/1000
	restante = 0
	while total_kilos >= (MAX_TRANSPORTE*0.8):
		
		if total_kilos >= 500:
			camiones = camiones + 1
			total_kilos = total_kilos - 500
		elif total_kilos > 400 and total_kilos < 500:
			camiones = camiones + 1
			total_kilos = total_kilos - total_kilos
		
	return camiones,round(total_kilos)
	
def main():
	naranjas = int(input("Ingrese la cantidad de naranjas: "))
	naranjas_cajon,naranjas_jugo,cant_naranjas = verificar_peso(naranjas)
	cajones = m.floor(cant_naranjas/100)
	camiones,restante = contar_camiones(cajones,naranjas_cajon,cant_naranjas)
	print(f"Salieron {camiones} camiones")
	print(f"Sobraron {restante}KG de naranja")
	print(f"Se pudieron armar {cajones} cajones")
	print(f"Quedaron {naranjas_jugo} naranjas para jugo")
main()