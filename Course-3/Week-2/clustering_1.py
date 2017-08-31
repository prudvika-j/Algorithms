
n = 0
edges = []
parent = []

def load_edges():
    
    global n, edges 
    fp = open("clustering1.txt")
    first_line = fp.readline()
    n = int(first_line)
    
    for line in fp:
        edge = line.split(" ")
        v1 = int(edge[0])
        v2 = int(edge[1])
        cost = int(edge[2])
        edges.append([cost , v1 ,v2])
    
    fp.close()
    edges = sorted(edges)
    
        

def find(v):
    return parent[v] 
    
    
def union(j , k):
    
    for i in range(1, n+1):
        if parent[i] == j:
            parent[i] = k
    parent[j] = k
    return True
    

def clustering():
    
    print("In Clustering")
    
    for i in range(n+1):
        parent.append(i)
        
    clusters = n
    i = 0
    
    while clusters > 4:
        cost , v1 , v2 = edges[i]
        j = find(v1)
        k = find(v2)
        if j != k:
           if union(j , k):
               clusters =  clusters - 1
        i = i + 1
        
    
    max_spacing = 999999
                
    while(i < len(edges)):
        cost , v1 , v2 = edges[i]
        if find(v1) != find(v2):
            if max_spacing > cost:
                max_spacing = cost
                break
        i = i + 1
    print("Max - Spacing: ", max_spacing)
    
            
    
    
if __name__=="__main__":
    
    load_edges()
    print("Number of nodes = ", n)
    clustering()