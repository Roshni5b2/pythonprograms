from queue import LifoQueue
s = LifoQueue()
s.put('eat')
s.put('sleep')
s.put('code')
print(s.get())
print(s.get())
print(s.get())
print(s.get())
