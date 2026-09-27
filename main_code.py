import tkinter
from tkinter import*
from tkinter import messagebox
import pandas as pd
r=Tk()
r.title("login")
r.geometry('700x600')
c=Canvas(r)
global s
s=""
def captcha():
    global s
    import random
    i=1
    while(i<=6):
        y=random.randint(1,3)
        if(y==1):
            z=random.randint(65,90)
        elif(y==2):
            z=random.randint(97,122)
        elif(y==3):
            z=random.randint(48,57)
        s=s+chr(z)
        i=i+1  
    return s
l1=Label(r,text="username",font=('arial',18))
l1.place(relx=0.2,rely=0.1,relwidth=0.3,relheight=0.1)
t1=Entry(r)
t1.place(relx=0.55,rely=0.1,relwidth=0.3,relheight=0.1)
l2=Label(r,text="password",font=('arial',18))
l2.place(relx=0.2,rely=0.25,relwidth=0.3,relheight=0.1)
t2=Entry(r,show="*")
t2.place(relx=0.55,rely=0.25,relwidth=0.3,relheight=0.1)
l3=Label(r,text=captcha(),bg="yellow",font=('arial',18))
l3.place(relx=0.2,rely=0.4,relwidth=0.3,relheight=0.1)
t3=Entry(r)
t3.place(relx=0.55,rely=0.4,relwidth=0.3,relheight=0.1)
B1=Button(r,text="cancel",command=r.destroy)
B1.place(relx=0.1,rely=0.75,relwidth=0.2,relheight=0.1)
def logbtn():
    u=t1.get()
    p=t2.get()
    f=0
    d=pd.read_excel('user.xlsx')
    lc=list(d["code"])
    lu=list(d["username"])
    lp=list(d["password"])
    i=0
    while(i<len(lu)):
        if((lu[i]==u)and(str(lp[i])==p)):
            f=1
            break
        i+=1
    
    global s
    ch=t3.get()
    if(ch!=s):
       messagebox.showerror("error","chaptcha notvalid")
    if(f==1):
       messagebox.showinfo("warning","welcome")
    else:
        a1=messagebox.askokcancel("warning","do you want to register?")
        if(a1==True):
            r2=Tk()
            r2.title('register')
            r2.geometry("600x600")
            c2=Canvas(r2)
            def regbtn():
                d=pd.read_excel('user.xlsx')
                lco=list(d["code"])
                lu1=list(d["username"])
                lp1=list(d["password"])
                lco.append(t11.get())
                lu1.append(t12.get())
                lp1.append(t13.get())
                d=pd.DataFrame(list(zip(lco,lu1,lp1)),columns=["code","username","password"])
                d.to_excel('user.xlsx')
            l11=Label(r2,text="code")
            l12=Label(r2,text="username")
            l13=Label(r2,text="password")
            t11=Entry(r2)
            t12=Entry(r2)
            t13=Entry(r2)
            B3=Button(r2,text="register",command=regbtn)
            l11.place(relx=0.1,rely=0.1,relwidth=0.2,relheight=0.1)
            l12.place(relx=0.1,rely=0.3,relwidth=0.2,relheight=0.1)
            l13.place(relx=0.1,rely=0.5,relwidth=0.2,relheight=0.1)
            t11.place(relx=0.4,rely=0.1,relwidth=0.2,relheight=0.1)
            t12.place(relx=0.4,rely=0.3,relwidth=0.2,relheight=0.1)
            t13.place(relx=0.4,rely=0.5,relwidth=0.2,relheight=0.1)
            B3.place(relx=0.4,rely=0.8,relwidth=0.2,relheight=0.1)
            r2.mainloop()
B2=Button(r,text="login",command=logbtn)
B2.place(relx=0.4,rely=0.75,relwidth=0.2,relheight=0.1)
def forgetmain():
    r3=Tk()
    r3.title('forget password')
    r3.geometry("500x500")
    c3=Canvas(r3)
    def forgetp():
        d=pd.read_excel('user.xlsx')
        lco=list(d["code"])
        lu=list(d["username"])
        lp=list(d["password"])
        cp=t14.get()
        for i in range(len(lco)):
            if(cp==str(lco[i])):
                s=str(lu[i])+""+str(lp[i])
                messagebox.showinfo("show",s)
                break
    l14=Label(r3,text="code")
    l14.place(relx=0.1,rely=0.1,relwidth=0.15,relheight=0.1)
    t14=Entry(r3)
    t14.place(relx=0.3,rely=0.1,relwidth=0.2,relheight=0.1)
    B5=Button(r3,text="search",command=forgetp)
    B5.place(relx=0.4,rely=0.5,relwidth=0.2,relheight=0.1)
    r3.mainloop()
B4=Button(r,text="forget password",command=forgetmain)
B4.place(relx=0.7,rely=0.75,relwidth=0.2,relheight=0.1)
r.mainloop()
