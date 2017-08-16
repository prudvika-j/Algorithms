import heapq

n = 0
lower = []
higher = []
median = []

def get_median():
    
    low = len(lower)
    high = len(higher)
    
    if low == high:
        return -lower[0]
    elif low < high:
        return higher[0]
    else:
        return -lower[0]
    
def addNumber(num):
    
    if len(lower) == 0:
        heapq.heappush(lower, -num)
    
    elif num <= -lower[0]:
        heapq.heappush(lower, -num)
        
    else:
        heapq.heappush(higher, num)
        
    

def balance():
    
    low = len(lower)
    high = len(higher)
    
    if low < high and high - low >= 2:
        ele = heapq.heappop(higher)
        heapq.heappush(lower, -ele)
        
    elif low > high and low - high >= 2:
        ele = -heapq.heappop(lower)
        heapq.heappush(higher, ele)
    else:
        return
    
if __name__=="__main__":
    
    fp = open("Median.txt")
    for num in fp:
        
        addNumber(int(num))
        balance()
        median.append(get_median())
        n = n + 1
    summ = 0
    for i in range(1, n+1):
        summ = summ + int(median[i-1])
    
    print("The medians are ")
    print(median)
    print("Median = ", summ % 10000)
        