
n = 0
l = 0
nodes = []
parent = {}

def load_nodes():

    global n, l
    fp = open("clustering_big.txt")
    first_line = fp.readline()
    fl = first_line.strip().split(" ")
    n = int(fl[0])
    l = int(fl[1])

    for line in fp:
        bits = line.strip().split(" ")
        nodes.append("".join(bits))
    fp.close()

def complement(ch):
    if ch == '1':
        return '0'
    else:
        return '1'

def closest(node):

    closer = []
    for i in range(l):
        closer.append(node[:i] + complement(node[i]) + node[i+1:])
        for j in range(l):
            closer.append(node[:i] + complement(node[i]) + node[i+1:j] + complement(node[j]) + node[j+1:])
    return closer

def find(v):
    while parent[v] != v:
        v = parent[v]
    return v


def union(j , k):
    parent[k] = j


def clustering():

    for node in nodes:
        parent[node] = node
    clusters = len(parent)

    for node in nodes:
        j = find(node)
        for closest_node in closest(node):
            if parent.get(closest_node):
                k = find(closest_node)
                if j != k:
                    union(j , k)
                    clusters -= 1
                    print(clusters)

    print("Number of clusters = ", clusters)


if __name__=="__main__":

    load_nodes()
    print("Number of nodes = ", n)
    clustering()

