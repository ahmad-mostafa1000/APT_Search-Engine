import CrawelerMod
#import IndexerMod
import ThreadingMod
import threading
MyCraweler = CrawelerMod.Craweler()
##MyCraweler.Crawel()
##MyIndexer = IndexerMod.Indexer()

##MyIndexer.StartIndexing()
#ThreadNumber = input('Enter number of threads: ')
#MyThreads=[]
#for i in range(int(ThreadNumber)):
#    try:
#       MyThreads.append(MyThread("Thread-"+ str(i+1)))
#    except:
#       print("Error: unable to start new thread")

#MyCraweler.Crawel("https://moz.com/top500")
#MyCraweler.Crawel("https://www.facebook.com/")
#MyCraweler.Crawel("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
#MyCraweler.Crawel("http://wordpress.stackexchange.com/questions/158015/unwanted-crawl-delay-10-line-added-to-my-robots-txt")
#MyCraweler.Crawel("https://www.youtube.com/")
#MyCraweler.Crawel("http://wordpress.stackexchange.com/questions/158015/unwanted-crawl-delay-10-line-added-to-my-robots-txt")
#MyCraweler.Crawel("https://docs.python.org/3/library/re.html")

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = ThreadingMod.myThread(1, "Thread-1", 1,threadLock)
thread2 = ThreadingMod.myThread(2, "Thread-2", 2,threadLock)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for t in threads:
    t.join()
print( "Exiting Main Thread")