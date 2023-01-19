f=open("pages.txt","r")
a=f.read().splitlines()
l=[]

for i in a:
    abc=i.split(":")
    l.append(abc)

URL=[]
init_imp=[]
URL_ext=[]

for i in range(len(l)):
    a=l[i][0].split(",")
    URL.append(a[0])
    init_imp.append(float(a[1]))

for i in range(len(l)):
    b=l[i][1]
    b=b.split()
    m=[]
    for i in b:
        if i[:5] in URL:
            m.append(i[:5])
            m.sort()
    alc=[]
    for i in m:
        if i not in alc:
            alc.append(i)
    URL_ext.append(alc)

importance={}

for i in range(len(URL)):
    dict1={}
    importance[URL[i]]=dict1
    dict1["Init Importance"]=init_imp[i]
    dict1["Importance"]=0.0
    dict1["Url"]=URL_ext[i]
#print(importance)
for k,v in importance.items():
    cal=v["Init Importance"]/len(v["Url"])
    for j in v["Url"]:
        importance[j]["Importance"]+=cal
#print(importance)
sort=sorted(importance.items(),key=lambda x:x[1]["Importance"],reverse=True)
n=int(input("How many pages do you want to print:"))
for i in range(n):
    print(sort[i][0],":",sort[i][1]["Importance"])

