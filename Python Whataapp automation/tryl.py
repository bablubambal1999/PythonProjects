x  = [1,2,3,4,2,3,4]
y =[]
def uniquelist(x):
    for i in x:
        if x[i] in y:
            continue
        y.append()
    return y
    
print(uniquelist(x))