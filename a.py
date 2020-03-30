from typing import List
import itertools, math
from functools import lru_cache, reduce
from operator import add, mul
from itertools import permutations, combinations
from collections import Counter
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

@lru_cache(maxsize=10000)
def sum_divisors(t):
    orig = t
    sm = 1
    for p in primes:
        q = 0
        cnt = 0
        if p > t:
            break
        while t%p == 0:
            t//=p
            cnt += 1
        if cnt:
            sm *= sum(math.pow(p, i) for i in range(cnt+1))
        if t == 1:
            break
    if t > 1:
        print(orig, 'bro')
    return int(sm - orig)

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

'''
#708 - incomplete
'''
# sqrt(10**14)

# from operator import add, mul
# mx = 95
# pt = get_primes_below(math.ceil(math.sqrt(mx)))
# primes = set((i<<1) +1 for (i,e) in enumerate(pt) if e == '1')
# primes.add(2)
# # print(primes)
# mxpowers = dict()
# avail = []
# pre = time.time()
# for p in primes:
#     k = math.floor(math.log(mx, p))
#     mxpowers[p] = k
#     arr = list(zip(itertools.accumulate([p]*k, mul), range(1,k+1)))
#     avail.extend(arr)
# print(mxpowers, avail)
# # print(2**46, 2**44*5)

# # combos of any length
# a = time.time()
# print(a-pre)
# all_combinations = (
#     lambda ls: 
#         # reduce(lambda a,v: a+(2<<(v-1)),
#         #     map(
#         #         lambda combo: reduce(add, map(lambda c: c[1], combo)),
#                 itertools.chain.from_iterable(
#                         itertools.filterfalse(
#                             lambda combo: reduce(mul, map(lambda c: c[0], combo)) > mx, 
#                             itertools.combinations(ls, size)
#                         )
#                         for size in range(1, len(ls)+1)
#                     )
#         #     )
#         # )
# )

# '''
# ((2, 1),)
# ((4, 2),)
# ((8, 3),)
# ((3, 1),)
# ((9, 2),)
# ((2, 1), (4, 2))
# ((2, 1), (3, 1))
# '''


# combs = []
# # combs = all_combinations(avail)
# print(combs)
# # for q in list(combs):
# #     print(q)
# twopow = [2<<i for i in range(mxpowers[2]+1)]
# print(twopow)
# sm = 1
# for combo in combs:
#     k =0
#     for c in combo:
#         k += c[1]
#     sm += twopow[k-1]
# print('final ', sm)
# b = time.time()
# print(b-a)

# sm = 1
# cache = dict() # num: num_prime_factors
# for t in range(3, mx,2):

#     if t in primes:
#         sm += 2
#         continue
#     q = 0
#     for p in primes:
#         while t%p == 0:
#             t//=p
#             q += 1
#         if t == 1:
#             break

#         if t in cache:
#             q += cache[t]
#             break
#     cache[t] = q
#     if q > mxpowers[2]:
#         print(cache)
#         print(q)
#     sm += twopow[q-1]
# print('final_ ', sm)
# c = time.time()
# print(c-b)

# k = reduce(lambda a,v: a*v, range(1,101))
# print(sum(int(i) for i in str(k)))

'''
#21
'''

# def phi(n): 
#     result = 1
#     for i in range(2, n):
#         if (math.gcd(i, n) == 1): 
#             result+=1
#     return result

# mx = 10000
# pt = get_primes_below(mx)
# primes = set((i<<1) +1 for (i,e) in enumerate(pt) if e == '1')
# primes.add(2)
# primes = sorted(primes)
# # print(sum_divisors(284))
# arr =set()
# for i in range(1, mx):
#     for j in range(i+1, mx):
#         if sum_divisors(i) == j and sum_divisors(j) ==i: # using lru_cache :)
#             arr.add(i)
#             arr.add(j)
#             print(i,j)
# print(sum(arr))            

'''
#22
'''

# a = open('names.txt').readlines()
# names = [w[1:-1] for w in a[0].split(',')]
# import string
# s = '0' + string.ascii_uppercase
# sm = 0
# for ind, name in enumerate(sorted(names)):
#     if name == 'COLIN':
#         print(sum(s.index(i) for i in name), (ind+1))
#     sm += sum(s.index(i) for i in name)*(ind+1)
# print(sm)

'''
#23
'''
# mx = 28123
# pt = get_primes_below(mx)
# primes = set((i<<1) +1 for (i,e) in enumerate(pt) if e == '1')
# primes.add(2)
# primes = sorted(primes)

# abundant = []
# for i in range(3, mx):
#     if sum_divisors(i) > i:
#         abundant.append(i)
# print(len(abundant), abundant[:10])

# possible = set()
# for a in abundant:
#     for b in abundant:
#         if a+b > mx:
#             break
#         possible.add(a+b)
# sm = 0
# for i in range(mx):
#     if i not in possible:
#         # print(i)
#         sm += i
# print(sm)
    
'''
#35
'''
# mx = 10**6
# print(mx)
# pt = get_primes_below(mx)
# primes = set((i<<1) +1 for (i,e) in enumerate(pt) if e == '1')
# primes.add(2)
# print(len(primes))

# bad = [0,2,4,5,6,8]

# cnt = 2 # for 2, 5
# for p in primes:
#     # if any even digits, skip
#     # if contains 0 or 5, skip
#     s = str(p)
#     if any(int(i) in bad for i in s):
#         continue
#     if any(int(s[i:] + s[:i]) not in primes for i in range(len(s))):
#         continue
#     cnt += 1
# print(cnt)

'''
#32
'''
# prods = set() # catch duplicates
# # case1: 1d*4d = 4d
# for i in range(1,10):
#     dig = list(str(i) for i in range(1,10))
#     dig.remove(str(i))
#     a,b = '', ''
#     for d in permutations(dig):
#         a = int(''.join(d[:4]))
#         b = int(''.join(d[4:]))
#         if b<a:
#             continue
#         if i * a == b:
#             print(i,a,b)
#             prods.add(b)

# # case2: 2d*3d=4d
# maindig = list(str(i) for i in range(1,10))
# for i in permutations(maindig, 2):
#     dig = list(str(i) for i in range(1,10))
#     dig.remove(i[0])
#     dig.remove(i[1])
#     a,b = '', ''
#     n = int(''.join(i))
#     for d in permutations(dig):
#         a = int(''.join(d[:3]))
#         b = int(''.join(d[3:]))
#         # print(n,a,b)
#         if b<a:
#             continue
#         if n * a == b:
#             print(n,a,b)
#             prods.add(b)
# print(sum(prods))

'''
#38
'''
# # ans must be >= 918273645
# # cases
# # 2d can't work b/c 2d+3d+3d != 9
# # 3d can't work b/c 3d+4d+4d != 9
# # 4d will work...
# dig = list(str(i) for i in range(2, 8))
# for d in permutations(dig):
#     a = 9000 + int(''.join(d[:3]))
#     b = 18000 + int(''.join(d[3:]))
#     if b == 2*a:
#         print(a,b)

'''
#46
'''
# mx = 10**6
# print(mx)
# pt = get_primes_below(mx)
# primes = set((i<<1) +1 for (i,e) in enumerate(pt) if e == '1')
# primes.add(2)
# primes = list(sorted(primes))
# print(len(primes), primes[:10])

# twosq = [2*i*i for i in range(1, math.floor(math.sqrt(mx)/1.4))]
# # print(twosq)

# for i in range(3,mx,2):
#     if i in primes:
#         continue
#     found = False
#     for p in primes:
#         if p > i:
#             found = False
#             break
#         for ts in twosq:
#             if p + ts > i:
#                 break
#             if p + ts == i:
#                 found = True
#                 break
#         if found:
#             break
#     if not found:
#         print(i)
#         break


'''
#65
'''
# mx = 98
# dig = [2*(i+2)//3 if (i-1)%3==0 else 1 for i in range(mx+1)]
# # dig = [2 for i in range(mx+1)]
# print(dig)
# curbot = dig.pop()
# curtop = 1
# front = 2
# for i in range(mx):

#     ind = mx - i-1
    
#     # print(ind, curtop, curbot)
#     # print(ind)
#     curtop = curbot*dig[ind] + curtop
#     curtop, curbot = curbot, curtop

# print(curtop+front*curbot, curbot)
# print(sum(int(i) for i in str(curtop+front*curbot)))

'''
#92
'''
# a = set([1]) # 1
# b = set([89]) #89
# for i in range(1, 10**7):
#     tmp = i
#     buff = [i]
#     while True:
#         if tmp in a:
#             a.update(buff)
#             break
#         if tmp in b:
#             b.update(buff)
#             break
#         tmp = sum(int(i)**2 for i in str(tmp))
#         buff.append(tmp)
#         # print(tmp)
# print(len(a), len(b))
'''
#89
'''
# d = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000,
# }
# inp = [l.strip() for l in open('./p089_roman.txt').readlines()]
# # inp = inp[:5]
# print(inp)
# cnt = 0
# for num in inp:
#     c = Counter(num)
#     print(num)
#     if c['D'] > 1 or c['L'] > 1 or c['V'] > 1:
#         print('bro')
#         break
#     newnum = num
#     newnum = newnum.replace('DCCCC', 'CM')
#     newnum = newnum.replace('CCCC', 'CD')
    
#     newnum = newnum.replace('LXXXX', 'XC')
#     newnum = newnum.replace('XXXX', 'XL')

#     newnum = newnum.replace('VIIII', 'IX')
#     newnum = newnum.replace('IIII', 'IV')
#     diff = len(num) - len(newnum)
#     cnt += diff
#     print(newnum if diff else '')
# print(cnt)

'''
#79
'''
# inp = [l.strip() for l in open('./p079_keylog.txt').readlines()]
# # inp = inp[:4]
# print(inp)
# sums = [0]*10
# times = [0]*10
# for i in inp:
#     for j in range(len(i)):
#         n = int(i[j])
#         sums[n] += j+1
#         times[n] += 1
# arr = [sums[i]/ times[i] if times[i] > 0 else 0 for i in range(10)]
# # print(sums, times)

# ns = sorted(range(10), key=lambda x:arr[x])
# for i in ns:
#     print(i, arr[i])

'''
#27
'''
# mx = 1000
# pt = get_primes_below(mx*100)
# primes = set((i<<1) +1 for (i,e) in enumerate(pt) if e == '1')
# primes.add(2)
# primes = list(sorted(primes))
# ps = set(primes)
# # b must be positive prime, b+a+1 must be prime
# # print(primes)
# for a in range(-1*mx, mx):
#     for b in primes:
#         if b > mx:
#             break
#         # if a == 1 and b== 41:
#         #     print(b, (b+a) in ps)
#         if b+a+1 not in ps:
#             continue
#         for n in range(9999):

#             if n*(n+a) + b not in primes:
#                 break
#         if n>40:
#             print(a,b,n)


'''
#81
'''
# arr = [[int(k) for k in row.split(',')] for row in open('./p081_matrix.txt').readlines()]
# # print(arr)
# # arr = [[1,1,1], [1,1,1], [1,1,1]]
# mx = len(arr)
# print(arr[0])
# for i in range(1, mx):
#     arr[i][0] += arr[i-1][0]
#     arr[0][i] += arr[0][i-1]

# for q in range(1, mx):
#     arr[q][q] += min(arr[q-1][q], arr[q][q-1])
#     for i in range(q+1, mx):
#         arr[i][q] += min(arr[i-1][q], arr[i][q-1])
#         arr[q][i] += min(arr[q][i-1], arr[q-1][i])
# # print(arr[0])
# print(arr[-1][-1])
# # print(arr)

'''
#243
'''
