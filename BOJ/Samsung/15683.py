from itertools import product

N, M = map(int, input().split())
# M x N
camera = []
board = [list(map(int,input().split())) for _ in range(N)]
dir = (0, 1, 2, 3) # right, up, left, down
dx, dy = (1, 0, -1, 0), (0, 1, 0, -1)

for i in range(N):
    for j in range(M):
        if board[i][j] > 0 and board[i][j] != 6:
            tmp = []
            for d in dir:
                tmp.append((d,i,j))
            camera.append(tmp)

# print(camera)
ret = 987654321

for cameras in product(*camera):
    MAP = [[True] * M for _ in range(N)]
    for i in range(M):
        for j in range(N):
            if board[j][i] == 6:
                MAP[j][i] = False

    for cctv in cameras:

        case = board[cctv[1]][cctv[2]]
        MAP[cctv[1]][cctv[2]] = False
        x = cctv[2]
        y = cctv[1]

        nx = x
        ny = y
        if case == 1:
            while True:
                if ((0+cctv[0]) % 4) % 2 == 0:
                    nx = nx + dx[(0+cctv[0])%4]
                    if nx < 0 or nx >= M or board[ny][nx] == 6:
                        break

                else:
                    ny = ny + dy[(0+cctv[0])%4]
                    if ny < 0 or ny >= N or board[ny][nx] == 6:
                        break
                MAP[ny][nx] = False

        elif case == 2:
            while True:
                if ((0 + cctv[0]) % 4) % 2 == 0:
                    nx = nx + dx[(0 + cctv[0]) % 4]
                    if nx < 0 or nx >= M or board[ny][nx] == 6:
                        break

                else:
                    ny = ny + dy[(0 + cctv[0]) % 4]
                    if ny < 0 or ny >= N or board[ny][nx] == 6:
                        break

                MAP[ny][nx] = False

            nx = x
            ny = y
            while True:
                if ((2 + cctv[0]) % 4) % 2 == 0:
                    nx = nx + dx[(2 + cctv[0]) % 4]
                    if nx < 0 or nx >= M or board[ny][nx] == 6:
                        break

                else:
                    ny = ny + dy[(2 + cctv[0]) % 4]
                    if ny < 0 or ny >= N or board[ny][nx] == 6:
                        break
                MAP[ny][nx] = False

        elif case == 3:
            while True:
                if ((0 + cctv[0]) % 4) % 2 == 0:
                    nx = nx + dx[(0 + cctv[0]) % 4]
                    if nx < 0 or nx >= M or board[ny][nx] == 6:
                        break

                else:
                    ny = ny + dy[(0 + cctv[0]) % 4]
                    if ny < 0 or ny >= N or board[ny][nx] == 6:
                        break

                MAP[ny][nx] = False

            ny = y
            nx = x

            while True:
                if ((3 + cctv[0]) % 4) % 2 == 0:
                    nx = nx + dx[(3+cctv[0])%4]
                    if nx < 0 or nx >= M or board[ny][nx] == 6:
                        break
                else:
                    ny = ny + dy[(3+cctv[0])%4]
                    if ny < 0 or ny >= N or board[ny][nx] == 6:
                        break
                MAP[ny][nx] = False


        elif case == 4:
            while True:
                if ((0 + cctv[0]) % 4) % 2 == 0:
                    nx = nx + dx[(0 + cctv[0]) % 4]
                    if nx < 0 or nx >= M or board[ny][nx] == 6:
                        break

                else:
                    ny = ny + dy[(0 + cctv[0]) % 4]
                    if ny < 0 or ny >= N or board[ny][nx] == 6:
                        break

                MAP[ny][nx] = False

            ny = y
            nx = x

            while True:
                if ((3 + cctv[0]) % 4) % 2 == 0:
                    nx = nx + dx[(3 + cctv[0]) % 4]
                    if nx < 0 or nx >= M or board[ny][nx] == 6:
                        break

                else:
                    ny = ny + dy[(3 + cctv[0]) % 4]
                    if ny < 0 or ny >= N or board[ny][nx] == 6:
                        break
                MAP[ny][nx] = False


            ny = y
            nx = x

            while True:
                if ((2 + cctv[0]) % 4) % 2 == 0:
                    nx = nx + dx[(2 + cctv[0]) % 4]
                    if nx < 0 or nx >= M or board[ny][nx] == 6:
                        break
                else:
                    ny = ny + dy[(2 + cctv[0]) % 4]
                    if ny < 0 or ny >= N or board[ny][nx] == 6:
                        break

                MAP[ny][nx] = False


        else:
            while True:
                nx = nx + dx[0]
                if nx < 0 or nx >= M or board[y][nx] == 6:
                    break

                MAP[y][nx] = False

            while True:
                ny = ny + dy[3]
                if ny < 0 or ny >= N or board[ny][x] == 6:
                    break

                MAP[ny][x] = False

            nx = x
            while True:
                nx = nx + dx[2]
                if nx < 0 or nx >= M or board[y][nx] == 6:
                    break

                MAP[y][nx] = False

            ny = y
            while True:
                ny = ny + dy[1]
                if ny < 0 or ny >= N or board[ny][x] == 6:
                    break

                MAP[ny][x] = False

    ret = min(ret, sum(map(sum, MAP)))
print(ret)