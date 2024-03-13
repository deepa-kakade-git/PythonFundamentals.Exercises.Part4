def factorial():
    x = int(input("Enter a number : "))
    product = 1


    for i in range(1 , x+1):
        product *=i
    return product

def main():
    result = factorial()
    print("Factorial :" + str(result))

main()