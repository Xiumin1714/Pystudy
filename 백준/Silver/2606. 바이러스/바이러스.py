from collections import deque

n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] 
visited=[0]*(n+1)

for i in range(v):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]    # 양방향
    
visited[1]=1 
q=deque([1])

while q:
    c=q.popleft()
    for nx in graph[c]:
        if visited[nx]==0:
            q.append(nx)
            visited[nx]=1
            
print(sum(visited)-1)