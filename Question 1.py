menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
j=1

#print menu
for i in menu:
  print(j,i)
  j+=1
print()
l=[]

#Take order
while True:
    n=list(map(int,input("Enter item.no and quantity: ").split()))
    if len(n)!=2:
        break
    else:
        l+=n

total=0
n=0

#Printing bill
for i in range(0,len(l),2):
    print(menu[l[i]-1][0]+",",str(l[i+1])+",","Rs",menu[l[i]-1][1]*l[i+1])
    n+=l[i+1]
    total+=menu[l[i]-1][1]*l[i+1]
print()
print("TOTAL"+",",n,"items"+",","Rs",total)
