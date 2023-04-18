#create,start,sleep
import threading
import time
def akshay(limit,sleeptime,threadname):
    for i in range(limit):
        time.sleep(sleeptime)
        print(threadname+"\n")
t=threading.Thread( target=akshay, args=(3,2,"AKSHAY'S THREAD",))#limit,sleeptime,threadname
t.start()
t1=threading.Thread(target=akshay,args=(3,1,"PIRANAV'S THREAD",))
t1.start()