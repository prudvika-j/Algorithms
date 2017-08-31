import heapq

n = 0
weights = []
heaptree = []
v = []

class Node:
     def __init__(self,  char = None, leftchild = None, rightchild = None):
         self.char = char
         self.leftchild = leftchild
         self.rightchild = rightchild




def load_weights():

    global n
    fp = open("huffman.txt")
    n = int(fp.readline())
    for i in range(n+1):
        weights.append(0)
    i = 1
    for line in fp:
        weights[i] = int(line)
        i += 1

    fp.close()


def heap():

    for i in range(1, n+1):
        heapq.heappush(heaptree, (weights[i], Node(char = i)))




def huffman_tree():

    while len(heaptree) > 1:

        fr1, node1 = heapq.heappop(heaptree)
        fr2, node2 = heapq.heappop(heaptree)
        nn = Node('$', node1, node2)
        heapq.heappush(heaptree, (fr1 + fr2 , nn))




def traverse(root):

    l = 0
    r = 0
    if root.leftchild == None and root.rightchild == None:
        return 0
    if root.leftchild != None:
        l = traverse(root.leftchild)

    if root.rightchild != None:
        r = traverse(root.rightchild)

    return  1 + max(l , r)


if __name__=="__main__":

    load_weights()
    print("Number of characters = ", n)
    heap()
    print("Building huffman tree..")
    huffman_tree()
    tup = heapq.heappop(heaptree)
    root = tup[1]
    print("Tree Traversal ")
    print("Max Length = ",traverse(root))
