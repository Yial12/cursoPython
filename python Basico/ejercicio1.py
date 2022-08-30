def run():
    nombre = input('ingresa tu nombre: '.capitalize())
    numero = input('ingresa un numero: '.capitalize())
    numero = int(numero)
    i = 1

    while i <= numero:
        print(nombre)
        i+=1


if __name__ == '__main__':
    run()