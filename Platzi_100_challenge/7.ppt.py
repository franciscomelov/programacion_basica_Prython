def winner(player_1, player_2, cont_1, cont_2):
    if player_1 == player_2:
        print("empate")
        return cont_1, cont_2

    elif player_1 == "piedra":
        if player_2 == "papel":
            print("Gana jugador 2")
            return cont_1, cont_2+1
        else:
            print("Gana jugador 1")
            return cont_1+1, cont_2
    
    elif player_1 == "papel":
        if player_2 == "tijera":
            print("Gana jugador 2")
            return cont_1, cont_2+1
        else:
            print("Gana jugador 1")
            return cont_1+1, cont_2

    elif player_1 == "tijera":
        if player_2 == "piedra":
            print("Gana jugador 2")
            return cont_1, cont_2+1
        else:
            print("Gana jugador 1")
            return cont_1+1, cont_2

def ppt():
    partidas = 0
    cont_1 =0
    cont_2 =0
    while partidas<3:
        partidas +=1
        player_1 = input("jugador 1: ")
        player_2 = input("Jugador 2: ")
        cont_1, cont_2 = winner(player_1, player_2, cont_1, cont_2)

    print("PUNTAJE")
    print("jugador 1: ", cont_1)
    print("jugador 2: ", cont_2)

    if cont_1 > cont_2:
        print("GANADOR jugador 1")
    elif cont_2 > cont_1:
        print("GANADOR jugador 2")
    else:
        print("EMPATE")



ppt()

