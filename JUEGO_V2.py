import random #se importa la librería para que la computadora eliga al azar una de las 3 opciones

# se crea un diccionario con las 9 variables posibles del juego junto a la variable ganadora, para luego comparar con la opción del jugador y la computadora
combinaciones_totales={"piedra"+"papel":"papel",
            "piedra"+"tijera":"piedra",
            "piedra"+"piedra":"empate",
            "tijera"+"papel":"tijera",
            "tijera"+"piedra":"piedra",
            "tijera"+"tijera":"empate",
            "papel"+"papel":"empate",
            "papel"+"tijera":"tijera",
            "papel"+"piedra":"papel"
            }

print("INSTRUCCIONES")
print("Solo se debe digitar 'piedra', 'papel' o 'tijera' en minúsculas")
print("Al inicio podrá elegir el número de vidas, que gane el mejor!")

print("-------")

nombre_jugador = input("Ingrese su nombre: ") #para una mayor personalización, se pide el nombre del jugador
print("-------")

opciones_validas = ["piedra", "papel", "tijera"] #se crea una tupla con las 3 opciones posibles para evitar errores

#se desea validar que el jugador digite un número, caso contrario se pedirá otra vez
while True:
    vidas_totales =input("¿Cuantas vidas desea?: ") #se pide cuantas vidas empezará cada uno
    if vidas_totales.isdigit():# si el valor ingresado es un número, pasará al siguiente paso sino se volverá a pedir
        vidas_totales = int(vidas_totales)  #si el valor digitado es un número, este se convertirá a entero y se saldrá del buble
        break
    else:
        print("Ingrese un número válido")
        print("-------")

#se aplica el número de vidas para ambos(jugador y computadora)
vida_jugador = vidas_totales
vida_computadora = vidas_totales
print("-------")
#Se usa el while para que cuando alguien llegue a 0 se termine el juego
while(vida_jugador > 0 and vida_computadora > 0):

    #Se usa otro while para validar que el jugador solo digite una de las 3 opciones
    while True:
        usuario = input("Digite una opción (piedra, papel o tijera): ")
        if usuario in opciones_validas:
            break
        else:
            print("Opción no válida, vuelva a intentarlo")
            print("-------")
    print("-------")
    #La computadora elije al azar una de las opciones que constan en la tupla
    computadora = random.choice(opciones_validas)
    print ("La computadora elije: ", computadora)

    for combinacion, resultado in combinaciones_totales.items():
        if usuario + computadora == combinacion:
            if resultado == usuario:
                vida_computadora -= 1
                print("Gana ", nombre_jugador)
            elif resultado == computadora:
                vida_jugador -= 1
                print("Gana la computadora")   
            else:
                print("Empate, siga intentando")
    print("Vidas del jugador:", vida_jugador, "- Vidas de la computadora:", vida_computadora)
    print("-------")

# Como uno de los dos debió llegar a 0, se compara con el jugador, si tiene 0 significa que ganó la computadora, sino el ganador es el jugador
if vida_jugador == 0:
    print("Gana la computadora, más suerte la próxima vez")   
else:
    print("Gana ", nombre_jugador, ", Felicidades!!")   
