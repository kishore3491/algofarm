# Source: HackerRank
# Given an Array, find index 'i', if one exists, such that Sum(A[0:i-1]) == Sum(A[i+1:)
'''
This is one of the simple examples of dynamic programming, which can be solved very effectively by 
pre-computing cache and avoiding redudant calculations.
'''

def findBalancerIndex(Arr):
    if(len(Arr) < 2):   # Considering empty and one element arrays as satisfying the condition
        print('YES')
        return
    alen = len(Arr)
    cache = [0]*alen
    cache[0] = Arr[0]
    
    for i in range(1, alen):          # Create a Sum Cache
        cache[i] = Arr[i] + cache[i-1]
        
    res  = False
    for i in range(1, alen):
        if(cache[i-1] == (cache[alen - 1] - cache[i])):   # Check if left sum eq right sum through precomputed cache
            res  = True
            break
    if(res):
        print('YES')
    else:
        print('NO')
        
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    ar = [int(x) for x in input().strip().split()]
    findBalancerIndex(ar)
