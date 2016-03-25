# Insertion Sort

def insertionsort(ar, n):
    for i in range(n - 1):
        if(ar[i] > ar[i+1]):
            j = i+1
            done = False
            tmp = ar[j]
            while(not done and j > 0):
                if(ar[j-1] > tmp):
                    ar[j] = ar[j-1]
                else:
                    ar[j] = tmp
                    done = True
                j -= 1
            if(ar[0] > tmp):
                ar[0] = tmp
        print(*ar)
            

n = int(input().strip())

ar = [int(x) for x in input().strip().split()]

insertionsort(ar, n)
