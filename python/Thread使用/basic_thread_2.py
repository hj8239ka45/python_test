##  2018/12/31 basic_thread_2
##  join

import threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.2)
    print('T1 finish\n')

def T2_job():
    print('T2 start\n')
    print('T2 finish\n')

def main():
    added_thread = threading.Thread(target=thread_job,name='T1')#定義增加的線程,命名線程名稱
    added_thread2 = threading.Thread(target=T2_job)
    added_thread.start()#執行增加的線程
    added_thread2.start()
    
    added_thread2.join()#等待added_thread任務執行完後才往下執行
    print('all done\n')#先start --> all done --> finish 證明多線程
if __name__=='__main__':
    main()
