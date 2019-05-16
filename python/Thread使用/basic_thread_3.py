##  2018/12/31 basic_thread_3
##  queue
##  FIFO隊列:先進先出 queue.Queue
##  LIFO隊列:後進先出 queue.LifoQueue
##  優先級隊列: queue.PriorityQueue

import threading
import time
from queue import Queue

def job(l,q):
    for i in range(len(l)):
        l[i] = l[i]**2
    q.put(l)

def multithreading(data):
    q = Queue() #q中存放返回值，代替return的返回值
    threads = []
    for i in range(4): #定義四個線程
        t = threading.Thread(target=job,args=(data[i],q))#job為索引，參數在args加入
        t.start()
        threads.append(t)#把每个线程append到线程列表中
    for thread in threads:#等每一個線程運行後再回到後續
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())#q.get()按顺序从q中拿出一个值
    print(results)
    
if __name__=='__main__':
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    multithreading(data)
