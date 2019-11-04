### import src.function as f

def condconcat(df): 
    a=("surfing","fishing","swimming","diving","other")
    l1=[]

    for e in df:
        if e>=1000:
            l1.append(a[0])
        elif e>=100:
            l1.append(a[1])
        elif e>=10:
            l1.append(a[2])
        elif e>=1:
            l1.append(a[3])
        else:
            l1.append(a[4])
    
    return l1