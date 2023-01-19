with open("Yearbook.txt","r") as f:
    yearbook={}
    a=f.read().splitlines()
    for i in a:
        for j in i:
            if j==":":
                i=i[:-1]
                sign={}
                yearbook[i]=sign
            elif j==",":
                s=i.split(",")
                sign[s[0]]=int(s[1])

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