class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                live = 0

                # Check all 8 neighbors
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue

                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < rows and 0 <= nc < cols:
                            if board[nr][nc] in (1, 2):
                                live += 1

                # 1 -> currently alive, becomes dead
                if board[r][c] == 1 and (live < 2 or live > 3):
                    board[r][c] = 2

                # 0 -> currently dead, becomes alive
                elif board[r][c] == 0 and live == 3:
                    board[r][c] = 3

        # Convert temporary states to final states
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1