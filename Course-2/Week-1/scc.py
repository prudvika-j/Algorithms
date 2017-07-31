import sys, resource
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))

g = {}
gt = {}
n = 875714
file_name = "source.txt"
visited = {}
size = []
stk = []
count = 0

def load_graph():
    
    global count
    for i in range(1,n+1):
        g[i], gt[i]  = [], []
    fp = open(file_name)
    for line in fp:
        edge = line.split(" ")
        key = int(edge[0])
        val = int(edge[1])
        g[key].append(val)
        gt[val].append(key)
        count +=1
    fp.close()
    
    
def dfs(start, graph):
    
    c = 1
    visited[start] = 1
    for node in graph[start]:
        if visited[node] == 0:
            c  = c + dfs(node, graph)
           
    stk.extend([start])
    return c
    
    
    
def dft(graph):
    
    for i in range(1,n+1):
        visited[i] = 0 
    for node in range(1, n+1):
        if visited[node] == 0:
            dfs(node, graph)
            


def scc():
    
    print("Started SCC")
    for i in range(1,n+1):
        visited[i] = 0
    while stk:
       node = stk.pop();
       if visited[node] == 0:
           size.extend([dfs(node, gt)])
           
if __name__=="__main__":
    load_graph()
    print("Number of vertices =", n)
    print("Number of edges =", count)
    dft(g)
    print("Calculating Strongly connected components")
    scc()
    print("Strongly Connected Components are")
    size.sort()
    print(size[-5:])