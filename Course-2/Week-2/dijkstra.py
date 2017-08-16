g = {}
visited = {}
dist = {}
n = 200
count = 0
#dijkstraData.txt
def load_graph():
    
    for i in range(1, n+1):
        g[i] = {}
    fp = open("dijkstraData.txt")
    for line in fp:
        line = line.strip()
        edges = line.split("\t")
        key = int(edges[0])
        length = len(edges)
        for i in range(1, length):
            edge_cost = edges[i].split(",")
            g[key][int(edge_cost[0])] = int(edge_cost[1])
        
    fp.close()
    
def min(dist):
    
    min = 1000000
    loc = 0
    for i in range(1, n+1):
        if dist[i] < min and visited[i] == 0:
            min = dist[i]
            loc = i
            
    return loc
    
def dijkstra(source):
    
    print("In Dijkstra")
    
    for i in range(1, n+1):
        visited[i] = 0
        dist[i] = 1000000
    
    edge = g[source]
    for key in edge.keys():
        dist[key] = edge[key]
        
    dist[source] = 0
    visited[source] = 1
    
    for i in range(2, n+1):
        u = min(dist)
        visited[u] = 1
        edges = g[u]
        for w in edges.keys():
            if visited[w] == 0:
                if dist[w] > dist[u] + g[u][w]:
                    dist[w] = dist[u] + g[u][w]
    
        
    
    
if __name__=="__main__":
    load_graph()
    print("Number of vertices = ", n)
    dijkstra(1)
    print("Dijkstra Ended ")
    print(dist)
    