from time import time
from functools import lru_cache

class Fibonacci:

    def __init__(self):
        self.cache = {0: 0, 1: 1}

    def calcola_elemento_con_cache(self, n):
        if n in self.cache.keys():
            return self.cache[n]
        else:
            res =  self.calcola_elemento_con_cache(n-1) + self.calcola_elemento_con_cache(n-2)
            self.cache[n] = res
            return res

    def calcola_elemento(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calcola_elemento(n-1) + self.calcola_elemento(n-2)

    @lru_cache(maxsize=None)
    def calcola_elemento_lru(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calcola_elemento_lru(n-1) + self.calcola_elemento_lru(n-2)

if __name__=="__main__":
    n = 999
    start = time()
    print(Fibonacci().calcola_elemento_lru(n))
    end  = time()
    print(f"tempo impiegato: {end - start}")