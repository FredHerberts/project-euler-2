import math
import time
Fibo_even = [2]
start = time.time()
def fibo(x,z):
    for x in range(x,100,3):
            y = int(((((1+math.sqrt(5))/2)**x)-(((1-math.sqrt(5))/2)**x))/math.sqrt(5))
            if y > z:
                break
            Fibo_even.append(y)
fibo(6,4000000)
print(sum(Fibo_even))
end = time.time()
print(end - start)
