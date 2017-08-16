import random
import math
import copy

graph = {}
n = 0
m = 0

def load_graph():
    
    global n, m
    
    fp = open("kargerMinCut.txt")
    for line in fp:
        line = line.strip()
        edges = line.split("\t")
        v1 = int(edges[0])
        graph[v1] = {}
        for i in range(1, len(edges)):
            v2 = int(edges[i])
            graph[v1][v2] = 1
            m = m + 1
            
        n = n + 1
        
    fp.close()
    
def mincut(g):
    
    random.seed()
    while len(g) > 2:
        v1 = random.choice(list(g.keys()))
        v2 = random.choice(list(g[v1].keys()))
        
        for v in g[v2]:
            g[v].pop(v2)
            if  v != v1:
                    g[v][v1] = g[v].setdefault(v1, 0) + g[v2][v]
                    g[v1][v] = g[v1].setdefault(v, 0) + g[v2][v]
                    
        g.pop(v2)
        
        
        
    v1 = list(g.keys())[0]
    v2 = list(g[v1].keys())[0]
    return g[v1][v2]
    
                
            
    
if __name__=="__main__":
    
    load_graph()
    print("Number of vertices = ", n)
    print("Number of edges = ", m)
    cut = 0
    trials = 10000
    for trial in range(trials):
        print("Trial = ", trial)
        gc = copy.deepcopy(graph)
        mc = mincut(gc)
        if cut == 0:
            cut = mc
        elif cut > mc:
            cut = mc
        print("Min Cut = ",cut)
    
            