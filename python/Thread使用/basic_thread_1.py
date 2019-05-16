##  2018/12/31 basic_thread_1
##  thread
import threading

def thread_job():
    print('This is an added Thread, number is %s'% threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job,name='T1')#定義增加的線程
    added_thread.start()#執行增加的線程
    print(threading.active_count())#目前執行的線程數
    print(threading.enumerate())#目前執行的線程名稱
    print(threading.current_thread())#運行程序使用的線程

#main()
if __name__=='__main__':
    main()
##    #本函式執行時__name__預設為'__main__'；若是引用其他程式如123.py則為'123'
##    #如此可以避免程式在運行時重複執了import時的程式以及使用函式時的文字
##    #http://blog.castman.net/%E6%95%99%E5%AD%B8/2018/01/27/python-name-main.html
##    
