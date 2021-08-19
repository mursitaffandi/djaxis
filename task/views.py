from django.shortcuts import redirect, render
from . import models
import psycopg2
from config.config import config

# Create your views here.

def index(req):
	params = config('config/database.ini')
	conn = psycopg2.connect(**params)
	cur = conn.cursor()
	if req.POST:
		username = req.POST['username']
		confirm_pasword = req.POST['confirm_pasword']
		
		cur.execute("INSERT INTO task_tugas(name) VALUES(%s);", (username,))
		conn.commit()
		# models.tugas.objects.create(name=username)
	
	# data = models.tugas.objects.all()
	cur.execute("select * from task_tugas")
	dataFetch = cur.fetchall()
	for row in dataFetch:
		print("Id = ", row[0], )
		print("name = ", row[1], "\n")

	cur.close()
	conn.close()
	return render(req, 'index.html', {
		'list_tugas' : dataFetch,
		})

def update(req, id):
	# currentData = models.tugas.objects.filter(pk=id)
	params = config('config/database.ini')
	conn = psycopg2.connect(**params)
	conn.autocommit = True
	cur = conn.cursor()
	if req.POST:
		new_name = req.POST['username']
		cur.execute("UPDATE task_tugas SET name = %s WHERE id = %s", (new_name, id))
		cur.close()
		conn.close()
		return redirect('/')

	cur.execute("select * from task_tugas where id = %s", (id,))
	currentData = cur.fetchall()
	cur.close()
	conn.close()
	return render(req, 'update.html', {
		'current_name' : currentData[0][1]
	})

def delete(req, id):
	models.tugas.objects.filter(pk=id).delete()
	return redirect('/')

def about(req):
	return render(req, 'about.html')
