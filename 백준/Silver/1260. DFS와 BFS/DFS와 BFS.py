def bfs(V, N):
    visited = [0]*(N+1)
    q = []
    q.append(V)
    visited[V] = 1
    ans = []

    while q:
        t = q.pop(0)
        ans.append(t)
        for w in adj_list[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
    return ans


def dfs(V, N):
    visited = [0]*(N+1)
    stack = []
    ans = []

    while True:
        if visited[V] == 0:
            visited[V] = 1
            ans.append(V)
        for w in adj_list[V]:
            if visited[w] == 0:
                stack.append(V)
                V = w
                break
        else:
            if stack:
                V = stack.pop()
            else:
                break
    return ans

N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N+1)]

for i in range(M):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

for lst in adj_list:
    lst.sort()

print(*dfs(V, N))
print(*bfs(V, N))