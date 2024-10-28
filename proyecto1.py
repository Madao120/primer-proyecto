import random
piedra = False
papel = False
tijeras = False
mpiedra = False
mpapel = False
mtijera = False

def funcion():
    maq= random.randint(1, 3)
    res = int(input(""))

    if (maq == 1):
        mpiedra = True
    elif (maq == 2):
        mpapel = True
    elif (maq == 3):
        mtijera = True
    
    if (res == 1):
            piedra =True
    elif (res == 2):
            papel = True
    elif (maq == 3):
            tijeras = True

    if (mpiedra and piedra):
          return("Parece que hubo un empate")
    elif (mpiedra and papel):
          return("Has ganado, que te aproveche el pollo")
    elif (mpiedra and tijeras):
          return("Vaya!, pare que has  perdido")
    elif (mpiedra and piedra):
          return("Parece que hubo un empate")



    if (res != piedra or res != papel or res != tijera):
        print("parece que no se ha introducido un valor válido")
    elif (res)