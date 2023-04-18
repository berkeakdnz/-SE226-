n = int(input("Enter a value to n "))
x = int(input("Enter a value to x "))

factorial = lambda n: 1 if n <= 1 else n * factorial(n-1)

result = sum([n**a/factorial(a) for a in range(x+1)])

print(result)