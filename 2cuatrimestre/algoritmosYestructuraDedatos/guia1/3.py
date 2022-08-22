VALOR_VIAJE = 100


def valor(viajes):
    total = viajes * VALOR_VIAJE

    while viajes > 0:
        if viajes >= 40:
            total = total - (VALOR_VIAJE * 0.4)
            viajes = viajes - 1
        elif viajes >= 31 and viajes <= 40:
            total = total - (VALOR_VIAJE * 0.3)
            viajes = viajes - 1
        elif viajes >= 21 and viajes <= 30:
            total = total - (VALOR_VIAJE * 0.2)
            viajes = viajes - 1
        elif viajes >= 1 and viajes <= 20:
            viajes = viajes - 1

    return total


def main():
    viajes = int(input("Ingrese viajes"))
    valor_viajes = valor(viajes)
    print(valor_viajes)


main()
