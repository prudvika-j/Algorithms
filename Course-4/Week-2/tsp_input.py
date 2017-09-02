import math

n = 0
cords = []
distance = [0]

def load_xy(file):

    global n

    fp = open(file)
    n = int(fp.readline().strip())
    for line in fp:
        x , y = line.strip().split(" ")
        cords.append((float(x) , float(y)))
    fp.close()


def get_distance(x1, y1, x2, y2):

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)



def calculate_distances():

    for i in range(1, n+1):
        distance.append([0])
    i = 1
    for (x1 , y1) in cords:
        for (x2 , y2) in cords:
            distance[i].append(get_distance(x1, y1, x2, y2))
        i += 1




if __name__=="__main__":

    load_xy("tsp.txt")
    print("Number of cities = ", n)
    print("Writing to test file...")
    calculate_distances()
    fp = open("test.txt", "w")
    fp.write(str(n) + "\n")
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                fp.write("999999 ")
            else:
                fp.write(str(distance[i][j]) + " ")

        fp.write("\n")
