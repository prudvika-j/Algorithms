A = []
count = 0
def read_file():
    fp = open("in.txt", "r")
    for line in fp:
        val = line.rstrip('\n')
       # print("value = ", val)
        A.append(int(val))
    fp.close()

def quicksort(low, high):
    if low < high:
        pivot = median(low, high)
        A[low], A[pivot] = A[pivot], A[low]
        j = partition(low, high)
        quicksort(low, j-1)
        quicksort(j+1, high)
    
def median(low, high):
    mid = int((low + high)/2)
    a,b,c = A[low], A[mid], A[high]
    if a > b:
        a,b = b,a
    if a > c:
        a,c = c,a
    if b > c:
        b,c = c,b
    if A[low] == b:
        return low
    elif A[mid] == b:
        return mid
    else:
        return high

def partition(low, high):
    pivot = low
    i = low + 1
    global count
    for j in range(low+1, high+1):
        if A[j] < A[pivot]:
            A[i], A[j] = A[j], A[i]
            i = i + 1
        count = count + 1
    A[pivot], A[i-1] = A[i-1], A[pivot]
    return i-1
 
read_file()
#print("median = ", median(0, len(A)-1))
quicksort(0, len(A)-1)   
print(A)
print("count = ", count)