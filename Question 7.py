phone_book={}

def insert():
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
    del_entry=input("Enter entry to be deleted: ")
    del phone_book[del_entry]
    return phone_book

def find_name():
    name_find=input("Enter name to search: ")
    return phone_book[name_find]

def find_phone():
    phone=int(input("Enter phone number to search: "))
    res=[val[phone] for key,val in phone_book.items() if phone in val]
    return res

while True:
    choice=int(input("1 : Inserting new entry: \n2 : Deleting an entry: \n3 : Find all entries from name \n4 : Find the entry with phone number \n5 : Exit\n\nPlease enter your choice: "))
    if choice==1:
        insert()
        print()
    elif choice==2:
        delete()
        print()
    elif choice==3:
        print(find_name())
        print()
    elif choice==4:
        print(find_phone())
        print()
    elif choice==5:
        break