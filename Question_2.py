#Question 2
l=[]
#Function to check course name
def courseno(n):
    ans=True
    if n[0].isalnum():
        for i in n[0]:
            if i.isdigit():
                index=n[0].index(i)
                if index==0:
                    ans=False
                    return ans
                elif n[0][index:].isalpha():
                    ans=False
                    return ans
            elif i.islower():
                ans=False
                return ans
            elif n[0][-1].isalpha():
                ans=False
                return ans
    return ans
n=["CSs12", "3", "B"]
#Take inputs and check for invalid inputs
while True:
    n=list(map(str,input("Enter course name, Credit and Grade: ").split())) #taking input in a list 
    a,b,c,d,e,f=0,0,0,0,0,0
    if len(n)==0:                    # if the input is empty list the loop breaks
        break
    elif len(n)>0 and len(n)<3:
        print("Invalid Input")
    elif len(n)==3:                  #conditions to check if the length of the list is 3
        if courseno(n)==False:
            print("Invalid Course Name")
        if n[1] in ['1','2','4']:           #check if the first index is a digit
            b+=1
        else:
            print("Invalid Credit")
        if n[2] in ["A+","A","A-","B","B-","C","C-","D","F"]:
            c+=1
        else:
            print("Invalid Grade")
        if courseno(n)==True and b>0 and c>0:
            l+=n
print("\nTranscript:")
course=[]
credit=[]
grade=[]

#creating seperate lists for grades and credits
for i in range(0,len(l),3):
    course.append(l[i])
for i in range(1,len(l),3):
    credit.append(int(l[i]))
for i in range(2,len(l),3):
    grade.append(l[i])

#creating dictionary for course and grade
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

#sort dictionary
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

#Calculating sgpa
sgpa=0
total_credits=sum(credit)
for i in range(len(credit)):
    sgpa+=credit[i]*new[i]/total_credits
print("\nSGPA:",round(sgpa,2))