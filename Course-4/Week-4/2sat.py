import sys, resource
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))

g = {}
gt = {}
n = 0
file_name = "2sat1.txt"
visited = {}
stk = []
count = 0
counter = 0
sccs = {}


def load_graph():

    global count , n
    fp = open(file_name)
    n = int(fp.readline().strip())
    for i in range(-n,n+1):
        g[i], gt[i]  = [], []
    for line in fp:
        edge = line.split(" ")
        v1 = int(edge[0])
        v2 = int(edge[1])
        g[-v1].append(v2)
        g[-v2].append(v1)
        gt[v2].append(-v1)
        gt[v1].append(-v2)
        count +=1
    fp.close()



def dfs(start, graph):


    visited[start] = 1
    for node in graph[start]:
        if visited[node] == 0:
            dfs(node, graph)

    stk.extend([start])


def dfs2(start, graph):

    visited[start] = 1
    for node in graph[start]:
        if visited[node] == 0:
            dfs2(node, graph )
    sccs[start] = counter



def dft(graph):

    for i in range(-n, n+1):
        visited[i] = 0
    for node in range(-n, n+1):
        if  visited[node] == 0 and node !=0:
            dfs(node, graph)



def scc():

    for i in range(-n, n+1):
        visited[i] = 0
    global counter
    while stk:
        node = stk.pop();
        if visited[node] == 0:
            counter += 1
            dfs2(node, gt )

def sat():

    print("Checking Satisfiability...")
    for i in range(1 , n+1):
        if sccs[-i] == sccs[i]:
            print("Unsatisfiable ")
            return 0
    return 1




if __name__=="__main__":
    load_graph()
    print("Number of variables =", n)
    print("Number of clauses =", count)
    dft(g)
    print("Calculating Strongly connected components")
    scc()
    if sat():
        print("Satisfiable ")
