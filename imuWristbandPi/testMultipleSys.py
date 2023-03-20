#import subprocess
#from time import sleep

#y=(0.1)
#subprocess.Popen(["python", 'BerryNew.py'])
#sleep(y)
#subprocess.Popen(["python", 'test.py'])


import os
os.system("python BerryNew.py &")
os.system("python test.py &")



#import berryIMUfunction
#import subprocess
 
#if(berryIMUfunction.power() == 0):
 #   subprocess.run('vcgencmd display_power 0', shell=True)
#else:
 #   subprocess.run('vcgencmd display_power 1', shell=True)
