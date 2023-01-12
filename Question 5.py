n=int(input())
l=[]
for i in range(n):
    l1=list(map(int,input().split()))
    l1+=[1]
    l.append(l1)
cx=int(input("Enter cx: "))
cy=int(input("Enter cy: "))
matrix=[[cx,0,0],[0,cy,0],[0,0,1]]
print("B: ",l)
result = [[sum(i*j for i,j in zip(X_row,Y_col)) for Y_col in zip(*matrix)] for X_row in l]

for r in result:
    for i in range(len(r)-1):
        print(r[i],end=" ")
    print()
