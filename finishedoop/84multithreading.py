import threading
import time

def func(num):
    print(f"sleeping for {num} seconds")
    time.sleep(num)

t1 = threading.Thread(target=func,args=[4])
t2 = threading.Thread(target=func,args=[2])
t3= threading.Thread(target=func,args=[7])


t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()