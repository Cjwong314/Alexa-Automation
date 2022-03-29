from ws import WS_Server
import json
import time
import pico_4wd as car

#Post Man 
#{"D": "true"}
#ws://192.168.1.127:8765 for Etavon
#ws://192.168.10.107:8765 for LHS
NAME = "my_pico_car"

#Wifi at Home
# WIFI_MODE = "sta"
# SSID = "Etavon"
# PASSWORD = "CU must win!"

# Wifi at Lutheran 
WIFI_MODE = "sta"
SSID = "LHS"
PASSWORD = "Turn in your homework."


ws = WS_Server(name=NAME, mode=WIFI_MODE, ssid=SSID, password=PASSWORD)
ws.start()

def on_receive(data):
    
    if "W" in data.keys():
        car.move("forward", 50)
        
    if "S" in data.keys():
        car.move("backward", 50)

    if "A" in data.keys():
        car.move("left", 50)
       
    if "D" in data.keys():
        car.move("right", 50)
        

ws.on_receive = on_receive

def main():
    print("start")
    while True:
        ws.loop()

try:
    main()
finally:
    car.move("stop")
    car.set_light_off()
