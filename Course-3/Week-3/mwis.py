
n = 0
weights = [0]

def load_vertices():

    global n

    fp = open("mwis.txt")
    n = int(fp.readline())
    for line in fp:
        weights.append(int(line))

    fp.close()


def mwis():

    values = [0, weights[1]]

    for i in range(2, n+1):
        values.append(max(values[i-1] , values[i-2]+ weights[i]))

    i = n
    vertices = set()

    while i >= 1:
        if values[i-1] >= values[i-2] + weights[i]:
            i -= 1
        else:
            vertices.add(i)
            i -= 2
    return vertices


if __name__ == '__main__':

    load_vertices()
    print("Number of vertices = ", n)
    vertices = mwis()
    print("MWIS = ", vertices)
    v = [1, 2, 3, 4, 17, 117, 517, 997]
    for ele in v:
        if ele in vertices:
            print("1")
        else:
            print("0")

