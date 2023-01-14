import ast
phone_book={}
def read():
    f=open("addrbook.txt","r")
    phone_book=ast.literal_eval(f.read())
    f.close()
    return phone_book

def write():
    f=open("addrbook.txt","w")
    s=str(phone_book)
    f.write(s)
    f.close()

def insert():
    phone_book=read()
    name=input("Enter name: ")
    dict={}
    phone_book[name]=dict
    address=input("Enter address: ")
    phone=int(input("Enter phone number: "))
    email=input("Enter email id: ")
    dict["address"]=address
    dict["phone"]=phone
    dict["email"]=email
    return phone_book

def delete():
    phone_book=read()
    del_entry=input("Enter entry to be deleted: ")
    del phone_book[del_entry]
    return phone_book

def find_name():
    phone_book=read()
    name_find=input("Enter name to search: ")
    return phone_book[name_find]

def find_phone():
    phone_book=read()
    phone=int(input("Enter phone number to search: "))
    res=[val[phone] for key,val in phone_book.items() if phone in val]
    return res

while True:
    choice=int(input("1 : Inserting new entry: \n2 : Deleting an entry: \n3 : Find all entries from name \n4 : Find the entry with phone number \n5 : Exit\n\nPlease enter your choice: "))
    if choice==1:
        new_phone_book=insert()
        phone_book={**phone_book,**new_phone_book}
        print()
    elif choice==2:
        new_phone_book=delete()
        phone_book={**phone_book,**new_phone_book}
        print()
    elif choice==3:
        print(find_name())
        print()
    elif choice==4:
        print(find_phone())
        print()
    elif choice==5:
        write()
        break