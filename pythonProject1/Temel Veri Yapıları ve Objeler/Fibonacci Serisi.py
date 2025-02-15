
a = 1
b = 1

Fibonacci = [a,b]
for i in range(20):
    a,b = b,a+b
    Fibonacci.append(b)
print(Fibonacci)





