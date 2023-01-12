import random as r
word_list=["abuse","adult","agent","anger","apple","award","basis","beach","birth","block","blood","board","brain","bread","break","brown","buyer","cause","chain","chair","chest","chief","child","china","claim","class","clock","coach","coast","court","cover","cream","crime","cross","crowd","crown","cycle","dance","death","depth","doubt","draft","drama","dream","dress","drink","drive","earth","enemy","entry"]
a=r.randint(0,len(word_list))
print(word_list[a])
count=1
letters_wrong_pos=[]
letters_corret_pos=[]
while count<8:
    s="-----"
    print("Attempt",count)

    n=input("Enter a 5 character string: ")

    if len(n)!=5:
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