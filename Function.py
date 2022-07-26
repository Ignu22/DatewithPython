def add(*args):
    sum=0
    args = list(args)
    args[0]=22
    for i in args:
        sum +=i
    return sum
    
print(add(1,2,3,4,5,6))