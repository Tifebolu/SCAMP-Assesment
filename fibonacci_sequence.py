def fibonacci(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        c =  a + b
        print (c)
        a = b
        b = c

        count += 1
    return (c)


n = int(input('Enter a number: '))
print(fibonacci(n))
