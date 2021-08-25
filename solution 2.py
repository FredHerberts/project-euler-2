import time
start = time.time()
def fibo(n):
    a, b, even_fibonacci_sum = 2, 1, 2
    for x in range(1, n):
        a, b = a + b, a
        if a % 2 == 0:
            if a > 4000000:
                return even_fibonacci_sum
            even_fibonacci_sum += a

result = fibo(100)
end = time.time()
print(end - start)
print(result)
