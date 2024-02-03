import os
import eel
from command import *

def start():
    print("Running...............")
    eel.init("UI")
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html', mode=None, host='localhost', block=True)
    
        
if __name__ == '__main__':
        start()
        print("system stop")   
        




