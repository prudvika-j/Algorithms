import math
import copy
import operator



n = 0
visited = {}
dist = []
path = []
f_path = []
distances = []
f_cost = 999999

def load_xy(file):

    global n

    fp = open(file)
    n = int(fp.readline().strip())
    for line in fp:
        dist.append(list(map(float, line.strip().split(" "))))
    fp.close()


def row_reduction(distance):

    row_sum = 0
    for i in range(n):
        mini = min(distance[i])
        if  mini != 0 and mini != 999999:
            for j in range(n):
                if distance[i][j] != 999999:
                    distance[i][j] = distance[i][j] - mini
            row_sum = row_sum + mini
    return row_sum

def row_reductn(distance):


    for i in range(n):
        mini = min(distance[i])
        if  mini != 0 and mini != 999999:
            for j in range(n):
                if distance[i][j] != 999999:
                    distance[i][j] = distance[i][j] - mini
    return distance

def col_min(distance):

    cols = []
    for i in range(n):
        mini = 999999
        for j in range(n):
            if distance[j][i] < mini:
                mini = distance[j][i]
        cols.append(mini)
    return cols


def column_reduction(distance):

    col_sum = 0
    cols = col_min(distance)
    for i in range(n):
        mini = cols[i]
        if  mini != 0 and mini != 999999:
            for j in range(n):
                if distance[j][i] != 999999:
                    distance[j][i] = distance[j][i] - mini
            col_sum = col_sum + mini
    return col_sum

def column_reductn(distance):


    cols = col_min(distance)
    for i in range(n):
        mini = cols[i]
        if  mini != 0 and mini != 999999:
            for j in range(n):
                if distance[j][i] != 999999:
                    distance[j][i] = distance[j][i] - mini
    return distance



def get_bound(v1 , v2 , distance , pb):

    d = distance[v1][v2]
    distance = reduced_matrix(v1 , v2 , distance)
    rs  = row_reduction(distance)
    cs  = column_reduction(distance)
    return rs + cs + d + pb



def reduced_matrix(v1 , v2, distance):

    distance[v2][0] = 999999
    for j in range(n):
            distance[v1][j] = 999999
            distance[j][v2] = 999999
    return distance

def copy_path():

    print("Temporary Path = ", path)
    for i in range(n):
        f_path[i] = path[i]

def set_false():

    for i in range(n):
        visited[i] = 0


def bnb(start , pb , level , cost, distance):

    global n, f_cost
    if level == n:
        cost = cost +  dist[start][0]
        if f_cost > cost:
            print("current_cost = ", cost)
            copy_path()
            f_cost = cost
            return
    else:
        temp = cost
        bounds = {}
        for j in range(1, n):
            if visited[j] == 0:
                dst = copy.deepcopy(distance)
                bounds[j] = get_bound(start , j , dst , pb)
        #print("bounds = ", bounds)
        sorted_bounds = dict(sorted(bounds.items(), key=operator.itemgetter(1)))
        #print("bounds = ", sorted_bounds ,"  level = ", level)
        mini = 999999
        next_vertex = 0
        keys = list(sorted_bounds.keys())
        #print("keys = ", keys)
        for v in keys[:6]:
                mini = sorted_bounds[v]
                next_vertex = v
                cost = cost + dist[path[level-1]][next_vertex]
                visited[next_vertex] = 1
                path[level] = next_vertex
                print("Next bound = ", mini)
                print("Next vertex = ", next_vertex)
                dst = copy.deepcopy(distance)
                dst = reduced_matrix(start, next_vertex , dst)
                dst = row_reductn(dst)
                dst = column_reductn(dst)
                dst[start][v] = 999999
                bnb(next_vertex, mini , level + 1, cost,  dst)


                cost = temp
                set_false()
                for j in range(level):
                    visited[path[j]] = 1



if __name__=="__main__":

    load_xy("test2.txt")
    print("Number of cities = ", n)
    for i in range(n):
        visited[i] = 0
        path.append(0)
        f_path.append(0)
    distances = []
    distances =  copy.deepcopy(dist)
    lb = row_reduction(distances) + column_reduction(distances)
    path[0] = 0
    visited[0] = 1
    distance = copy.deepcopy(distances)
    bnb(0, lb, 1, 0, distance)
    print("Finding shortest length tour.....")
    print("Cost = ", f_cost)
    print("Rounded cost = ", round(f_cost))
    print("Final path = ", f_path)
