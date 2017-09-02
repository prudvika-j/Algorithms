


n = 0
visited = []
dist = []
path = []
fs = 999999
fpath = []

def load_xy(file):

    global n

    fp = open(file)
    n = int(fp.readline().strip())
    for line in fp:
        dist.append(list(map(float, line.strip().split(" "))))
    fp.close()

def second_min(i):

    mini = min(dist[i])
    s_mini = 999999
    for j in range(n):
        if s_mini > dist[i][j] and dist[i][j] != mini:
            s_mini = dist[i][j]
    return s_mini

def copy_path():

    print("Temporary Path = ", path)
    for i in range(n):
        fpath[i] = path[i]


def set_false():

    for i in range(n):
        visited[i] = 0


def tsp(cb , cw , level):

    global n, fs
    if level == n:
        cr = 0
        if dist[path[level-1]][0] != 999999:
            cr = cw + dist[path[level-1]][0]
        if cr < fs:
            copy_path()
            fs = cr
            print("Current Cost = ", fs)
        return

    for i in range(1, n):
        if dist[path[level-1]][i] != 999999 and visited[i] == 0:
            temp  = cb
            cw = cw + dist[path[level-1]][i]

            if level == 1:
                cb = cb - ((min(dist[path[level-1]]) + min(dist[i]))/2)
            else:
                cb = cb - ((second_min(path[level-1]) + min(dist[i]))/2)
            if cb+cw < fs:
                path[level] = i
                visited[i] = 1
                tsp(cb, cw , level+1)

            cw = cw - dist[path[level-1]][i]
            cb = temp
            set_false()
            for j in range(level):
                visited[path[j]] = 1


def get_bound():

    pb = 0.0
    for i in range(n):
        fmin = min(dist[i])
        smin = second_min(i)
        print("fmin = ", fmin , "smin = ", smin)
        pb = pb + fmin + smin
    pb = pb / 2
    print("parent bound = ", pb)
    visited[0] = 1
    path[0] = 0
    tsp(pb, 0 , 1)




if __name__=="__main__":


    load_xy("test.txt")
    print("Number of cities = ", n)
    print("distance = ", dist)
    for i in range(n):
        visited.append(0)
        fpath.append(0)
        path.append(-1)
    get_bound()
    print("cost = ", fs)
    print("Final path = ", fpath)