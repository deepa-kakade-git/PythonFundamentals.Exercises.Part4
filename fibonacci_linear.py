def fibonacci(num):
    if (num==1):
        return  0
    elif num==2:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, num+1):
            c = a + b
            a = b
            b = c
        return c

#num = 5
for i in range(1,31):
    print(fibonacci(i))