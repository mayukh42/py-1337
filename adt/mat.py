
class Mat(object):
    ''' ADT for 2D matrix
    '''
    def __init__(self, r, c, o):
        self.r = r
        self.c = c

        mat = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(o)
            mat.append(row)
        self.mat = mat
    
    def __str__(self) -> str:
        s = "\n"
        for i in range(self.r):
            for j in range(self.c):
                s += f"{self.get(i, j)} "
            s += "\n"
        s += "\n"
        return s

    def get(self, r, c):
        return self.mat[r][c]
    
    def set(self, r, c, o):
        e = self.get(r, c)
        self.mat[r][c] = o
        return e
