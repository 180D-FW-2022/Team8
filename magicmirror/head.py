import threading
import os
import argparse
import struct
import wave
from threading import Thread
import pvrhino
from pvrecorder import PvRecorder
#import MagicMirror.wake as wake
#import pyautogui


#gesture control is the main control. use speech to wake engine to turn on voice control . 
#voice control performs 1 command and then shuts off and goes down to gesture control 
def wake_up(num):
    os.system('python3 wake.py --access_key 4n7j8/reOKePM5xXFp+CmSFnBsgRZ5EF2m9bjghxif/OpZCG/LHcnw== --keyword_paths ./engine_training/wake_engine.ppn')
   

def gesture_rec(num):
    os.system('python gestures.py')

#def magic_mirror(num):
   # os.system('python magic_mirror.py')

if __name__ == "__main__":
    #while
    os.system('npm start server & python3 wake.py --access_key 4n7j8/reOKePM5xXFp+CmSFnBsgRZ5EF2m9bjghxif/OpZCG/LHcnw== --keyword_paths ./engine_training/wake_engine.ppn & python3 gestures.py')
        #t1 = threading.Thread(target=wake_up, args=(10,))
        #t2 = threading.Thread(target=gesture_rec, args=(10,))
        #t3 = threading.Thread(target=magic_mirror, args=(10,))


        #t1.start()
        #t2.start()
        #t3.start
    
        # print("Done!")