# coding: utf-8
import sqlite3
conn = sqlite3.connect("todo.db")
conn.execute("create table todo (id integer primary key,task char(100) not null,status bool not null)")
conn.execute("insert into todo (task,status) values('this is 1',1)")
conn.execute("insert into todo (task,status) values('this is 2',1)")
conn.execute("insert into todo (task,status) values('this is 3',0)")
conn.execute("insert into todo (task,status) values('this is 4',1)")
conn.commit()
conn.close()
