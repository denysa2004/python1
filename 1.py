#seminar 5 ,pb 3

def func(matrix):
    i=0
    while i<len(matrix):
        if i % 2 == 0:
            for j in range(len(matrix[i])-1):
                if matrix[i][j] >= matrix[i][j + 1]:
                    return 0
            if i<len(matrix)-2:
                if matrix[i][len(matrix) - 1] > matrix[i + 1][len(matrix) - 1]:
                    return 0

            i=i+1

        else:
            for j in range(len(matrix[i])-1, 1, -1):
                if matrix[i][j] >= matrix[i][j-1]:
                    return 0
            if i<=len(matrix)-2:
                if matrix[i][0] > matrix[i+1][0]:
                    return 0
            i=i+1

    return 1

def test():
    assert func([
        [1, 2, 3],
        [6, 5, 4],
        [7, 8, 9]
    ]) == 1

test()


