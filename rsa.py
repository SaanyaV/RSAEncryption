#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 14:37:31 2020

@author: sunilverma
"""

import math
import random as rd
import time

class keyGen():
    """
    1. generate all primes less than a given number
    2. randomly select 2 prime numbers, p & q
    3. compute N (p * q) [@ computeN]
    4. compute phiN ((p-1)*(q-1)) [@ computePhiN]
    5. find coprimes of N and phiN [@ findCoPrimes]
    5a. requires list of primefactors of N [@ primeFactorList]
    5b. requires list of primefactors of phiN [@ primeFactorList]
    6. randomly select one coprime (e) [@ selectE - use in public key]
    7. find d [@ findD], d is always <= e
    """
    
    def __init__(self, lessthanPrime = 1000, randomValues = True):
        self.lessthanPrime = lessthanPrime
        if int(self.lessthanPrime) == self.lessthanPrime:         
            if randomValues == True:
                self.output = self.runRSA_RandomInputs()
            elif randomValues == False:
                self.output = self.runRSA_KeyboardInputs()
            else:
                print("Incorrect Specification")
        else:
            print("Provide an integer for the value of lessthanPrime")
        
        self.keys = {
            "publicKey"     : [self.output["E"], self.output["N"] ],
            "privateKey"    : [self.output["D"], self.output["N"] ] 
            }
    
    def runRSA_RandomInputs(self):
        start_time = time.time()
        pfList = self.primeNumbersLessThan(self.lessthanPrime)
        p = pfList[rd.randint(0, len(pfList)-1)]
        q = p
        while q == p:
            q = pfList[rd.randint(0, len(pfList)-1)]
        N = self.computeN(p,q)
        phiN = self.computePhiN(p, q)
        coPrimeList = self.findCoPrimes(N,phiN)
        E = self.selectE(coPrimeList)
        D = E
        while D == E:
            D = self.findD(E,phiN)
        end_time = time.time()
        print(f"Time taken to produce keys is {round(end_time - start_time,2)} seconds")
        return{ 
            "p" : p,
            "q" : q,
            "N" : N,
            "phiN" : phiN,
            "coPrimeList": coPrimeList,
            "E": E,
            "D": D
            }
    
    def runRSA_KeyboardInputs(self):
        start_time = time.time()
        checkPrime = False
        while checkPrime == False:
            p = int(input("Input an PRIME NUMBER value of p: "))
            checkPrime = self.testPrimeSmall(p)
        q = p
        checkPrime = False
        while (q == p) | (checkPrime == False):
            q = int(input("input an PRIME NUMBER value of q: "))
            checkPrime = self.testPrimeSmall(q)
        N = self.computeN(p,q)
        phiN = self.computePhiN(p, q)
        coPrimeList = self.findCoPrimes(N,phiN)
        print(coPrimeList)
        incoPrimeList = False
        while incoPrimeList == False:
            E = int(input("Please input the value of the coprime you want to use: "))
            if E in coPrimeList:
                incoPrimeList = True
        D = self.findD(E,phiN)
        end_time = time.time()
        print(f"Time taken to produce keys is {round(end_time - start_time,2)} seconds")
        return{ 
            "p" : p,
            "q" : q,
            "N" : N,
            "phiN" : phiN,
            "coPrimeList": coPrimeList,
            "E": E,
            "D": D
            }
                
    def computeN(self,p,q):
        n = p * q
        return n
    
    def computePhiN (self,p,q):
        phiN = (p-1)*(q-1)
        return phiN
    
    def findCoPrimes(self,n,phiN):
        n_primeList = self.primeFactorList(n)
        phiN_primeList = self.primeFactorList(phiN)
        primeList = n_primeList + phiN_primeList
        coprimeList = []
        for i in range(2, phiN):
            isCoprime = True
            for x in primeList:
                if i % x == 0:
                    isCoprime = False
            if isCoprime == True:
                coprimeList.append(i)                       
        return coprimeList
    
    def selectE(self,coprimeList):
        idx = rd.randint(0,len(coprimeList)-1) 
        e = coprimeList[idx]
        return e
    
    def findD(self,e,phiN):
        keepTrying = True
        d = 0
        while keepTrying:
            d=d+1
            if d*e % phiN == 1:
                keepTrying = False
        return d

    def testPrimeSmall(self,a):
        if a <= 1: 
            return False
        elif a == 2:
            return True
        for i in range(2, math.ceil(a**.5)+1): 
            if a % i == 0:
                return False
        return True
        
    def primeFactorList(self,a):
        listPFactors=[]
        for i in range(2,a+1):
            if self.testPrimeSmall(i):
                if a % i == 0:
                    listPFactors = listPFactors + [i]
        return listPFactors
        
    
k = keyGen(lessthanPrime=500, randomValues = True)
#k = keyGen(lessthanPrime=100, randomValues = False)
print(f"The value of p is: {k.output['p']}")
print(f"The value of q is: {k.output['q']}")
#print(f"The values in coprime list are: {k.output['coPrimeList']}")
print(f"The public key is [e, n]: {k.keys['publicKey']}")
print(f"The private key is [d, n]: {k.keys['privateKey']}")

