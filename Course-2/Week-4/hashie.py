tablesize = 0
hashtable = []
low = -10000
high = 10000
count = 0
sums = []
visited = {}

def find(ele):
    
    l = 0
    h = tablesize - 1
    while l <= h:
        m = int((l + h)/2)
        if hashtable[m] == ele:
            return m
        elif hashtable[m] > ele:
            h = m - 1
        else:
            l = m + 1
    
    return m
            
    

def all_sums(x, lb, ub):
    
    for y in range(lb, ub+1):
        if x != hashtable[y]:
        
            s = x + hashtable[y]
            if s >= low and s <= high:
                if visited[s] == 0:
                    visited[s] = 1
                    

if __name__=="__main__":
    
        
    fp = open("sum.txt")
    for num in fp:
        hashtable.append(int(num))
        
    for i in range(low, high+1):
        visited[i] = 0
        
    hashtable = list(set(hashtable))
    print("Removed duplicates")
    hashtable.sort()
    print("Array is sorted")
    
    tablesize = len(hashtable)
    print("tablesize = ", tablesize)    
    for i in hashtable:
        print("i =", i)
        lb = find(low - i)
        ub = find(high - i)
        print("lb = ",lb," ub = ", ub)
        all_sums(i, lb, ub)
        
     
    for i in range(low, high+1):
        if visited[i] == 1:
            count += 1
        
    print("Final Count = ", count)