#n = 1

#for i in range(1,101):
    #print(str(i) + "\n")

for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz" + "\n")
    elif (i % 5 == 0):
        print("Buzz" + "\n")
    elif (i % 3 == 0):
        print("Fizz" + "\n")
    else:
        print(str(i) + "\n")



