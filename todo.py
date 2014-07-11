# coding: utf-8
import sqlite3
from bottle import route,run,debug

@route('/todo')
@route('/my_todo_list')
def todolist():
	conn = sqlite3.connect('todo.db')
	c = conn.cursor()
	c.execute("select id,task from todo where status like '1'")
	result = c.fetchall()
	return str(result)


debug(True)
run()