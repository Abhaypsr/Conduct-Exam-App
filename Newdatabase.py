import sqlite3

conn=sqlite3.connect("newdatabase")
tablename='exam'

#conn.execute("Create table '"+tablename+"' (name char[20] Primary key not null,status char[10] not null,day int not null,month int not null,year int not null,stream char[20] not null,fee int not null,description char[50] );")


j=[]
t=conn.execute("delete from exam where name='tempexam1'")
for ch in t:
    print(ch)
    
conn.commit()
print('database created')