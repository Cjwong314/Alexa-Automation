from re import X
import keyboard

while True:
    if keyboard.read_key() == "p":
        print("You pressed p")
        x = "p"
    if keyboard.read_key() == "q":
         print("You pressed q")
         x = "q"
    print(x)


    