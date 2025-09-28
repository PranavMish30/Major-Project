import random

from locations import vertices

n = len(vertices)
graph = [ [0] * n ] * n
for i in range(n):
    for j in range(n):
        weight = random.randint(-1,5)
        if weight == -1:
            weight = float('inf')

        graph[i][j] = weight



