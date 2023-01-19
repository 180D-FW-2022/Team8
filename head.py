import threading
import rhino_engine
import gestures
import os

def voice_rec(num):
    os.system(' python rhino_engine.py --access_key 4n7j8/reOKePM5xXFp+CmSFnBsgRZ5EF2m9bjghxif/OpZCG/LHcnw== --context_path ./demo.rhn')

def gesture_rec(num):
    os.system('python gestures.py')

if __name__ == "__main__":
    #while
        t1 = threading.Thread(target=voice_rec, args=(10,))
        t2 = threading.Thread(target=gesture_rec, args=(10,))

        t1.start()
        t2.start()
    
        print("Done!")