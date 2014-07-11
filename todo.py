# coding: utf-8
import sqlite3
from bottle import route, run, debug, template, request,get


@route('/todo')
@route('/my_todo_list')
def todolist():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("select id,task from todo where status like '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output


@route('/new', method="GET")
def new_item():
    if request.GET.get('save', '').strip():
        new1 = request.GET.get('task', '').strip().decode("utf-8")
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new1, 1))
        new_id = c.lastrowid
        conn.commit()
        c.close()
        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id
    else:
        return template('new_task.tpl')


debug(True)
run()