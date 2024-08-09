import time

# clock = time.strftime("%H:%M:%S")

# print(clock)
t1=time.time()

epoc = time.time()
print(epoc)
i=0                                       #<------whatever u place here it will calculate time it took to run this code
while i<5:
    print(i)
    i=i+1
t1 = time.time()-t1
print(t1)