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
        j = partition(low, high)
        quicksort(low, j-1)
        quicksort(j+1, high)

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
quicksort(0, len(A)-1)   
print(A)
print("count = ", count)