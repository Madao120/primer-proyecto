import random #import para hacer que la mñaqiuna pueda escoger un nñumero aleatorio dentro de un rango

#valores
cempatar = 0
cganar = 0
cperder = 0
respuesta = 0


#funciones
def menu(): #el menú que se repetirá hasta que el cliente termine la partida
    print("""
    1-  Roca
    2-  Papiro
    3-  Cizallas
    4-  Terminar la partida
""")
    
def valor_usuario(res, piedra, papel, tijeras): #valor que escojerá el usuario
    if (res == 1):
        piedra = True
        return ("Has escojido piedra")
    elif (res == 2):
        papel = True
        return ("Has escojido papel")
    elif (res == 3):
        tijeras = True
        return ("Has escojido tijeras")
    elif (res == 4):
        return

def valor_maquina(mpiedra, mpapel, mtijeras): #valor que escojerá la máquina aleatoriamente
    maq= random.randint(1, 3)
    if (maq == 1):
        mpiedra = True
        return ("Y la máquina ha escojido piedra")
    elif (maq == 2):
        mpapel = True
        return ("Y la máquina ha escojido papel")
    elif (maq == 3):
        mtijera = True
        return ("Y la máquina ha escojido tijeras")

def versus(piedra, papel, tijeras, mpiedra, mpapel, mtijeras, cganar, cempatar, cperder): #todas las comparaciones posibles y contadores de los resultados para posteriormente mostrarlos al terminar la partida
    if (mpiedra and piedra):
        cempatar += 1
        return("Parece que hubo un empate")
    elif (mpiedra and papel):
        cganar += 1
        return("Has ganado!")
    elif (mpiedra and tijeras):
        cperder += 1
        return("Vaya!, parece que has perdido")
    elif (mpapel and piedra):
        cperder += 1
        return("Vaya!, parece que has perdido")
    elif (mpapel and papel):
        cempatar += 1
        return("Parece que hubo un empate")
    elif (mpapel and tijeras):
        cganar += 1
        return("Has ganado!")
    elif (mtijeras and piedra):
        cganar += 1
        return("Has ganado!")
    elif (mtijeras and papel):
        cperder += 1
        return("Vaya!, parece que has perdido")
    elif (mtijeras and tijeras):
        cempatar += 1
        return("Parece que hubo un empate")

def puntuaciones (cganar, cperder, cempatar):    #Esta función definirá quien ha ganado la partida y contará los resultados según si se ha ganado empatado o perdido hasta que acabe la partida (4)
    if (cganar > 1):
        return("Has ganado un total de ", cganar, "veces, Felicidades!")
    elif (cganar == 1):
        print("Has ganado un total de ", cganar, "vez")
    elif (cganar == 0):
        print ("Que mala suerte! Parece que no has ganado ninguna partida (q noob)")
        
    if (cempatar > 1):
        print("Has empatado", cempatar, "veces")
    elif (cempatar == 1):
        print("Has empatado", cempatar, "vez")
    elif (cempatar == 0):
        print ("No has empatado ni 1 vez")

    if (cperder > 1):
        print("Y has perdido", cperder, "veces")
    elif (cperder == 1):
        print("Y has perido", cperder, "vez")
    elif (cperder == 0):
        print ("¡Y Guau! No has perdido ni una vez")

#def bucle_menu_fin ():  #inicio de bucle y la función que contiene las demás

print("Bienvenido al simulador de Roca Papiro y Cizallas") #Inicio

respuesta = 0
while (respuesta != 4):  
    menu()
    piedra = False
    papel = False
    tijeras = False
    mpiedra = False
    mpapel = False
    mtijeras = False
    respuesta = int(input("Escoja el número correspondiante a la palabra"))
    if (respuesta != 1 and respuesta != 2 and respuesta != 3 and respuesta != 4):
        print("parece que no se ha introducido un valor válido, introdúzcalo de nuevo por favor.")
    elif (respuesta == 1 or respuesta == 2 or respuesta == 3):
        valor_usuario(respuesta, piedra, papel, tijeras)
        valor_maquina(mpiedra, mpapel, mtijeras)
        versus(piedra, papel, tijeras, mpiedra, mpapel, mtijeras, cganar, cperder, cempatar)
    elif (respuesta == 4):
        print("Se ha acabado la partida estas son sus puntuaciones:")
        puntuaciones(cganar, cperder, cempatar)

#bucle_menu_fin()
