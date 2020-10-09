t = int(input())
while t > 0:
    t -= 1
    k = int(input())
    board = ['X' for i in range(64)]
    board[0] = 'O'
    for i in range(k-1):
        board[i+1] = '.'

    for i in range(8):
        for j in range(8):
            print(board[j+8*i], end ='')
        print()

