#create hash table
phone_book = {}

#add key-values
phone_book['Mother']='+77788842424'
phone_book['Father']='+88877724242'
phone_book['Sister M']="+333222129"
phone_book['Brother P']="+55576767"

#create function for checking contacts (if they already exist or not)
def check_contacts(name):
    if name not in phone_book:
        phone_book[name]=True
        number=input("Enter the number: ")
        phone_book[name]=number
        print("Adding this contact")
        print(phone_book)
    else:
        print("This contact already exists")

check_contacts('Sister E')