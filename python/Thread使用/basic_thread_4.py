##  2018/12/31 basic_thread_4
##  GIL不一定有效率: 多線程不一定比較快
##  Global Interpreter Lock
##为了让各个线程能够平均利用CPU时间，python会计算当前已执行的微代码数量，
##达到一定阈值后就强制释放GIL。而这时也会触发一次操作系统的线程调度
##（当然是否真正进行上下文切换由操作系统自主决定）。

import threading
from queue import Queue
import copy
import time

def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)


def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))#由0~999999
    s_t = time.time()
    normal(l*4)
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)
