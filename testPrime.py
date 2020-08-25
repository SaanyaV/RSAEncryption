import math
import time

def testPrimeSmall(a):
    start_time = time.time()
    if a <= 1:
        print(f"Time taken to produce keys is {round(time.time() - start_time,2)} seconds")
        return False
    elif a == 2:
        print(f"Time taken to produce keys is {round(time.time() - start_time,2)} seconds")
        return True
    for i in range(2, math.ceil(a**.5)+1): 
        if a % i == 0:
            print(f"Time taken to produce keys is {round(time.time() - start_time,2)} seconds")
            return False
    print(f"Time taken to produce keys is {round(time.time() - start_time,2)} seconds")
    return True

s = testPrimeSmall(205401818722163128368902805803)
