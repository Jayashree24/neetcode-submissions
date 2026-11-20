class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rr = [set() for _ in range(9)]
        cc = [set() for _ in range(9)]
        tt = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                n = board[r][c]
                if n == '.':
                    continue
                if n not in rr[r]:
                    rr[r].add(n)
                else:
                    return False
                if n not in cc[c]:
                    cc[c].add(n)
                else:
                    return False
                sq = ( r // 3) * 3 + (c //3)
                if n not in tt[sq]:
                    tt[sq].add(n)
                else:
                    return False
        return True


            