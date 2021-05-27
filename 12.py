#program to add and multiply two 3*3 matrices
a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
b=[[7,8,9],
   [1,2,3],
   [4,5,6]]
result= [[0,0,0],
         [0,0,0],
         [0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        result[i][j]= a[i][j]*b[i][j]
for r in result:
    print(r)

