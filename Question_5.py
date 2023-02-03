
cx=int(input("Enter cx: "))
cy=int(input("Enter cy: "))

def coordinates():
    l1 = []
    while True:
        user_input = list(map(int,input('Enter x and y coordinates : ').split()))
        if not(len(user_input)==2):
            break
        else:
            #making the coordinates in the form of a tuple
            inputs = tuple(user_input)
            #appneding those coordinates in a list
            l1.append(inputs)
    return l1
matrix=[[cx,0,0],[0,cy,0],[0,0,1]]
result = [[sum(i*j for i,j in zip(X_row,Y_col)) for Y_col in zip(*matrix)] for X_row in coordinates()]
print()
for r in result:
    for i in range(len(r)-1):
        print(r[i],end=" ")
    print()
