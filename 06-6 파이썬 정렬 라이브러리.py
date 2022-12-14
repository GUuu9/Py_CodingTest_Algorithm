# 6-6 파이썬의 정렬 라이브러리
import time
start_time = time.time()


# sorted
array1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

result = sorted(array1)
print(result)

# sort
array2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

array2.sort()
print(array2)

# key use
array3 = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array3, key = setting)
print(result)

end_time = time.time()
print("time : ", end_time - start_time)
