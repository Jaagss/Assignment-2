f=open("Question 3.txt","r")
n=int(input("The number of students: "))
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
mi=min(max_.values())
name=[k for k,v in max_.items() if v==m]
minimum=[k for k,v in max_.items() if v==mi]
print("The students with maximum signatures: ",*name,sep=" ")
print("The students with minimum signatures: ",*minimum,sep=" ")