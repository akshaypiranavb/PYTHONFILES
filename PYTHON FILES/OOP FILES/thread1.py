#setname,getname
import threading
import time
def akshay(limit):
    for i in range(5):
        time.sleep(limit+1)
        print(threading.current_thread().getName())
        print("AKSHAY THREAD\n")
for j in range(5):
    t=threading.Thread(target=akshay,args=(5,))
    t.setName("thread"+str(j))
    t.start()
        
        