def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(len(x)):
        inter = (x[i]- y[i])
        res+= (inter if inter>=0 else -1*inter) #Abs
    return res


def jaccard_dist(x, y): #We assume they are the same length
    xds = 0
    inter = 0
    for i in len(range(x)):
        if (x[i]==y[i]):
            inter+=1
        xds +=x[i]
    return 1.0- inter/xds

def cosine_sim(x, y):
    sum = 0
    for i in range(len(x)):
        sum += x[i] *y[i]
    return sum/(len(x) *len(y))

# Feel free to add more
