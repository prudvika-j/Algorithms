mst = []
near = {}
graph = {}
n = 0
m = 0
mincost = 0

def load_graph():
    
    global n , m
    fp = open("edges.txt")
    first_line = fp.readline().split(" ")
    n = int(first_line[0])
    m = int(first_line[1])
    for i in range( 1, n+1):
        graph[i] = {}
    for line in fp:
        edge = line.split(" ")
        v1 = int(edge[0])
        v2 = int(edge[1])
        cost = int(edge[2])
        graph[v1][v2] = cost
        graph[v2][v1] = cost
        
    fp.close()
        
def prim(source):
    
    print("Running Prims ")
    
    global mincost
    
    for i in range(1, n+1):
        near[i] = 999999
    near[source] = 0
    while len(mst) < n:
        
        mini = 999999
        j = -1
        for i in range(1, n+1):
            if mini > near[i] and i not in mst:
                mini = near[i]
                j = i
        
        
        mincost = mincost + near[j]
        mst.append(j)
        
        for i in range(1, n+1):
            if i in graph[j]: 
                if near[i] > graph[j][i] and i not in mst:
                    near[i] = graph[j][i]
    
    
    print("Prims Ended ")
    
if __name__=="__main__":
    load_graph()
    print("Number of vertices = ", n)
    print("Number of edges = ", m)
    prim(1)
    print("Minimum Spanning Tree =", mst)
    print("Minimum Cost = ", mincost)
    