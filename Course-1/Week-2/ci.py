c = 0
A = []
B = []
n = 0
k = 0
def read_file():
    fp = open("inp.txt", "r")
    for line in fp:
        val = line.rstrip('\n')
       # print("value = ", val)
        A.append(int(val))
        B.append(0)
    fp.close()
    
def merge( low, mid, high ):
    i = low
    j = mid + 1
   # print("low = ", low, " high = ", high)
    global c
    k = low
    while i <= mid and j <= high:
        if A[i] < A[j]:
            B[k] = A[i]
            i = i + 1
            
        else:
            c = c + mid - i + 1
            B[k] = A[j]
            j = j + 1
        k = k + 1 
    
    #print(" count = ",c)
    
    #print(" i = ", i, " j = ", j, " k = ",k)
    
    while i <= mid :
            B[k] = A[i]
            i = i + 1
            k = k + 1
    while j <= high:
            B[k] = A[j]
            j = j + 1
            k = k + 1
            
    for i in range (low, high + 1 ):
        A[i] = B[i]
    return
            
        
def count( low, high ):
    if low < high:
        mid = int((low + high)/2)
        count ( low, mid )
        count ( mid+1, high )
        merge ( low, mid, high)
    return

read_file()
n = len(A)
count( 0, n-1 )
print("count = ",c)
#print(B)