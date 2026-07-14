class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        return self.check_verti(board) & self.check_hor(board) & self.check_box(board)


    def check_verti(self, board):
        for x in range(9):
            c_d = set()
            for line in board:
                i = line[x]
                if line[x] != '.':
                    if i in c_d:
                        return False
                    c_d.add(i)
        return True


    def check_hor(self, board):
        for line in board:
            c_d = set()
            for i in line:
                if i != '.':
                    if i in c_d:
                        return False
                    c_d.add(i)
        return True

    def check_box(self, board):
        size = 3

        f = board[:size]
        s = board[size:2*size]
        t = board[2*size:]
        
        return self.check_hor(self.extracter(f)) & self.check_hor(self.extracter(s)) & self.check_hor(self.extracter(t))

    def extracter(self, lines):
        f = list()
        s = list()
        t = list()
        size = 3

        for line in lines: 
            f.append(line[:size])
            s.append(line[size:2*size])
            t.append(line[2*size:])
        
        f = [item for sublist in f for item in sublist]
        s = [item for sublist in s for item in sublist]
        t = [item for sublist in t for item in sublist]

        return f, s, t
