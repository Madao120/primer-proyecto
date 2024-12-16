import random

# Valores iniciales
cempatar = 0
cganar = 0
cperder = 0

# Funciones
def menu():
    print("""
    1-  Roca
    2-  Papiro
    3-  Cizallas
    4-  Terminar la partida
    5-  Reiniciar la partida
""")

def valor_usuario(res): #Valor usuario.
    piedra, papel, tijeras = False, False, False
    if res == 1:
        piedra = True
        print ("Has escojido piedra")
    elif res == 2:
        papel = True
        print ("Has escojido papel")
    elif res == 3:
        tijeras = True
        print ("Has escojido tijeras")
    return piedra, papel, tijeras

def valor_maquina(): #Valor random de la máquina.
    mpiedra, mpapel, mtijeras = False, False, False
    maq = random.randint(1, 3)
    if maq == 1:
        mpiedra = True
        print ("Y la máquina ha escojido piedra")
    elif maq == 2:
        mpapel = True
        print ("Y la máquina ha escojido papel")
    elif maq == 3:
        mtijeras = True
        print ("Y la máquina ha escojido tijeras")
    return mpiedra, mpapel, mtijeras

def versus(piedra, papel, tijeras, mpiedra, mpapel, mtijeras, cganar, cempatar, cperder): #Resultados por cada versus.
    if mpiedra and piedra:
        cempatar += 1
        resultado = "Parece que hubo un empate"
    elif mpiedra and papel:
        cganar += 1
        resultado = "Has ganado!"
    elif mpiedra and tijeras:
        cperder += 1
        resultado = "Vaya!, parece que has perdido"
    elif mpapel and piedra:
        cperder += 1
        resultado = "Vaya!, parece que has perdido"
    elif mpapel and papel:
        cempatar += 1
        resultado = "Parece que hubo un empate"
    elif mpapel and tijeras:
        cganar += 1
        resultado = "Has ganado!"
    elif mtijeras and piedra:
        cganar += 1
        resultado = "Has ganado!"
    elif mtijeras and papel:
        cperder += 1
        resultado = "Vaya!, parece que has perdido"
    elif mtijeras and tijeras:
        cempatar += 1
        resultado = "Parece que hubo un empate"
    return resultado, cganar, cempatar, cperder

def mensaje_puntuaciones (cganar, cperder, cempatar): #Esta función definirá quien ha ganado la partida y contará los resultados según si se ha ganado empatado o perdido hasta que acabe la partida (4).
    if (cganar > 1):
        print("Has ganado un total de", cganar, "veces")
    elif (cganar == 1):
        print("Has ganado un total de", cganar, "vez")
    elif (cganar == 0):
        print ("Que mala suerte! Parece que no has ganado ninguna partida")
        
    if (cempatar > 1):
        print("Has empatado", cempatar, "veces")
    elif (cempatar == 1):
        print("Has empatado", cempatar, "vez")
    elif (cempatar == 0):
        print ("No has empatado ni 1 vez")

    if (cperder > 1):
        print("Y has perdido", cperder, "veces\n")
    elif (cperder == 1):
        print("Y has perido", cperder, "vez\n")
    elif (cperder == 0):
        print ("¡Y Guau! No has perdido ni una vez\n") 

def puntuaciones_por_ronda(cganar, cperder, cempatar): #Este es un mini menú que saltará cada vez que termine una ronda, el cual mostrará el recuento actual de la partida.
    print("Rondas ganadas:", cganar)
    print("Rondas empatadas:", cempatar)
    print("Rondas perdidas:", cperder)

def reiniciar_puntuaciones():  #5 Opción para reiniciar la partida
    return 0, 0, 0

# Ejecución del juego
print("Bienvenido al simulador de Roca Papiro y Cizallas")

replay = False

while replay != True:   #  Primer Bucle para repetir la partida
    respuesta = 0
    cganar, cperder, cempatar = reiniciar_puntuaciones()

    while respuesta != 4:   #   La Partida
        menu()
        respuesta = int(input("Escoja el número correspondiente a la palabra: "))

        if respuesta == 5:
            cganar, cperder, cempatar = reiniciar_puntuaciones()
            print("La partida ha sido reiniciada.")
        
        elif respuesta == 4:
            print("Se ha acabado la partida, estas son sus puntuaciones:")
            mensaje_puntuaciones(cganar, cperder, cempatar)
            break
            
        elif respuesta == 1 or respuesta == 2 or respuesta == 3:
            piedra, papel, tijeras = valor_usuario(respuesta)
            mpiedra, mpapel, mtijeras = valor_maquina()
            resultado, cganar, cempatar, cperder = versus(piedra, papel, tijeras, mpiedra, mpapel, mtijeras, cganar, cempatar, cperder)
            print(resultado)
            puntuaciones_por_ronda(cganar, cperder, cempatar)
            if cganar == 3 or cperder == 3: #Agregado para que finalice la partida llegado al límite de puntuación (3 puntos)
                print("\nSe ha alcanzado el límite de puntos.", "¡Has ganado!"if (cganar > cperder)else "Que lástima, has perdido.", "\n    -Recuento de rondas- \n")
                mensaje_puntuaciones(cganar, cperder, cempatar)
                break
        else:
            print("Parece que no se ha introducido un valor válido, introdúzcalo de nuevo por favor.")

    replay = input("¿Quiere Jugar otra partida? (s/n)").lower()
    if replay != "s" :
        replay = True