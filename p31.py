import statistics
import math
import time
print("The value of pi is", math.pi)
seconds = time.time()
print("Seconds since epoch (the point where time begins). =", seconds)
li = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print("The average of list values is : ", end="")
print(statistics.mean(li))
local_time = time.ctime(seconds)
print("Local time:", local_time)
