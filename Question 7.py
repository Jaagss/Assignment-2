import ast
phone_book={}


def read():
    f=open("addrbook.txt","r+")
    phone_book=ast.literal_eval(f.read())
    f.close()
    return phone_book

def write(phone_book):
    f=open("addrbook.txt","w")
    f.write(str(phone_book))
    f.close()

def insert(phone_book):
    name=input("Enter name: ")
    dict1={}
    temp_dict = {}
    address=input("Enter address: ")
    phone=int(input("Enter phone number: "))
    email=input("Enter email id: ")
    temp_dict['address'] = address
    temp_dict['phone'] = phone
    temp_dict['email'] = email
    l = []
    l.append(temp_dict)
    dict1[name] = l
    if phone_book == {}:
        phone_book = dict1
    else:
        add_list = []
        for k,v in phone_book.items():
            if k==name:
                add_list.append(v)
                add_list.append(dict1[name])
            if(len(add_list)==0):
                phone_book = dict1
            else:
                phone_book[k] = add_list
    return phone_book

def delete(phone_book):
    del_entry=input("Enter entry to be deleted: ")
    del phone_book[del_entry]
    return phone_book

def find_name(phone_book):
    name_find=input("Enter name to search: ")
    for keys,values in phone_book.items():
        if name_find in keys:
            print(keys,values)

def find_phone(phone_book):
    phone=int(input("Enter phone number to search: "))
    for key,value in phone_book.items():
        for x in value:
            if len(value)>1:
                for y in x:
                    for i,j in y.items():
                        if j == phone:
                            return key,y
            else:
                for i,j in x.items():
                    if j == phone:
                        return key,phone_book[key]

f = open("addrbook.txt")
if(len(f.read().splitlines())==0):
    phone_book = {}
    pass
else:
    phone_book = read()
f.close()
while True:
    choice=int(input("1 : Inserting new entry: \n2 : Deleting an entry: \n3 : Find all entries from name \n4 : Find the entry with phone number \n5 : Exit\n\nPlease enter your choice: "))
    if choice==1:
        new_phone_book=insert(phone_book)
        phone_book={**phone_book,**new_phone_book}
        print(phone_book)
        print()
    elif choice==2:
        new_phone_book=delete(phone_book)
        phone_book={**phone_book,**new_phone_book}
        print()
    elif choice==3:
        print()
        find_name(phone_book)
        print()
    elif choice==4:
        print()
        key,value = find_phone(phone_book)
        print(key,value)
        print()
    elif choice==5:
        write(phone_book)
        break