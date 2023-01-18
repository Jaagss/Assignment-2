f=open("pages.txt","r")
a=f.read().splitlines()
l=[]

for i in a:
    abc=i.split(":")
    