__author__ = 'Ryan'

import itertools
class DiceBag:
    def __init__(self, dietype, numdice):
        self.dietype = dietype
        self.numdice = numdice
        self.dice = [[i for i in range(1,dietype + 1)] for j in range(numdice)]
        self.probs = self.findprobs()
        self.counts = self.findcounts()
        self.off = self.offfrompascalldiag()
        self.mean = (self.dietype * self.numdice + self.numdice)/2

    def factorial(self, n):
        num = 1
        for i in range(1,n+1):
            num = num * i
        return num

    def choose(self,n,k):
        return self.factorial(n)/(self.factorial(k) * self.factorial(n-k))

    def offfrompascalldiag(self):
        off = []
        for i in range(0, len(self.counts)):
            off.append((self.choose(self.numdice - 1 + i, self.numdice - 1) - self.counts[i]))
        return off

    def combos(self):
        return list(itertools.product(*self.dice))

    def findcounts(self):
        temp = self.sums()
        return [temp.count(i) for i in range(self.numdice, self.numdice * self.dietype + 1)]

    def sums(self):
        return [sum(i) for i in self.combos()]

    def findprobs(self):
        tot = self.dietype ** self.numdice
        sums = self.sums()
        return {i:sums.count(i)/tot for i in range(self.numdice, self.numdice * self.dietype + 1)}