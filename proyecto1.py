import random

#valores
piedra = False
papel = False
tijeras = False
mpiedra = False
mpapel = False
mtijeras = False
cempatar = 0
cganar = 0
cperder = 0

#funciones
def menu(): #el menú que se repetirá hasta que el cliente termine la partida
    print("""
    1-  Piedra
    2-  Papel
    3-  Tijeras
    4-  Terminar la partida
""")


def valor_maquina(): #valor que escojerá la máquina aleatoriamente
    maq= random.randint(1, 3)
    if (maq == 1):
        mpiedra = True
    elif (maq == 2):
        mpapel = True
    elif (maq == 3):
        mtijera = True
    
def valor_usuario(res): #valor que escojerá el usuario
    if (res == 1):
            piedra =True
    elif (res == 2):
            papel = True
    elif (res == 3):
            tijeras = True
    elif (res == 4):
        return

def versus(): #todas las comparaciones posibles
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

def puntuaciones ():
    if (cganar > 1):
        return("Has ganado un total de ", cganar, "veces")
    elif (cganar == 1):
        print("Has ganado un total de ", cganar, "vez")
    elif (cganar == 0):
        print ("Que mala suerte! Parece que no has ganado ninguna partida (q noob)")
        
    if (cganar > 1):
        print("Has empatado", cganar, "veces")
    elif (cganar == 1):
        print("Has empatado", cganar, "vez")
    elif (cganar == 0):
        print ("No has empatado ni 1 vez")

    if (cganar > 1):
        print("Has perdido", cganar, "veces")
    elif (cganar == 1):
        print("Has perido", cganar, "vez")
    elif (cganar == 0):
        print ("Guau! No has perdido ni una vez")
    
print("Bienvenido al simulador de Roca Papiro y Cizallas") #Inicio
respuesta = 0

while (respuesta != 4):  #inicio de bucle
    menu()
    respuesta = int(input("Escoja el númeor correspondiante a la palabra"))
    if (respuesta != 1 or respuesta != 2 or respuesta != 3 or respuesta != 4):
        print("parece que no se ha introducido un valor válido")
    elif (respuesta == 1 or respuesta == 2 or respuesta == 3):
        valor_usuario(respuesta)
        valor_maquina
        versus
    elif (respuesta == 4):
        print("Se ha acabado la partida estas son sus puntuaciones:")
        puntuaciones()