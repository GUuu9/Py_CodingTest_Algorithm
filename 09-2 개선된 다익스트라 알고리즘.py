# 9-2 개선된 다익스트라 알고리즘
from multiprocessing import heap
import time
start_time = time.time()

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값을 설정(10억)

n, m = map(int, input().split())

start = int(input())

graph = [[] for i in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")

    else:
        print(distance[i])

end_time = time.time()
print("time : ", end_time - start_time)
