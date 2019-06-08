import math
import time
Fibo_even = [2]
start = time.time()

def fibo(x,z):
    loop = True
    while loop == True:
        y = int(((((1+math.sqrt(5))/2)**x)-(((1-math.sqrt(5))/2)**x))/math.sqrt(5))
        x += 1
        if y % 2 == 0:
            if y > z:
                loop = False
                break
            Fibo_even.append(y)

    for x in range(x,100):
            y = int(((((1+math.sqrt(5))/2)**x)-(((1-math.sqrt(5))/2)**x))/math.sqrt(5))
            if y % 2 == 0:
                if y > z:
                    break
                Fibo_even.append(y)
fibo(5,4000000)
print(sum(Fibo_even))
end = time.time()
print(end - start)