import math

n = 0
cords = [0]
visited = {}
cost = 0

def load_xy(file):

    global n

    fp = open(file)
    n = int(fp.readline().strip())
    for line in fp:
        line = line.strip().split(" ")
        x  , y = line[1] , line[2]
        cords.append((float(x) , float(y)))
    fp.close()


def get_distance(v1 , v2):

    x1, y1 = cords[v1]
    x2, y2 = cords[v2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)



def nn():

    global cost
    count = 0
    current_vertex = 1
    visited[current_vertex] = 1

    while(count < n-1):

        mini = 1000000
        next_vertex = 0
        for v in range(2, n+1):
            if visited[v] == 0:
                dist = get_distance(current_vertex , v)
                if mini > dist:
                    mini = dist
                    next_vertex = v
        visited[next_vertex] = 1
        cost = cost + mini
        current_vertex = next_vertex
        count += 1
        print("Count = ", count)


    cost = cost + get_distance(current_vertex , 1)
    print("Tour Cost = ", cost)





if __name__=="__main__":

    load_xy("nn.txt")
    print("Number of cities = ", n)
    for i in range(1, n+1):
        visited[i] = 0
    print("Calculating tour cost...")
    nn()


