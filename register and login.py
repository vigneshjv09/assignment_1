global x
global y
global pw
def login():
    maill=input("Enter your mail id to login")
    pwl=input("enter your password to login")
    if check2(maill,pwl)==1:
        print("login success")
def forgetpw():
    mailf=input("enter your mail id")
    if check(mailf)==1:
        print("no username found do you wanna signup(Y/N)")
        r=input()
        if r=='Y' or r=='y':
            register()
    else:
        print("1.Retrieve password\n2.Replace password")
        rp=int(input())
        if rp==1:
            retrive(mailf)
        elif rp==2:
            print("replace password will update soon......")
            #rplc()#mailf

def rplc(s,pw2):
    mails=[]
    pws=[]
    d = open("register.txt", "r")

    for i in d:
        x,y=i.split(",")
        y=y.strip()
        mails.append(x)
        pws.append(y)
    if s in mails:
        idx2=(mails.index(s))
        rpl=pws[idx2]
        print(rpl)
        pws.insert(idx2,pw2)
    else:
        print("username not found press 1 to resgister")
        pn=input()
        if pn=='1':
            register()


def register():
    global mail
    mail=input("Enter your Mail id")
    cout=0
    if "@" in mail:
        cout+=1
        idx = mail.index("@")
        if "." in mail:
            cout+=1
            if mail[idx+1]!=".":
                cout+=1
                if mail[0].islower():
                    cout+=1
                else:
                    print("first letter should in alphabetic try again!!!")
                    register()
            else:
                print("dont put . immediate to @ try again!!!")
                register()
        else:
            print("mail id shoud have . try again!!!")
            register()
    else:
        print("mail id should have @ try again!!!")
    if cout==4:
        print("valid mail")
        password()
def password():
    def splchr(s):
        for i in s:
            if i in "~!@`#$%^&*()_-=+><.,/?\|" :
                return 1
                break
    def upper1(s):
        for i in s:
            if i.isupper():
                return 1
                break
    def lower1(s):
        for i in s:
            if i.islower():
                return 1
                break
    def digit1(s):
        for i in s:
            if i.isdigit():
                return 1
                break
    pw=input("Enter Your PassWord")
    cout1=0
    lenght=len(pw)
    #specialchr=
    if lenght > 5 and lenght< 16:
        if splchr(pw)==1:
            if upper1(pw)==1:
                if lower1(pw)==1:
                    if digit1(pw)==1:
                        cout1+=1
                    else:
                        print("password must have a digit")
                        password()
                else:
                    print("password must have a lowercase try again !!!")
                    password()
            else:
                print("password must have a uppercase try again !!!")
                password()
        else:
            print("password must have a special character try again !!!")
            password()
    else:
        print("password should have minimum 5 to 16")
        password()
    if cout1==1:
        try :
            storedata(mail,pw)
        except NameError:
            return pw
def retrive(s):
    mails=[]
    pws=[]
    d = open("register.txt", "r")
    for i in d:
        x,y=i.split(",")
        y=y.strip()
        mails.append(x)
        pws.append(y)
    idx2=mails.index(s)
    pws1=pws[idx2]
    print("your password is :",pws1)

def check(s):
    mails=[]
    pws=[]
    d = open("register.txt", "r")
    for i in d:
        x,y=i.split(",")
        y=y.strip()
        mails.append(x)
        pws.append(y)
    if s  not in mails or len(mails)==0:
        return 1
    else:
        return 0
    d.close()
def check2(s,d1):
    mails=[]
    pws=[]
    d = open("register.txt", "r")
    for i in d:
        x,y=i.split(",")
        y=y.strip()
        mails.append(x)
        pws.append(y)
    if s in mails:
        if (pws[mails.index(s)])==d1:
            return 1
        else:
            print("missmatching password press 3 to forget password ")
            a=input()
            if a=='3':
                forgetpw()
                """mailp=input("enter your mail id")
                if check(mailp)==0:
                    print("your password is:",pws[mails.index(mailp)])
                else:
                    print("no user found press 1 to registration")
                    ma1=input()
                    if ma1=='1':
                         register()
            elif a=='2':
                print("enter your mail id")
                ma3=input()
                print("enter your new password")
                po=password()
                rplc(ma3,po)"""

            else:
                print("thankyou")
    else:
        print("no user found press 1  to registration!!!")
        b=input()
        if b=='1':
            register()
    d.close()
def storedata(mail1,pword):
    if check(mail1)==1:
        d=open("register.txt","a")
        d.writelines(mail1+","+pword+"\n")
        print("Registration successfull")
        d.close()
    else:
        print("user id exists please try different name")
        register()

#driver code
print("1.Register\n2.login\n3.Forget Password")
userinput=int(input())
if userinput==1:
    register()
elif userinput==2:
    login()
elif userinput==3:
    print("forget password")
    forgetpw()
else:
    print("please select valid option")
