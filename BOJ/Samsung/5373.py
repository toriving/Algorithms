import copy

dic = {'U+': 1, 'D+': 2, 'F+':3, 'B+':4, 'L+':5, 'R+':6, 'U-': -1, 'D-': -2, 'F-':-3, 'B-':-4, 'L-':-5, 'R-':-6 }

def rotation(space, dir):
    if dir == 1:
        rotated = copy.deepcopy(list(map(list,zip(*reversed(space)))))
    else:
        rotated = copy.deepcopy(space)
        for _ in range(3):
            rotated = list(map(list,zip(*reversed(rotated))))

    return rotated

t = int(input())
for _ in range(t):
    n = int(input())
    dir = list(dic[x] for x in input().split())
    # 윗, 아, 앞, 뒷, 왼, 오
    cube = [[['w', 'w', 'w'],
             ['w', 'w', 'w'],
             ['w', 'w', 'w']],
            [['y', 'y', 'y'],
             ['y', 'y', 'y'],
             ['y', 'y', 'y']],
            [['r', 'r', 'r'],
             ['r', 'r', 'r'],
             ['r', 'r', 'r']],
            [['o', 'o', 'o'],
             ['o', 'o', 'o'],
             ['o', 'o', 'o']],
            [['g', 'g', 'g'],
             ['g', 'g', 'g'],
             ['g', 'g', 'g']],
            [['b', 'b', 'b'],
             ['b', 'b', 'b'],
             ['b', 'b', 'b']]]


    for d in dir:
        tmp = copy.deepcopy(cube)
        if d == 1:
            tmp[0] = rotation(cube[0], 1)
            tmp[2][0] = cube[5][0]
            tmp[4][0] = cube[2][0]
            tmp[3][0] = cube[4][0]
            tmp[5][0] = cube[3][0]
        elif d == -1:
            tmp[0] = rotation(cube[0], -1)
            tmp[2][0] = cube[4][0]
            tmp[4][0] = cube[3][0]
            tmp[3][0] = cube[5][0]
            tmp[5][0] = cube[2][0]
        elif d == 2:
            tmp[1] = rotation(cube[1], 1)
            tmp[2][2] = cube[4][2]
            tmp[4][2] = cube[3][2]
            tmp[3][2] = cube[5][2]
            tmp[5][2] = cube[2][2]
        elif d == -2:
            tmp[1] = rotation(cube[1], -1)
            tmp[2][2] = cube[5][2]
            tmp[4][2] = cube[2][2]
            tmp[3][2] = cube[4][2]
            tmp[5][2] = cube[3][2]

        elif d == 3: # 윗, 아, 앞, 뒷, 왼, 오
            tmp[2] = rotation(cube[2], 1)
            tmp[0][2][0] = cube[4][2][2]
            tmp[0][2][1] = cube[4][1][2]
            tmp[0][2][2] = cube[4][0][2]

            tmp[4][0][2] = cube[1][0][0]
            tmp[4][1][2] = cube[1][0][1]
            tmp[4][2][2] = cube[1][0][2]

            tmp[1][0][0] = cube[5][2][0]
            tmp[1][0][1] = cube[5][1][0]
            tmp[1][0][2] = cube[5][0][0]

            tmp[5][0][0] = cube[0][2][0]
            tmp[5][1][0] = cube[0][2][1]
            tmp[5][2][0] = cube[0][2][2]

        elif d == -3:
            tmp[2] = rotation(cube[2], -1)
            tmp[0][2][0] = cube[5][0][0]
            tmp[0][2][1] = cube[5][1][0]
            tmp[0][2][2] = cube[5][2][0]

            tmp[5][0][0] = cube[1][0][2]
            tmp[5][1][0] = cube[1][0][1]
            tmp[5][2][0] = cube[1][0][0]

            tmp[1][0][0] = cube[4][0][2]
            tmp[1][0][1] = cube[4][1][2]
            tmp[1][0][2] = cube[4][2][2]

            tmp[4][0][2] = cube[0][2][2]
            tmp[4][1][2] = cube[0][2][1]
            tmp[4][2][2] = cube[0][2][0]

        elif d == 4:
            tmp[3] = rotation(cube[3], 1)
            tmp[0][0][0] = cube[5][0][2]
            tmp[0][0][1] = cube[5][1][2]
            tmp[0][0][2] = cube[5][2][2]

            tmp[5][0][2] = cube[1][2][2]
            tmp[5][1][2] = cube[1][2][1]
            tmp[5][2][2] = cube[1][2][0]

            tmp[1][2][0] = cube[4][0][0]
            tmp[1][2][1] = cube[4][1][0]
            tmp[1][2][2] = cube[4][2][0]

            tmp[4][0][0] = cube[0][0][2]
            tmp[4][1][0] = cube[0][0][1]
            tmp[4][2][0] = cube[0][0][0]

        elif d == -4:
            tmp[3] = rotation(cube[3], -1)
            tmp[0][0][2] = cube[4][2][0]
            tmp[0][0][1] = cube[4][1][0]
            tmp[0][0][0] = cube[4][0][0]

            tmp[4][0][0] = cube[1][2][0]
            tmp[4][1][0] = cube[1][2][1]
            tmp[4][2][0] = cube[1][2][2]

            tmp[1][2][0] = cube[5][0][2]
            tmp[1][2][1] = cube[5][1][2]
            tmp[1][2][2] = cube[5][2][2]

            tmp[5][0][2] = cube[0][0][0]
            tmp[5][1][2] = cube[0][0][1]
            tmp[5][2][2] = cube[0][0][2]

        elif d == 5: # 윗, 아, 앞, 뒷, 왼, 오
            tmp[4] = rotation(cube[4], 1)
            tmp[0][0][0] = cube[3][2][0]
            tmp[0][1][0] = cube[3][1][0]
            tmp[0][2][0] = cube[3][0][0]

            tmp[3][0][0] = cube[1][0][0]
            tmp[3][1][0] = cube[1][1][0]
            tmp[3][2][0] = cube[1][2][0]

            tmp[1][0][0] = cube[2][2][0]
            tmp[1][1][0] = cube[2][1][0]
            tmp[1][2][0] = cube[2][0][0]

            tmp[2][0][0] = cube[0][0][0]
            tmp[2][1][0] = cube[0][1][0]
            tmp[2][2][0] = cube[0][2][0]

        elif d == -5:
            tmp[4] = rotation(cube[4], -1)
            tmp[0][0][0] = cube[2][0][0]
            tmp[0][1][0] = cube[2][1][0]
            tmp[0][2][0] = cube[2][2][0]

            tmp[2][0][0] = cube[1][2][0]
            tmp[2][1][0] = cube[1][1][0]
            tmp[2][2][0] = cube[1][0][0]

            tmp[1][0][0] = cube[3][0][0]
            tmp[1][1][0] = cube[3][1][0]
            tmp[1][2][0] = cube[3][2][0]

            tmp[3][0][0] = cube[0][2][0]
            tmp[3][1][0] = cube[0][1][0]
            tmp[3][2][0] = cube[0][0][0]

        elif d == 6:# 윗, 아, 앞, 뒷, 왼, 오
            tmp[5] = rotation(cube[5], 1)
            tmp[0][0][2] = cube[2][0][2]
            tmp[0][1][2] = cube[2][1][2]
            tmp[0][2][2] = cube[2][2][2]

            tmp[2][0][2] = cube[1][2][2]
            tmp[2][1][2] = cube[1][1][2]
            tmp[2][2][2] = cube[1][0][2]

            tmp[1][0][2] = cube[3][0][2]
            tmp[1][1][2] = cube[3][1][2]
            tmp[1][2][2] = cube[3][2][2]

            tmp[3][0][2] = cube[0][2][2]
            tmp[3][1][2] = cube[0][1][2]
            tmp[3][2][2] = cube[0][0][2]

        elif d == -6:
            tmp[5] = rotation(cube[5], -1)
            tmp[0][0][2] = cube[3][2][2]
            tmp[0][1][2] = cube[3][1][2]
            tmp[0][2][2] = cube[3][0][2]

            tmp[3][0][2] = cube[1][0][2]
            tmp[3][1][2] = cube[1][1][2]
            tmp[3][2][2] = cube[1][2][2]

            tmp[1][0][2] = cube[2][2][2]
            tmp[1][1][2] = cube[2][1][2]
            tmp[1][2][2] = cube[2][0][2]

            tmp[2][0][2] = cube[0][0][2]
            tmp[2][1][2] = cube[0][1][2]
            tmp[2][2][2] = cube[0][2][2]
        print(tmp)
        cube = copy.deepcopy(tmp)
    for x in cube[0]:
        print(''.join(x))
