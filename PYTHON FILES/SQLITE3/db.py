import sqlite3
try:
	def insertvalue(name,age,city):
		con=sqlite3.connect('users.db')
		qry="insert into users (NAME,AGE,CITY) values (?,?,?);"
		con.execute(qry,(name,age,city))
		con.commit()
	def updatevalue(name,age,city,id):
		con=sqlite3.connect('users.db')
		qry="update users set NAME=?,AGE=?,CITY=? where ID=?;"
		con.execute(qry,(name,age,city,id))
		con.commit()
	def deletevalue(id):
		con=sqlite3.connect('users.db')
		qry="delete from users where id=?;"
		con.execute(qry,(id))
		con.commit()
	def selectvalues():
		con=sqlite3.connect('users.db')
		qry="select * from users"
		result=con.execute(qry)
		for i in result:
			print(i)
		
	ch=1
	while ch==1:
		print("""
		1.INSERT
		2.UPDATE
		3.DELETE
		4.SELECT
		""")
		c=int(input("ENTER THE CHOICE : "))
		if c==1:
			name=input("ENTER THE NAME : ")
			age=input("ENTER THE AGE : ")
			city=input("ENTER THE CITY : ")
			insertvalue(name,age,city)
			print("VALUES INSERTED IN THE DATABASE")
		elif c==2:
			id=input("ENTER THE ID NUMBER : ")
			name=input("ENTER THE NAME : ")
			age=input("ENTER THE AGE : ")
			city=input("ENTER THE CITY : ")
			updatevalue(name,age,city,id)
			print("VALUES ARE UPDATED IN THE DATA BASE")
		elif c==3:
			id=input("ENTER THE ID : ")
			deletevalue(id)
			print("VALUES ARE DELETED FROM THE DATABASE")
		elif c==4:
			selectvalues()
			print("VALUES ARE PRINTED")
		else:
			print("ENTER A VALID CHOICE")
		ch=int(input("ENTER 1 TO CONTINUE OR TO EXIT"))
except:
	print("ERROR")
print("THANK YOU")