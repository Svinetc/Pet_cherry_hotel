n = int(input())
m = [list(map(int,input().split())) for i in range(n)]

for i in range(n):
    row_total = 0
    count = 0
    for j in range(n):
        if i == j and n- i -1 == n-j-1:
            m[i][j]
        average = row_total//n

    print(average,end=' ')
