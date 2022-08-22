# Resolver el siguiente problema diseñando y utilizando funciones:
# Un productor frutihortícola desea contabilizar sus cajones de naranjas según el pe-so para poder cargar el camión de reparto. 
# La empresa cuenta con N camiones, y cada  uno  puede  transportar  hasta  media  tonelada  (500  kilogramos). 
# En  un  cajón caben 100 naranjas con un peso entre 200 y 300 gramos cada una. Si el peso de alguna naranja se encuentra fuera del rango indicado, 
# se clasifica para procesar co-mo jugo. Se solicita desarrollar un programa para ingresar la cantidad de naranjas cosechadas e informar cuántos cajones se pueden llenar, 
# cuántas naranjas son pa-ra jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente reparto. Simular el peso de cada unidad generando un número entero al azar entre 150 y 350.Además,
# se  desea  saber  cuántos  camiones  se  necesitan  para  transportar  la  cose-cha,  considerando  que  la  ocupación  del  camión  no  debe  ser  inferior  al  80%; 
# en caso contrario el camión no serán despachado por su alto costo.

'''
1. pedir la cantidad de naranjas cosechadas
0. simular el peso de cada naranja con random entre 150 y 300
0. si el peso de la naranja esta fuera del rango, se clasifica para jugo
2.en un cajon entran 100 naranjas
3. en un camion entran 500 kilogramos
4. el camion solo se puede despachar si va cargado minimo hasta el 80&
5. saber cuantos camiones se necesitan para transportar la cosecha


'''
import random


MAX_TRANSPORTE = 500
MAX_NARANJAS = 100

def verificar_peso(naranjas):
	consumo = 0
	jugo = 0
	total_peso = 0
	restantes = 0
	peso_restante = 0

	cajones = naranjas/MAX_NARANJAS
	

	for i in range(naranjas):
		peso_naranja = random.randint(150,300)
		if peso_naranja >= 200 and peso_naranja <= 300:
		
			consumo = consumo + 1
			total_peso = total_peso + peso_naranja


		else:
			jugo = jugo + 1

		promedio_peso = total_peso/naranjas
		
	return consumo, jugo,total_peso,restantes,cajones


def ingresar_naranjas():
	naranjas = int(input("Ingrese cantidad de naranjas"))

	return naranjas

def verificar_camion(total_peso):
	camiones = 0
	peso_kg = total_peso/1000
	if (MAX_TRANSPORTE * 0.8) >= peso_kg:
		print("No se llega al peso para despachar por lo menos 1 camion.")
	elif peso_kg >= MAX_TRANSPORTE:
		while peso_kg>=MAX_TRANSPORTE:
			if peso_kg > (MAX_TRANSPORTE*0.8) and peso_kg < MAX_TRANSPORTE:
				peso_kg = peso_kg - (MAX_TRANSPORTE*0.8)
				camiones = camiones + 1
			else:	
				peso_kg = peso_kg - MAX_TRANSPORTE
				camiones = camiones + 1
	return camiones
			


def mostrar_datos(camiones,jugo,restantes):
	if camiones>=1:
		print(f"1.Cantidad de camiones: {camiones} \n 2. Cantidad de naranjas para jugo: {jugo} \n 3.Naranjas restantes: {restantes}")

def main():
	naranjas = ingresar_naranjas()
	consumo, jugo,total_peso,restantes,cajones = verificar_peso(naranjas)
	camiones = verificar_camion(total_peso)
	mostrar_datos(camiones,jugo,restantes)
	

main()

