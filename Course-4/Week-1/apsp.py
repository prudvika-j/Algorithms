
n = 0
e = 0
g = {}
A = []

def load_graph(file):

    global n , e

    fp = open(file)
    ve = fp.readline().strip().split(" ")
    n = int(ve[0])
    e = int(ve[1])
    for i in range(1, n+1):
        g[i] = {}
    for line in fp:
        edge = line.strip().split(" ")
        v1 = int(edge[0])
        v2 = int(edge[1])
        cost = int(edge[2])
        g[v1][v2] = cost
    fp.close()



def apsp():

    for i in range(n+1):
        A.append([0])

    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                A[i].append(0)
            else:
                if i in g and j in g[i]:
                    A[i].append(g[i][j])
                else:
                    A[i].append(99999999)

    for k in range(1, n+1):
        print("Iteration = ", k)
        for i in range(1, n+1):
            for j in range(1, n+1):
                A[i][j] = min(A[i][j] , A[i][k] + A[k][j])



def find_cycle():

    for i in range(1, n+1):
        if A[i][i] < 0:
            return 1
    return 0


def shortest_shortest():

    shortest= 99999999
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i != j and A[i][j] < shortest:
                shortest = A[i][j]

    return shortest

if __name__=="__main__":

    load_graph("g1.txt")
    print("Number of vertices = ", n)
    print("Finding shortest paths.....")
    apsp()
    if not find_cycle():
        print("Shortest of shortest paths = ", shortest_shortest())
    else:
        print("The graph has a negative cycle")