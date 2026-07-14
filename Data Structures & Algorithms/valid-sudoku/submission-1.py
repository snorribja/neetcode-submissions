class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x_d = dict()
        y_d = dict()
        s_d = dict()
        
        for i_ind, i in enumerate(board):
            for j_ind, j in enumerate(i):
                if j == ".":
                    continue
                if i_ind not in x_d:
                    x_d[i_ind] = [j]
                elif j in x_d[i_ind]:
                    return False
                else:
                    x_d[i_ind].append(j)

                if j_ind not in y_d:
                    y_d[j_ind] = [j]
                elif j in y_d[j_ind]:
                    return False
                else:
                    y_d[j_ind].append(j)
                
                ti_ind = i_ind // 3
                tj_ind = j_ind // 3
                if (ti_ind, tj_ind) not in s_d:
                    s_d[(ti_ind, tj_ind)] = [j]
                elif j in s_d[(ti_ind, tj_ind)]:
                    return False
                else:
                    s_d[(ti_ind, tj_ind)].append(j)

        return True

