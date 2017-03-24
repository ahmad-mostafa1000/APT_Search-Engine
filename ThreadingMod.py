import threading
import time

class myThread (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):

        # Get lock to synchronize threads
        threadLock.acquire()
        #Entering database and getting links !!!!!!!!!!!!
        print(' In')
        time.sleep(3)
        print(' out')
        # Free lock to release next thread
        threadLock.release()
        # Crawling Here !!!!!!!!!!!!!!!!!!!!!!!


threadLock = threading.Lock()
threads = []


# Create new threads
thread1 = myThread('s')
thread2 = myThread('w')
thread3 = myThread('o')
thread4 = myThread('t')
thread5 = myThread('a')
# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
threads.append(thread4)
threads.append(thread5)
# Wait for all threads to complete
for t in threads:
    t.join()
print("Exiting Main Thread")

#synchronized(mLock)
#{

#/ * Do
#critical
#work * /

#}