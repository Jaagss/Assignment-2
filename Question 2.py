#Question 2
l=[]
def courseno(n):
    ans=True
    for i in n[0]:
        if i.isalnum():
            if i.isdigit():
                index=n[0].index(i)
                if index==0:
                    ans=False
                    return ans
                if n[0][index:].isalpha():
                    ans=False
                    return ans
            elif i.isalpha() and i.isupper():
                ans=True
            elif i.islower():
                ans=False
                return ans
                
    return ans


while True:
    n=list(map(str,input().split())) #taking input in a list 
    a,b,c,d,e,f=0,0,0,0,0,0
    if len(n)==0:                    # if the input is empty list the loop breaks
        break
    elif len(n)>0 and len(n)<3:
        print("Incorrect input")
    elif len(n)==3:                  #conditions to check if the length of the list is 3
        if courseno(n)==False:
            print("Imporper course no")
        if n[1] in ['1','2','4']:           #check if the first index is a digit
            b+=1
        else:
            print("Incorrect credit")
        if n[2] in ["A+","A","A-","B","B-","C","C-","D","F"]:
            c+=1
        else:
            print("Incorrect grade")
        if courseno(n)==True and b>0 and c>0:
            l+=n

course=[]
credit=[]
grade=[]

for i in range(0,len(l),3):
    course.append(l[i])
for i in range(1,len(l),3):
    credit.append(int(l[i]))
for i in range(2,len(l),3):
    grade.append(l[i])

ngrade=grade[:]
course_grade={}
for key in course:
    for value in ngrade:
        course_grade[key]=value
        ngrade.remove(value)
        break

keys=list(course_grade.keys())
keys.sort()
sorteddict={i:course_grade[i] for i in keys}

for x in sorteddict:
    print(x,":",sorteddict[x])

new=[]
for j in grade:
    if j=="A+":
        new.append(10)
    if j=="A":
        new.append(10)
    if j=="A-":
        new.append(9)
    if j=="B":
        new.append(8)
    if j=="B-":
        new.append(7)
    if j=="C":
        new.append(6)
    if j=="C-":
        new.append(5)
    if j=="D":
        new.append(4)
    if j=="F":
        new.append(2)

sgpa=0
total_credits=0
for i in credit:
    total_credits+=int(i)
for i in range(len(credit)):
    sgpa+=credit[i]*new[i]/total_credits
print()
print("SGPA:",round(sgpa,2))