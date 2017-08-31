

weights = []
lengths = []
ratio = {}
ctimes = []
n = 0

def read_file():
    global n
    fp = open("jobs.txt")
    n = int(fp.readline())
    for i in range(0, n+1):
        weights.append(0)
        lengths.append(0)
    i = 1
    for line in fp:
        ln = line.split(" ")
        weights[i] = int(ln[0])
        lengths[i] = int(ln[1])
        i += 1
    
    fp.close()
    
def calculate_ratio():
    
    print("In Ratio ")
    
    for i in range(1, n+1):
        d = weights[i] / lengths[i]
        if d in ratio:
            ratio[d].append(i)
                
        else:
            ratio[d] = []
            ratio[d].append(i)
            
            
def calculate():
    
    print("In Calculate ")
    ls = []
    time = 0
    for i in ratio.keys():
        ls.append(i)
    ls.sort()
    ls.reverse()
    for i in range(0, n+1):
        ctimes.append(0)
    
    for d in ls:

        for job in ratio[d]:
            time = time + lengths[job]
            ctimes[job] = time
            
    print("Completed Calculation ")
    
            
  
 
  
def sort_jobs():
    
    print("In sort jobs")
    
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if weights[i] < weights[j]:
                temp = weights[i]
                weights[i] = weights[j]
                weights[j] = temp
                temp = lengths[i]
                lengths[i] = lengths[j]
                lengths[j] = temp
    
        
    
if __name__=="__main__":
    
    
    read_file()
    print("Total jobs = ", n)
    sort_jobs()
    calculate_ratio()
    calculate()
    s = 0
    for i in range(1, n+1):
        s = s + ( ctimes[i] * weights[i])
        
    print("Sum of weighted completion times = ", s)
        
    
    
    