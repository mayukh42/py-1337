from adt.mat import Mat
from adt.item import DPTCell

def test_mat():
    yxs = [
        [0, 1, 2, 3],
        [4, 5, 6, 7], 
        [8, 9, 10, 11]
    ]
    mat = Mat(len(yxs), len(yxs[0]), DPTCell(0, []))
    print(mat)

    for i in range(len(yxs)):
        for j in range(len(yxs[i])):
            mat.set(i, j, yxs[i][j])
    print(mat)

    print(mat.get(1, 2))


if __name__ == '__main__':
    test_mat()
