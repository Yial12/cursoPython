def run():
    edad = input('que edad tienes ?'.capitalize())
    edad = int(edad)

    if edad >= 18:
        print('eres mayor de edad'.capitalize())
    else:
        print('eres menor de edad'.capitalize())


if __name__ == '__main__':
    run()
