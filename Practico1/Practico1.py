import random

def adivinar(intentos):
    numeroaleatorio = random.randint(0, 100)
    print(numeroaleatorio)
    for i in range(0, intentos):
        numeroingresado = int(input('Ingrese un entero: '))
        if numeroingresado == numeroaleatorio:
            print('Felicitaciones, adivinaste.')
            i=i+1
            print('Adivinaste en', i ,'intentos')
            break
        elif numeroingresado < numeroaleatorio:
            print('No, es un poco mayor')
        else:
            print('No, es un poco menor')
    else:
        print('Se acabaron los intentos')

intentos = int(input('Ingrese la cantidad de intentos (entre 0 y 100):'))
adivinar(intentos)