dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N * N + 1)

    # 현재 위치 숫자 기준 상하좌우 확인
    #   -> 1 큰 곳이 있다면 visited 기록
    for y in range(N):
        for x in range(N):
            for i in range(4):  # 상하좌우 확인
                new_y = y + dy[i]
                new_x = x + dx[i]

                # 델타는 범위 밖을 잘 체크해주어야 한다!!!
                if new_y < 0 or new_y >= N or new_x < 0 or new_x >= N:
                    continue

                if arr[new_y][new_x] == arr[y][x] + 1:
                    # 현재 숫자는 다음으로 이동이 가능하다
                    visited[arr[y][x]] = 1
                    break   # 나머지 방향은 볼 필요 없다.

    # 연속된 1의 개수가 가장 긴 곳을 찾는다.
    # 가장 긴 길이, 현재 몇 개인지, 출발지
    max_cnt = cnt = start = 0
    for i in range(1, N * N + 1):
        if visited[i] == 1:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
                start = i - cnt
            cnt = 0     # 개수 초기화

    print(f'#{tc} {start} {max_cnt + 1}')

