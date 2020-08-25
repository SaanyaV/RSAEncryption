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
    5b. requires list of primes less than phiN [@ primeFactorLessThan]
    5.b.1. requires a test of prime number [@ testPrimeSmall]
    6. randomly select one coprime (e) [@ selectE]
    7. find d [@ findD], d is always <= e
    """
    
    def __init__(self,lessthanPrime = 1000, randomPQ = True):
        if randomPQ == True:
            lessthanPrime = lessthanPrime
            pfList = self.primeFactorLessThan(lessthanPrime)
            self.p = pfList[rd.randint(0, len(pfList)-1)]
            self.q=self.p
            while self.q == self.p:
                self.q = pfList[rd.randint(0, len(pfList)-1)]
        else:
            self.p = int(input("Input an integer value of p: "))
            self.q = int(input("input an integer value of q: "))
            
        self.N = self.computeN(self.p,self.q)
        self.phiN = self.computePhiN(self.p, self.q)
        #result = self.generateKeys(N,phiN)
        
    def generateKeys(self):
        start_time = time.time()
        coPrimeList = self.findCoPrimes(self.N,self.phiN)
        E = self.selectE(coPrimeList)
        #D = self.findD(E,self.phiN)
        D = self.findD_K(E,self.phiN)
        result = {
            "N": self.N,
            "phiN":self.phiN,
            "E-public":E,
            "D-private":D}
        end_time = time.time()
        print(f"time taken is {round(end_time - start_time,2)} seconds")
        return result
                
    def computeN(self,p,q):
        n = p * q
        return n
    
    def computePhiN (self,p,q):
        phiN = (p-1)*(q-1)
        return phiN
    
    def findCoPrimes(self,n,phiN):
        n_primeList = self.primeFactorList(n)
        phiN_primesLessThan = self.primeFactorLessThan(phiN)
        for i in n_primeList:
            if i in phiN_primesLessThan:
                phiN_primesLessThan.remove(i)
        return phiN_primesLessThan
    
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
    
    def findD_K(self,e,phiN):
        d = 1
        keepTrying = True
        while keepTrying:
            #print (d)
            tmp_d = (1+d*phiN)/e
            if (int(tmp_d) == tmp_d) | (d == e) :
                keepTrying = False
            d = d + 1
        return d
        
    
    def primeFactorLessThan(self,a):
        pFactors =[2]
        if a <= 2:
            pFactors = [2]
        else:
            for i in range(3,a+1):
                if self.testPrimeSmall(i):
                    pFactors = pFactors + [i]
        return pFactors  

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
        
    
k = keyGen(lessthanPrime=2000, randomPQ = True)
#k = keyGen(lessthanPrime=100, randomPQ = False)
      
