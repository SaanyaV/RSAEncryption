# -*- coding: utf-8 -*-
"""
Code to create PrimeNumbers
"""
import math
import time

def testPrimeBrute(a):
    if a <= 1:
        return False
    elif a == 2:
        return True
    for i in range(2, math.ceil(a**.5)+1): 
        if a % i == 0:
            return False
    return True

def firstPrime(biggerThan = 10):
    numAdd = 1
    while testPrimeBrute(biggerThan + numAdd) == False:
        numAdd = numAdd + 1
    return biggerThan + numAdd

def createPrimes(biggerThan = 10, quantity = 5):
    result = []
    while len(result) < quantity:
        prime = firstPrime(biggerThan)
        result.append(prime)
        biggerThan = prime
    return result

def primeFactorList(a):
    for i in range(2,math.ceil(a/2)+1):
        if testPrimeBrute(i):
            if a % i == 0:
                return [i,a/i]


#s = firstPrime(10000000000000000000)
#print(f"The number is {len(str(s))} digit long and is {s}. Time taken is {round(time.time() - start_time,2)} seconds")
for x in range(1,10):
    biggerThan = int(10**x)
    smallPrime =  createPrimes(biggerThan,1)
    bigPrime = createPrimes(10**10,1)
    num = int(smallPrime[0]*bigPrime[0])
    start_time = time.time()
    lenP = len(str(smallPrime[0]))
    t = primeFactorList(num)
    print(f"It took {round(time.time() - start_time,2)} seconds to find the prime factors. The smallest prime factor is {lenP} digits long.")
#print(f"The prime numbers greater than {len(str(biggerThan))-1} digit long are {s}. Time taken is {round(time.time() - start_time,2)} seconds")
