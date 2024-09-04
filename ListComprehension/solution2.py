#using list comprehension

    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    list = []
    for n1 in range(x+1):
        for n2 in range(y+1):
            for n3 in range(z+1):
                if n1+n2+n3 != n:
                    list.append([n1,n2,n3])
    print(list)
