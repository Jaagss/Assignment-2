f=open("pages.txt","r")
a=f.read().splitlines()
URL=[]
l=[]
for i in a:
    abc=i.split(":")
    l.append(abc)
URL=[]
init_imp=[]
URL_txt=[]
for i in range(len(l)):
    split_=l[i][0].split(",")
    URL.append(split_[0])
    init_imp.append(float(split_[1]))

for i in range(len(l)):
    split_=l[i][1].split()
    a=[]

    for i in split_:
        i=i.strip(",")
        if i in URL:
            a.append(i)
    URL_txt.append(a)
importance={}
for i in range(len(URL)):
    dict1={}
    importance[URL[i]]=dict1
    dict1["init importance"]=init_imp[i]
    dict1["Importance"]=0.0
    dict1["Url"]=URL_txt[i]
for k,v in importance.items():
    cal=v["init importance"]/len(v["Url"])
    for j in v["Url"]:
        importance[j]["Importance"]+=cal

sort=sorted(importance.items(),key=lambda x: x[1]["Importance"],reverse=True)

for i in sort:
    print(i[0],":",i[1]["Importance"])