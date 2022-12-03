# 8-2 피보나치(재귀)
import time
start_time = time.time()

d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))

end_time = time.time()
print("time : ", end_time - start_time)
