
n = 0
w = 0
items = []


def load_items():

    global w, n

    fp = open("knapsack_big.txt")

    wn = fp.readline().strip().split(" ")

    w = int(wn[0])
    n = int(wn[1])
    items.append([0])
    for line in fp:
        item  = line.strip().split(" ")
        items.append(item)

    fp.close()


def knapsack():

    prev_row = []


    for i in range(w+1):
        prev_row.append(0)

    for i in range(1, n+1):
        print("Ieration ", i)
        vw = items[i]
        vi  = int(vw[0])
        wi  = int(vw[1])
        current_row = []
        for x in range(w+1):
            if wi > x:
                current_row.append(prev_row[x])
            else:
                current_row.append(max(prev_row[x], vi + prev_row[x-wi]))

        prev_row = current_row

    print("Knapsack optimal solution = ", prev_row[w])


if __name__ == '__main__':

    load_items()
    print("Number of items = ", n)
    print("Running knapsack... ")
    knapsack()



