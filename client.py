import asyncio
import websockets
import keyboard
import speech_recognition as sr
from gtts import gTTS
# Initialize the recognizer
r = sr.Recognizer()
 
def test_key():   
    name = ""
    if keyboard.read_key() == "a":
        name = '{"A": "true"}'
    if keyboard.read_key() == "w":
        name = '{"W": "true"}'
    if keyboard.read_key() == "s":
        name = '{"S": "true"}'
    if keyboard.read_key() == "d":
        
        name = '{"D": "true"}'
    return name

def voice():
     with sr.Microphone() as source2:
            name = ""
            # wait for a second to let the recognizer, adjust the energy threshold 
            # based on the surrounding noise level
           
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            #listens for the user's input
            audio2 = r.listen(source2)
             
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
 
            print("Did you say "+MyText)
            #SpeakText(MyText)

            if "back" in MyText:
                print("moving back")
                name  = '{"S": "true"}'
            if "left" in MyText:
                print("left")
                name = '{"A": "true"}'
            if "right" in MyText:
                print("right")
                name = '{"D": "true"}'
            if "forward" in MyText:
                print("forward")
                name = '{"W": "true"}'
            return name
        
# sends name to websocket
async def hello():
        #name = test_key()
    name = voice()
   
    #uri = "ws://localhost:8765"
    #luhi
    #uri = "ws://192.168.10.107:8765"
    #home
    uri = "ws://192.168.1.127:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")

def main():
    #voice()
    asyncio.run(hello())

while True:
    try: 
        main()
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occured")