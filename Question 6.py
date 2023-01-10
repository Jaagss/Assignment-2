wts = [(10, 5), (20, 5), (100, 15), (40, 10), (30,10), (10,5), (100,40), (40,10)]
wts_new=[]
for i in wts:
    b=round(i[0]/i[1],2)
    wts_new.append(b)

f=open("IPmarks.txt","r")
a=f.read()
print(a)
f.close()
l=[]
s=[]
f=open("IPgrades.txt","w")

for i in a:
    s=a.split("\n")
for i in s:
    i=i.split(",")
    l.append(i)
for i in l:
    for j in range(len(i)):
        i[j]=int(i[j])
for i in l:
    total_marks=0
    for j in range(len(i)):
        if j==0:
            pass
        elif j!=0:
            total_marks+=i[j]/wts_new[j-1]
    print(total_marks)
    if total_marks>=80:
        grade="A"
    elif total_marks>=70:
        grade="A-"
    elif total_marks>=60:
        grade="B"
    elif total_marks>=50:
        grade="B-"
    elif total_marks>=40:
        grade="C"
    elif total_marks>=35:
        grade="C-"
    elif total_marks>=30:
        grade="D"
    elif total_marks<30:
        grade="F"
    ans=str(i[0])+","+str(round(total_marks,2))+","+grade
    f.write(ans)
    f.write("\n")
f.close()