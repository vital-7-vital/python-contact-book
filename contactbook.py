
phone={}
def add_cont():
    name=input("enter the name")
    contact=input("enter the contact")
    phone[name]=contact
def view_cont():
    for k,v in phone.items():
        print(k,v)
def ser_ch():
    sname=input("seach name: ")
    if sname in phone:
        print(sname,":",phone[sname])
    else :
        print("doesnt exist")
e=1
while(e==1):
    choice=int (input("1 Add contact\n2 View contacts\n3 Search contact\n4 Exit\n"))
    match choice:
        case 1:
            add_cont()
        case 2:
            view_cont()
        case 3:
            ser_ch()
        case 4:
            print("exit")
            e=e+1

