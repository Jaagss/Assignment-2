n=int(input())
l=[]
for i in range(n):
    l1=list(map(int,input().split()))
    l1+=[1]
    l.append(l1)
cx=int(input())
cy=int(input())
matrix=[[cx,0,0],[0,cy,0],[0,0,1]]

result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*matrix)] for X_row in l]

for r in result:
   print(r)