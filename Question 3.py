f=open("Question 3.txt","r")
n=int(input())
yearbook={}
for i in range(n*2-1):
    a=f.readline()
    if a=="\n":
        pass
    else:
        a=a.split(":")
        d=a[0]
        sign={}
        yearbook[d]=sign
        for i in range(n-1):
            b=f.readline()
            for i in b:
                if i in ["0","1"]:
                    c=int(i)
            b=b.split(",")
            e=b[0]
            sign[e]=c
f.close()
max_={}
for key,value in yearbook.items():
    count_1=0
    for i,j in value.items():
        if j==1:
            count_1+=1
    max_[key]=count_1
m=max(max_.values())
name=[k for k,v in max_.items() if v==m]
print(*name,sep=" ")