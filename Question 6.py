wts = [(10, 5), (20, 5), (100, 15), (40, 10), (30,10), (10,5), (100,40), (40,10)]
f=open("Question 6.txt","r")
a=f.read()
l=[]
s=[]
for i in a:
    s=a.split("\n")
for i in s:
    i=i.split(",")
    l.append(i)
for i in l:
    for j in range(len(i)):
        i[j]=int(i[j])
total_marks=0