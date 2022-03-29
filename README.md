# Alexa-Automation
# this project was a fun way for me to learn about web sockets, voice recognition, and further expanding my knowledge on python.  This code is in relation to the 
# PICO CAR 4WD that can be found online.  This code basically allows the car to interact with a websocket and recieve vocie and keyboard inputs allowing for the car
# to drive forward, left, right, or backward.
------------------------------------------------
#client.py is the code that is run that connects to the web socket.  Input for the car can be changed by simply chaninging the variable input for 
#name in the async def hello() function.
------------------------------------------------
#keyboard_pq.py was my testing file for keyboard inputs.
------------------------------------------------
#localhostclient.py/localserver.py were used to test a websocket server and client.  These are later integrated inside of the client.py file and the main.py file.
------------------------------------------------
#main.py is the code that is uploaded onto the pico car 4wd.  This code allows the car to act like a websocket and for commands to be passed to it.
------------------------------------------------
#voicetest.py was my testing grounds for implementing voice commands to be sent over to the websocket created either virutally or through the car.
