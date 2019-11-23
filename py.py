x=open('uin','a')
x.close()
del x

def modify(empid):


def deldet(empid):


def delemp(empid):



def empadd(addid):
    elist=open("uin","a")
    elist.write(addid+"\n")
    fileadd=open(addid,'a')
    add=True
    while add:
        a=input("Property: ")
        b=input("Value: ")
        c=a+': '+b
        fileadd.write(c)
        eq=input("Do you want to add more? [y/n]")
        eq=eq.lower()
        while 0<1:
            if eq=='y':
                add=True
                break
            if eq=='n':
                add=False
                break
            else:
                print("Invalid input. Please try again.")
    fileadd.close()
    del fileadd


def empfound(empid):
    empdet=open(empid,'r')
    for i in empdet.readlines():
        print(i[:-1])
    empdet.close()
    del empdet
    mod=False
    md=input("Do you want to modify anything? [y/n]")
    md=md.lower()
    while 0<1:
        if md=='y':
            mod=True
            break
        if md=='n':
            break
        else:
            print("Invalid input. Please try again.")
    if mod:
        print('''What do you want to do?
1. Modify details
2. Delete details
3. Delete employee''')
        while 0<1:
            opt=input("Choose your option: ")
            if opt in "123":
                if opt=='1':
                    modify(empid)
                if opt=='2':
                    deldet(empid)
                if opt=='3':
                    delemp(empid)
                break    
            else:
                print("Invalid input. Please try again.")
        
        

enquiry=True
while enquiry:
    uid=input("Enter Employee UIN: ")
    elist=open("uin","r")
    for i in elist.readlines():
        if i==(uid+"\n"):
            elist.close()
            empfound(uid)
            break
    else:
        elist.close()
        print("Employee not found")
        while 0<1:
            asdf=input("Do you want to add the employee? [y/n] ")
            asdf=asdf.lower()
            if asdf=='y':
                empadd(uid)
                break
            if asdf=='n':
                break
            else:
                print("Invalid input. Please try again.")
    while 0<1:
        enq=input("Do you want to check again? [y/n]")
        enq=enq.lower()
        if enq=='y':
            enquiry=True
            break
        if enq=='n':
            enquiry=False
            break
        else:
            print("Invalid input. Please try again.")
