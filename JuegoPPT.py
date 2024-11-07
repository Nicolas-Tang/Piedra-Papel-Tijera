

nombre1 = input("Como se llama el jugador 1? ")
nombre2 = input("Como se llama el jugador 2? ")

turnos = 0

while turnos < 3:
    turnos += 1

    jugador1 = input("Hola " + nombre1 + ", que elijes? piedra, papel o tijera?").lower()
    jugador2 = input("Hola " + nombre2 + ", que elijes? piedra, papel o tijera?").lower()

    condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijera" and jugador2 == "papel"

    if jugador1  == jugador2:
        print("Ha sido un empate")
    elif  condicion1 or condicion2 or condicion3:
        print("Ha ganado: ", nombre1)
    else:
        print("Ha ganado: ", nombre2)
    

