#import IndexerMod
import ThreadingMod
import threading
##MyCraweler.Crawel()
##MyIndexer = IndexerMod.Indexer()

##MyIndexer.StartIndexing()

#MyThreads=[]

#MyCraweler.Crawel("https://moz.com/top500")
#MyCraweler.Crawel("https://www.facebook.com/")
#MyCraweler.Crawel("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
#MyCraweler.Crawel("http://wordpress.stackexchange.com/questions/158015/unwanted-crawl-delay-10-line-added-to-my-robots-txt")
#MyCraweler.Crawel("https://www.youtube.com/")
#MyCraweler.Crawel("http://wordpress.stackexchange.com/questions/158015/unwanted-crawl-delay-10-line-added-to-my-robots-txt")
#MyCraweler.Crawel("https://docs.python.org/3/library/re.html")

threadLock = threading.Lock()
MyThreads = []
ThreadNumber = input('Enter number of threads: ')
# Create new threads

for i in range(int(ThreadNumber)):
    try:
       MyThreads.append(ThreadingMod.myThread(1, "Thread-"+str(i+1), 1,threadLock))
    except:
       print("Error: unable to start new thread")

for i in range(int(ThreadNumber)):
    MyThreads[i].start()


# Wait for all threads to complete
for i in MyThreads:
    i.join()

print( "Exiting Main Thread")
