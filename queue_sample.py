#Queue

from queue import Queue
q = Queue(maxsize=3)

print(q.qsize())
print(q.queue)
print(q.empty())
print(q.full())
q.put('A')
q.put('B')
q.put('C')
q.put_nowait('D')
print(q.qsize())
print(q.queue)
print(q.empty())
print(q.full())

#var = q.get()
#print(var)
#print(q.queue)
#var = q.get()
#var = q.get()
#var = q.get()
#print('処理終了')
