# 7-5 부품 찾기(이진 탐색)
import time
start_time = time.time()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return min
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')



end_time = time.time()
print("time : ", end_time - start_time)
