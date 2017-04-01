import threading
import time
import CrawelerMod
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter,Lock):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.Lock = Lock

    def run(self):
        print( "Starting " + self.name)
        MyCraweler = CrawelerMod.Craweler()
        MyCraweler.Crawel(self.Lock)

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
