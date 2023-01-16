import random as r
import requests

word_list=["abuse","adult","agent","anger","input","sting","print","beach","birth","block","wrong","board","brain","bread","break","brown","buyer",
"cause","chain","chair","chest","chief","child","china","claim","cable","space","brave","coast","court","cover","cream","crime","quick","crowd","crown",
"crows","dance","death","depth","doubt","draft","marks","dream","grade","drink","drive","earth","saved","entry","faith","cloth","towel","clots","sharp","slice",
"stone","space","solid","extra","eight","gable","habit","hacks","table","vague"]
a=r.randint(0,len(word_list))

count=1
letters_wrong_pos=[]
letters_corret_pos=[]

def api_check(text):
    app_id  = "8d5a695c"
    app_key  = "c0dd9e7c9c423d19a643d406949bd59c"
    endpoint = "entries"
    language_code = "en-us"
    word_id = text
    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
    r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
    if word_id in r.text:
        return True 
    else:
        return False

while count<7:
    s="-----"
    print("Attempt",count)

    n=input("Enter a 5 character string: ")
    if api_check(n)==False:
        print("Invalid input\n")

    elif len(n)!=5:
        print("Invalid input\n")

    else:
        count+=1
        for i in range(5):
            if n[i]==word_list[a][i]:
                s=list(s)
                s.insert(i,n[i])
                s="".join(s)
                letters_corret_pos.append(i)
            elif n[i] in word_list[a]:
                letters_wrong_pos.append(n[i])
        if s[:5]==word_list[a]:
            print("The letters in correct position: \n"+s[:5],"\n")
            print("Well played! \nYou guessed the right word")
            break
        else:
            print("The letters in correct position: \n"+s[:5],"\n")
            print("Letters in the word: \n"+"".join(letters_wrong_pos),"\n")