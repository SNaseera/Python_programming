import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)

time1 = time.perf_counter()
# func(10)
# func(2)
# func(7)
# func(1)
# time2 = time.perf_counter()
# print(time1)
# print(time2)
# print(time2-time1)
t1 = threading.Thread(target=func, args=[10])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[7])
t4 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
time2 = time.perf_counter()
print(time1)
print(time2)
print(time2-time1)