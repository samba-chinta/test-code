def FindMinSubRectangle(mat):
    rows = len(mat)
    cols = len(mat[0])
 
    temp = []
    for i in range(rows):
        temp1 = []
        for j in range(cols):
            if i == 0 or j == 0:
                temp1 += mat[i][j],
            else:
                temp1 += 0,
        temp += temp1,

    for i in range(1, rows):
        for j in range(1, cols):
            if (mat[i][j] == 0):
                temp[i][j] = min(temp[i][j-1], temp[i-1][j],temp[i-1][j-1]) + 1
            else:
                temp[i][j] = 0

    val = temp[0][0]
    mini = 0
    minj = 0
    for i in range(rows):
        for j in range(cols):
            if (val < temp[i][j]):
                val = temp[i][j]
                mini = i
                minj = j
 
    return [tuple((mini-val,minj)),tuple((mini-val,minj+val)),tuple((mini,minj)),tuple((mini,minj+val))]
 
n=int(input())
mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))
 
result = FindMinSubRectangle(mat)

print(result[0],",",result[1],",",result[2],",",result[3])