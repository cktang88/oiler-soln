from typing import List
import functools, itertools, math
import time

from bitarray import bitarray

def get_primes_below(n: int) -> str:
    mx = n>>1
    prime = bitarray(mx)  # only store odds, prime[i] = 2*i+1
    prime[:] = True
    prime[0] = False # init
    c = 0
    for i in range(3, mx*2+1, 2):
        c+=1
        if not prime[c]:
            continue
        prime[3*c+1: mx: i] = False
    return prime.to01()

def num_factors(t):
    orig = t
    numfactors = 1
    for p in primes:
        q = 0
        while t%p == 0:
            t//=p
            q += 1
        numfactors *= (q+1)
        if t == 1:
            break
    if t > 1:
        print(orig, 'bro')
    return numfactors

'''
#60
'''
# def prob60():
#     k =10000
#     a = time.time()
#     bigpt = get_primes_below(k*k)
#     b = time.time()
#     pt = get_primes_below(k)
#     primes = set((i<<1) +1 for (i,e) in enumerate(pt) if e == '1')
#     # print(len(bigpt))
#     print(len(primes))
#     c = time.time()
#     print(b-a, c-b)
#     def isprime(n):
#         if n%2==0:
#             return False
#         if n < k:
#             return n in primes
#         return bigpt[(n-1)>>1] == '1'
#     # print(isprime(201), isprime(15), isprime(211))

#     from itertools import permutations, combinations

#     rev_sorted_primes = sorted(primes, reverse=True)
#     # print(rev_sorted_primes)
#     combs = combinations(primes,2)
#     pairs = set() # Invariant: (a,b) where b > a
#     for arr in combs:
#         if arr[0] > arr[1]:
#             arr = arr[::-1]
#         a = [arr, arr[::-1]]
#         bad = any(not isprime(int(''.join([str(c) for c in perm]))) for perm in a)
#         if not bad:
#             pairs.add(arr)

#     def append_group(groups):
#         result = set()
#         for group in groups:
#             mx = group[-1]
#             for p in rev_sorted_primes:
#                 if p <= mx:
#                     break
#                 candidates = [(q, p) for q in group]
#                 bad = any((c not in pairs) for c in candidates)
#                 if not bad:
#                     result.add((*group, p))
#         return result

#     print(len(pairs), ' pairs')
#     a = time.time()
#     triples = set() # Invariant: (a,b,c) where c > b > a
#     triples = append_group(pairs)

#     print(len(triples), ' triples')
#     b = time.time()
#     print(b-a)
#     c = time.time()
#     quads = append_group(triples)
#                 # print((trip[0], trip[1], trip[2], p))
#     d = time.time()
#     print(d-c)
#     print(len(quads), ' quads')

#     # not worth optimizing, instantaneous
#     quints = append_group(quads)
#     print(quints)

# sqrt(10**14)

from operator import add, mul
mx = 250
pt = get_primes_below(math.ceil(math.sqrt(mx)))
primes = set((i<<1) +1 for (i,e) in enumerate(pt) if e == '1')
primes.add(2)
# print(primes)
mxpowers = dict()
avail = []
pre = time.time()
for p in primes:
    k = math.floor(math.log(mx, p))
    mxpowers[p] = k
    arr = list(zip(itertools.accumulate([p]*k, mul), range(1,k+1)))
    avail.extend(arr)
print(mxpowers, avail)
# print(2**46, 2**44*5)

# combos of any length
a = time.time()
print(a-pre)
all_combinations = (
    lambda ls: 
        functools.reduce(lambda a,v: a+(2<<(v-1)),
            map(
                lambda combo: functools.reduce(add, map(lambda c: c[1], combo)),
                itertools.chain.from_iterable(
                        itertools.filterfalse(
                            lambda combo: functools.reduce(mul, map(lambda c: c[0], combo)) > mx, 
                            itertools.combinations(ls, size)
                        )
                        for size in range(1, len(ls)+1)
                    )
            )
        )
)

'''
((2, 1),)
((4, 2),)
((8, 3),)
((3, 1),)
((9, 2),)
((2, 1), (4, 2))
((2, 1), (3, 1))
'''



combs = all_combinations(avail)
print(combs)
# for q in list(combs):
#     print(q)
sm = 1
# for c in combs:
#     sm += 2<<(functools.reduce(-1)
print('final ', sm)
b = time.time()
print(b-a)
