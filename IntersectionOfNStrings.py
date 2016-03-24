'''
Given N Strings/Lists/Arrays/Sets, find intersection of all. 
'''

# The idea is to use two sets as cache, emptying one of them after every even/odd iteration.
# The time complexity will be O(N), N = Number of input lists, or O(N^2) if you were checking against each element,
# where as space complexity is O(2N) for two cache sets, provided python is capable of recycling the sets instead of 
# creating new ones after each clear() call.
def intersection(S):
    slen = len(S)
    
    if(slen == 0):
        return 0
    elif(slen == 1):
        return len(S[0])
    
    oddcache = set()
    evencache = set()
    
    init = S[0]
    for e in range(len(init)):
        evencache.add(init[e])

    k = 1
    while(k < slen):
        st = S[k]
        # Even cache
        if(k%2 == 0):      
            for i in range(len(st)):
                if(st[i] in oddcache):
                    evencache.add(st[i])
            oddcache.clear()
                
        # Odd cache
        else:
            for i in range(len(st)):
                if(st[i] in evencache):
                    oddcache.add(st[i])
            evencache.clear()
            
        k += 1
    
    if(not evencache):
        return len(oddcache)
    else:
        return len(evencache)


n = int(input().strip())  

S = []
for i in range(n):
    S.append(input().strip())

print(intersection(S))
