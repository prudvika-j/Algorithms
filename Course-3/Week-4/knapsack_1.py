
n = 0
w = 0
items = []
A = []

def load_items():
    
    global w, n
    
    fp = open("knapsack1.txt")
    
    wn = fp.readline().strip().split(" ")
    
    w = int(wn[0])
    n = int(wn[1])
    items.append([0])
    for line in fp:
        item  = line.strip().split(" ")
        items.append(item)
    
    fp.close()
    
    
def knapsack():
    
    for i in range(n+1):
        A.append([])
    for i in range(w+1):
        A[0].append(0)
        
    for i in range(1, n+1):
        vw = items[i]
        vi  = int(vw[0])
        wi  = int(vw[1])
        for x in range(w+1):
            if wi > x:
                A[i].append(A[i-1][x])
            else:
                A[i].append(max(A[i-1][x], vi + A[i-1][x-wi]))
                
    print("Knapsack optimal solution = ", A[n][w])
        
    
if __name__ == '__main__':
    
    load_items()
    print("Number of items = ", n)
    print("Running knapsack... ")
    knapsack()
        
    
    
    