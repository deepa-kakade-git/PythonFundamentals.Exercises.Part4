num = int(input("Enter a number"))

print("x(n) of your number is : " + str((num - 1) + (num - 2)))


    #result = fibonacci(num)
    #print("Fibonacci of " + str(num) + "is" + str(result))
def fibonacci(num):
    if (num==1):
        return  0
    elif num==2:
        return 1
    else:
        return (fibonacci(num-1) + fibonacci(num-2))


for i in range(1,31):
    print(fibonacci(i))
#print(num-2)

#def calculate_xn(num):
#   ex_of_en = (num - 1) + (num - 2)
#   print(ex_of_en)
