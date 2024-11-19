import random

print("1) ✊")
print("2) ✋")
print("3) ✌️")
player = int(input("Elige un número : "))
computer = random.randint(1,3)

if player == 1:
    print("Has elegido: ✊")
elif player == 2:
    print("Has elegido: ✋")
elif player == 3:
    print("Has elegido: ✌️")
else:  
    print("Respuesta incorrecta")
    exit()

if computer == 1:
    print("CPU ha elegido: ✊")
if computer == 2:
    print("CPU ha elegido: ✋")
if computer == 3:
    print("CPU ha elegido: ✌️")

if player==computer:
    print ("Empate")
if player==1 and computer ==3:
    print("Has ganado")
if player==1 and computer ==2:
    print("Has perdido")
if player==2 and computer ==1:
    print("Has ganado")
if player==2 and computer ==3:
    print("Has perdido")
if player==3 and computer ==2:
    print("Has ganado")
if player==3 and computer ==1:
    print("Has perdido")

