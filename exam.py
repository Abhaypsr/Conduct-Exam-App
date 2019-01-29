from tkinter import *
import time
import sqlite3
conn = sqlite3.connect('Newdatabase')
win=Tk()
win.geometry("500x400+200+100")
win.title("Exam")
win.resizable(width=False,height=False)
f1=Frame(win)
f1.pack(side=TOP)
f1.pack_propagate(False)
f1=Frame(win,height=50,width=600)
f1.pack(side=TOP)
f1.pack_propagate(False)
f2=Frame(win,height=450,width=600,bg="white")
f2.pack(side=TOP)
f2.pack_propagate(False)
Label(f1,text="CONDUCT EXAM PROCESS",font=('arial',25,'bold'),bg="blue",fg="wheat",width=70).pack(side=LEFT)
def home():
    win.geometry("600x500+150+70")
    f2.config(bg="blue")
    def bk(g):
        h.config(bg="white")
        p.config(bg="white")
        r.config(bg="white")
        ue.config(bg="white")
        ce.config(bg="white")
        lo.config(bg="white")
        g.config(bg="yellow")
    def homebutton():
        bk(h)
        for ch in f4.winfo_children():
            ch.destroy()
        Label(f4,text="Write something....",bg="white",fg="gray40").place(x=30,y=50)
        Text(f4,width=30,height=5).place(x=30,y=80)
        Button(f4,text="Post",bg="blue",fg="white",width=7).place(x=30,y=180)
    def upcomingexam():
        bk(ue)
        for ch in f4.winfo_children():
            ch.destroy()
        def upcomingexamfind():
            pass
        def form1(tname,ty):
            def formfill(tname):
                for ch in tf.winfo_children():
                    ch.destroy()
                
                Button(tf,text=tname,font=('arial',20),bg="white",fg="black").place(x=100,y=5)
                Label(tf,text="Sqllabus:- zset     \nTotal marks :- 380\nConduct on :- 12/12/2019",bg="white",fg="gray40").place(x=200,y=5)
                Label(tf,text="Student name",bg="white",width=12).place(x=40,y=80)
                Entry(tf).place(x=170,y=80)
                Label(tf,text="father name",bg="white",width=12).place(x=40,y=110)
                Entry(tf).place(x=170,y=110)
                Label(tf,text="Student Age",bg="white",width=12).place(x=40,y=140)
                Entry(tf).place(x=170,y=140)
                Label(tf,text="12th marks ",bg="white",width=12).place(x=40,y=170)
                Entry(tf).place(x=170,y=170)
                Label(tf,text="Mobile no.",bg="white",width=12).place(x=40,y=200)
                Entry(tf).place(x=170,y=200)
                Label(tf,text="Email address",bg="white",width=12).place(x=40,y=230)
                Entry(tf).place(x=170,y=230)
                Label(tf,text="Aadhar no.",bg="white",width=12).place(x=40,y=260)
                Entry(tf).place(x=170,y=260)
                Label(tf,text="Enter city",bg="white",width=12).place(x=40,y=290)
                Entry(tf).place(x=170,y=290)
                Entry(tf).place(x=300,y=290)
                Label(tf,text="Avilable city:-",bg="white",fg="gray50").place(x=250,y=320)
                Label(tf,text="city1\ncity2",bg="white",fg="gray50").place(x=320,y=320)
                Button(tf,text="Submit",bg="yellow",fg="black",font=('arial',12)).place(x=120,y=360)
#            fset.config(bg="yellow",fg="black")
            j=[]
            t=conn.execute("select stream,day,month,year from exam where name='"+tname+"'")
            for ch in t:
                j.append(ch)
            Label(tf,text="Title:-"+str(tname)+"    \nSqllabus:"+str(j[0][0])+"     \nConduct on :-"+str(j[0][1])+"/"+str(j[0][2])+"/"+str(j[0][3]),bg="white",fg="gray50").place(x=110,y=ty)
            Button(tf,text="Form fill",bg="white",command=lambda: formfill(tname)).place(x=300,y=ty)
        tf=Frame(f4,width=480,height=450,bg="white",highlightbackground="gray80",highlightcolor="gray80",highlightthickness=2)
        tf.place(x=0,y=0)
        Label(tf,text="Upcoming Exam --",bg="white",fg="gray30").place(x=20,y=20)
        t=conn.execute("select name from exam where status='Active'")
        j=[]
        k=0
        ty=80
        for ch in t:
            j.append(ch[0])
            k=k+1
        if k>0:
            Button(tf,text=str(j[0]),bg="blue",font=('arial',15),width=7,fg="white",height=3,command=lambda: form1(j[0],ty)).place(x=20,y=70)
            k=k-1
        if k>0:
            Button(tf,text=str(j[1]),bg="blue",font=('arial',15),width=7,fg="white",height=3,command=lambda: form1(j[1],ty+130)).place(x=20,y=200)
            k=k-1
        if k>0:
            Button(tf,text=str(j[2]),bg="blue",font=('arial',15),width=7,fg="white",height=3,command=lambda: form1(j[2],ty+260)).place(x=20,y=330)
            k=k-1
        
    def profile():
        bk(p)
        for ch in f4.winfo_children():
            ch.destroy()
        tname=conn.execute("select name from user where name=('"+name.get()+"')")
        for i in tname:
            t=i
        Label(f4,text="Name  - "+str(t[0]),font=('arial',10),bg="white").place(x=20,y=50)
        tname=conn.execute("select mail from user where name=('"+name.get()+"')")
        for i in tname:
            t=i
        Label(f4,text="Mail  - "+str(t[0]),font=('arial',10),bg="white").place(x=20,y=100)
        tname=conn.execute("select age from user where name=('"+name.get()+"')")
        for i in tname:
            t=i
        Label(f4,text="Age  - "+str(t[0]),font=('arial',10),bg="white").place(x=20,y=150)
        tname=conn.execute("select mobileno from user where name=('"+name.get()+"')")
        for i in tname:
            t=i
        Label(f4,text="Mobile NO.  - "+str(t[0]),font=('arial',10),bg="white").place(x=20,y=200)
        tname=conn.execute("select description from user where name=('"+name.get()+"')")
        for i in tname:
            t=i
        Label(f4,text="Description  - "+str(t[0]),font=('arial',10),bg="white").place(x=20,y=250)
        Button(f4,text="Change profile",bg="blue",fg="white").place(x=70,y=300)
    def conductexam():
        bk(ce)
        def datastore():
            global conn,i,semaphore,d
#            t=0
#            for j in range(i+1):
#                t=t+int(ts[j].get())
#            d=description.get("1.0","end-1c")
            if (time.localtime()[0]<int(year.get())):
                conn.execute("insert into exam (name,status,day,month,year,stream,fee,description) values (?,?,?,?,?,?,?,?)",(title.get(),'Active',date.get(),month.get(),year.get(),stream.get(),fee.get(),d))
            elif (time.localtime()[0]>int(year.get())):
                conn.execute("insert into exam (name,status,day,month,year,stream,fee,description) values (?,?,?,?,?,?,?,?)",(title.get(),'Inactive',date.get(),month.get(),year.get(),stream.get(),fee.get(),d))
            elif (time.localtime()[0]==(year.get())):
                if (time.localtime()[1]<int(month.get())):
                    conn.execute("insert into exam (name,status,day,month,year,stream,fee,description) values (?,?,?,?,?,?,?,?)",(title.get(),'Active',date.get(),month.get(),year.get(),stream.get(),fee.get(),d))
                elif (time.localtime()[1]>int(month.get())):
                    conn.execute("insert into exam (name,status,day,month,year,stream,fee,description) values (?,?,?,?,?,?,?,?)",(title.get(),'Inactive',date.get(),month.get(),year.get(),stream.get(),fee.get(),d))
                elif (time.localtime()[1]==int(month.get())):
                    if (time.localtime()[2]<=int(day.get())):
                        conn.execute("insert into exam (name,status,day,month,year,stream,fee,description) values (?,?,?,?,?,?,?,?)",(title.get(),'Active',date.get(),month.get(),year.get(),stream.get(),fee.get(),d))
                    elif (time.localtime()[2]>int(day.get())):
                        conn.execute("insert into exam (name,status,day,month,year,stream,fee,description) values (?,?,?,?,?,?,?,?)",(title.get(),'Inactive',date.get(),month.get(),year.get(),stream.get(),fee.get(),d))
            conn.commit()
            semaphore=0
        def savenext():
            global i,semaphore,cc
            if semaphore==0:
                conn.execute("create table '"+str(title.get())+"'(centername char[50] not null,city char[20] not null,totalseats int not null)")
                semaphore=1
            for k in f4.winfo_children():
                k.destroy()
            def citycenter():
                global i,x,y
                i=i+1
                y=y+30
                cityin.append(StringVar())
                ts.append(StringVar())
                Entry(f4,text=cityin[i]).place(x=x,y=y)
                Entry(f4,text=ts[i]).place(x=x+150,y=y)
                cc.place(x=650,y=y+30)
            t=0
            for j in range(i+1):
#                t=t+int(ts[j].get())
                conn.execute("insert into '"+title.get()+"'(centername,city,totalseats) VALUES (?,?,?)",(cityin[j].get(),city.get(),int(ts[j].get())))
            cityin.append(StringVar())
            ts.append(StringVar())
            i=0
            Label(f4,text="Select Center :- ",bg="white",fg="blue").place(x=0,y=20)
            Entry(f4,text=city).place(x=50,y=70)
            Entry(f4,text=cityin[i]).place(x=150,y=70)
            Entry(f4,text=ts[i]).place(x=300,y=70)
            cc=Button(f4,text="+",bg="gray98",command=citycenter)
            cc.place(x=150,y=100)
            Button(f4,text="Save and Next",command=savenext).place(x=150,y=350)
            Button(f4,text="Done",bg="yellow",fg="black",command=conductexam).place(x=250,y=400)
        for ch in f4.winfo_children():
            ch.destroy()
        def citycenter():
            global i,x,y,cc
            i=i+1
            y=y+30
            cityin.append(StringVar())
            ts.append(StringVar())
            Entry(f4,text=cityin[i]).place(x=x,y=y)
            Entry(f4,text=ts[i]).place(x=x+150,y=y)
            cc.place(x=150,y=y+30)
#        title=StringVar()
#        stream=StringVar()
#        date=StringVar()
#        month=StringVar()
#        year=StringVar()
#        fee=StringVar()
#        city=StringVar()
#        city.set("")
#        cityin=[]
#        cityin.append(StringVar())
#        cityin[0].set("")
#        ts=[]
#        ts.append(IntVar())
#        ts[i].set("")
        def examd():
            def dget():
                global description,d
                d=description.get("1.0","end-1c")
                conductexam()
            global title,stream,date,month,year,fee,description,d
            for ch in f4.winfo_children():
                ch.destroy()
            Label(f4,text="ENTER EXAM TITLE",bg="white",fg="blue").place(x=20,y=20)
            Entry(f4,text=title).place(x=150,y=20)
            Label(f4,text="STREAM",bg="white",fg="blue").place(x=20,y=70)
            Entry(f4,text=stream).place(x=150,y=70)
            Label(f4,text="DATE OF EXAM",bg="white",fg="blue").place(x=20,y=120)
            Entry(f4,text=date,width=3).place(x=150,y=120)
            Entry(f4,text=month,width=3).place(x=180,y=120)
            Entry(f4,text=year,width=5).place(x=210,y=120)
            Label(f4,text="FORM FEES",bg="white",fg="blue").place(x=20,y=170)
            Entry(f4,text=fee).place(x=150,y=170)
            Label(f4,text="Description : ",bg="white",fg="blue").place(x=20,y=220)
            description=Text(f4,width=30,height=9)
            description.place(x=150,y=220)
            Button(f4,text="Done",bg="yellow",fg="black",command=dget).place(x=100,y=400)
        def centerd():
            global cc,city,cityin,ts,i
            for ch in f4.winfo_children():
                ch.destroy()
            Label(f4,text="Select Center :- ",bg="white",fg="blue").place(x=0,y=20)
            Label(f4,text="Enter city",bg="white").place(x=45,y=50)
            Label(f4,text="Enter center name",bg="white").place(x=150,y=50)
            Label(f4,text="No. of seats",bg="white").place(x=300,y=50)
            Entry(f4,text=city).place(x=50,y=70)
            Entry(f4,text=cityin[i]).place(x=150,y=70)
            Entry(f4,text=ts[i]).place(x=300,y=70)
            cc=Button(f4,text="+",bg="gray98",command=citycenter)
            cc.place(x=150,y=100)
            Button(f4,text="Save and Next",command=savenext,bg="blue",fg="white").place(x=150,y=350)
            Button(f4,text="Done",bg="yellow",fg="black",command=conductexam).place(x=250,y=400)
        Button(f4,text="Exam detail",font=('arial',15,'bold'),bg="blue",fg="white",command=examd).place(x=100,y=100)
        Button(f4,text="Center detail",font=('arial',15,'bold'),bg="blue",fg="white",command=centerd).place(x=100,y=200)
        Button(f4,text="SUBMIT",font=('arial',15,'bold'),bg="YELLOW",command=datastore).place(x=100,y=300)
    for ch in f2.winfo_children():
        ch.destroy()
    f3=Frame(f2,width=120,height=450,bg="blue")
    f3.pack(side=LEFT)
    f3.pack_propagate(False)
    f4=Frame(f2,width=480,height=450,bg="white")
    f4.pack(side=LEFT)
    f4.pack_propagate(False)
#    f5=Frame(f2,width=550,height=350,bg="white")
#    f5.pack(side=RIGHT)
#    f5.pack_propagate(False)
    h=Button(f3,text="HOME",bg="white",width=12,bd=4,command=homebutton)
    h.place(x=10,y=40)
    p=Button(f3,text="PROFILE",bg="white",width=12,bd=4,command=profile)
    p.place(x=10,y=90)
    r=Button(f3,text="RANK",width=12,bg="white",bd=4)
    r.place(x=10,y=140)
    ue=Button(f3,text="UPCOMING\nEXAMS",bd=4,width=12,bg="white",command=upcomingexam)
    ue.place(x=10,y=190)
    ce=Button(f3,text="Conduct Exam",bd=4,width=12,bg="white",command=conductexam)
    ce.place(x=10,y=240)
    lo=Button(f3,text="Log out",bg="white",width=12,bd=4,command=openpage)
    lo.place(x=10,y=290)
    homebutton()
def login():
    def logincheck():
        cursor = conn.execute("select password from login where name='"+name.get()+"'")
        for row in cursor:
            passt=str(row[0])
        if passwd.get()!=passt:
            Label(f2,text="password not match",fg="red",bg="pink").place(x=150,y=180)
            return
        else:
            home()
    for i in f2.winfo_children():
        i.destroy()
    Label(f2,text="ENTER NAME",bg="white",fg="blue").place(x=100,y=100)
    Entry(f2,text=name).place(x=220,y=100)
    Label(f2,text="ENTER PASSWORD",bg="white",fg="blue").place(x=100,y=150)
    Entry(f2,text=passwd).place(x=220,y=150)
    Button(f2,text="LOGIN",command=logincheck,bg="blue",fg="white").place(x=160,y=200)
    Button(f2,text="BACK",command=openpage,bg="yellow",fg="black").place(x=230,y=200)
def signin():
    def signcmplt():
        if passwd1.get()!=passwd2.get():
            Label(f2,text="Passwd not match",fg="red",bg="pink").place(x=120,y=280)
            return
        if name.get()=="":
            Label(f2,text="Empty",fg="red",bg="white").place(x=320,y=100)
            return
        for i in f2.winfo_children():
            i.destroy()
        conn.execute("insert into login (name,mail,password) VALUES (?, ?, ?)",
          (name.get(),mail.get(),passwd1.get()))
        conn.execute("insert into user (name,mail,password) VALUES (?, ?, ?)",
          (name.get(),mail.get(),passwd1.get()))
        
        conn.commit()
        Label(f2,text="Success").pack()
    for i in f2.winfo_children():
        i.destroy()
    Label(f2,text="ENTER NAME",bg="white",fg="blue").place(x=100,y=50)
    Entry(f2,text=name).place(x=220,y=50)
    Label(f2,text="ENTER MAiL",bg="white",fg="blue").place(x=100,y=100)
    Entry(f2,text=mail).place(x=220,y=100)
    Label(f2,text="ENTER PASSWORD",bg="white",fg="blue").place(x=100,y=150)
    Entry(f2,text=passwd1).place(x=220,y=150)
    Label(f2,text="RE-ENTER PASSWORD",bg="white",fg="blue").place(x=100,y=200)
    Entry(f2,text=passwd2).place(x=230,y=200)
    Button(f2,text="SIGN IN",command=signcmplt,bg="blue",fg="white").place(x=160,y=250)
    Button(f2,text="BACK",command=openpage,bg="yellow",fg="black").place(x=250,y=250)
def openpage():
    for i in f2.winfo_children():
        i.destroy()
    Button(f2,text="LOGIN",font=('arial',18,),bg="blue",fg="white",command=login).place(x=100,y=100)
    Button(f2,text="SIGN IN",font=('arial',18),bg="blue",fg="white",command=signin).place(x=100,y=200)
name=StringVar()
name.set("deeraj")
mail=StringVar()
passwd=StringVar()
passwd.set("deerajpass")
passwd1=StringVar()
passwd2=StringVar()
semaphore=0
global f3,f4,cityin,ts,description,cc
title=StringVar()
stream=StringVar()
date=StringVar()
month=StringVar()
year=StringVar()
fee=StringVar()
city=StringVar()
city.set("")
cityin=[]
cityin.append(StringVar())
cityin[0].set("")
ts=[]
ts.append(IntVar())
i=0
ts[i].set("")
x=150
y=70
one=1
d=""
openpage()
win.mainloop()