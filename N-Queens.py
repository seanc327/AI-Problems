def queen(n):
    # create chessboard
    board = [["."]*n for _ in range(n)]

    # determining whether queen can be placed or not
    def valid(i, j):
        # row/column check
        for k in range(n):
            if board[k][j] == u"\u2655" or board[i][k] == u"\u2655":
                return True
        # diagonal check
        for k in range(n):
            for l in range(n):
                if k-l == i-j or k+l == i+j:
                    if board[k][l] == u"\u2655":
                        return True
        return False

    # steps
    boards = []
    def placement(row):
        if row == n:
            boards.append([row.copy() for row in board])
            return True

        for col in range(n):
            if board[row][col] != u"\u2655" and not valid(row, col):
                board[row][col] = u"\u2655"
                boards.append([row.copy() for row in board])
                if placement(row + 1):
                    return True
                board[row][col] = "."
        return False
    placement(0)
    for step in boards[:-2]:
        for row in step:
            print(*row)
        # print space
        print()

    for row in boards[-2]:
        print(*row)
    print()

queen(4)
