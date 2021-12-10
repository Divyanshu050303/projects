import pathlib
import os.path, time
import datetime

t=0
def getdate():
    import datetime
    return  datetime.datetime.now()
def add(name, id, lug):

    with open(name, "a") as op:
        op.write(str([str(getdate())])+" : "+ " "+name+"  "+id+" "+lug +'\n')

        print("**********************************************************")
        print("Record added Successfully")
        print("Thank you ")
        print("**********************************************************")

def search(nam):
    file=pathlib.Path(nam)
    if(file.exists()):
        f=open(nam)
        if ( f.read()):
            print("*********************************************************")
            print("Record Found")
            print("**********************************************************")
    else:
        print("*********************************************************")
        print("Record not found")
        print("*********************************************************")
def amount(nam):
    file = pathlib.Path(nam)
    if (file.exists()):
        ti_m = os.path.getmtime(nam)
        m_ti = time.ctime(ti_m)
        t_obj = time.strptime(m_ti)
        T_stamp = time.strftime("%b %d %Y %H:%M%S", t_obj)
        t = datetime.datetime.now()
        d=datetime.datetime.strptime(T_stamp, "%b %d %Y %H:%M%S")
        c=t-d
        h=c.total_seconds()//60
        print(h,"mins")
        g=h/60
        if(g>0 and g<=1):
            print("Rs",g*50)
            print("*********************************************************")
            os.remove(nam)
        elif(g>1 and g<=2):
            print("Rs",g*100)
            print("*********************************************************")
            os.remove(nam)
        elif(g>3 and g<=5):
            print("Rs",g*150)
            print("*********************************************************")
            os.remove(nam)
        else:
            print("Rs",g*500)
            print("*********************************************************")
            os.remove(nam)
    else:
        print("Record not found")
        print("*********************************************************")
while(True):
    print("Enter Your Choice:")
    print("1. Add record")
    print("2. Search record")
    print("3. Amount To Be Paid")
    print("4. Exit")
    n=int(input("Enter the operation: "))
    if(n==1):
        print("*********************************************************")
        name=input("Enter the name : ")
        id=input("Enter the id : ")
        lug=input("Enter the item_name : ")
        add(name, id, lug)
        t=datetime.datetime.now()
    elif(n==2):
        print("*********************************************************")
        nam=input("Enter the name")
        search(nam)
    elif(n==3):
        print("*********************************************************")
        nam=input("Enter the name")
        amount(nam)
    elif(n==4):
        print("*********************************************************")
        print("Successfully Exited")
        print("*********************************************************")
        break
    else:
        print("*********************************************************")
        print("Wrong choice")
        print("*********************************************************")
