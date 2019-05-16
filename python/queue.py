import queue

q_1 = queue.Queue()
q_2 = queue.Queue()
#put items at the end of the queue
for x in range(9):
    q_1.put("item-" + str(x))

#remove items from the head of the queue
while not q_1.empty():
    print (q_1.get())
    print(q_1.empty())
#put items at the end of the queue
for x in range(9):
    q_2.put("item-" + str(x+9))

#remove items from the head of the queue
while not q_2.empty():
    print (q_2.get())
