#Fibonacci Series
#The Fibonacci Series is when two number add up to the next one.  e.g 0,1,1,2,3,5,8,13,21 .......

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci (n - 1) + fibonacci (n - 2)



terms = int(input("How many terms?: "))
for i in range (terms):
    print(fibonacci(i), end = " ")