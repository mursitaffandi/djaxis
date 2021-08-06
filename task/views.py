from django.shortcuts import redirect, render
from . import models
# Create your views here.


def index(req):
	if req.POST:
		username = req.POST['username']
		confirm_pasword = req.POST['confirm_pasword']
		print(username)
		print(confirm_pasword)
		models.tugas.objects.create(name=username)
	
	data = models.tugas.objects.all()
	return render(req, 'index.html', {
		'list_tugas' : data,
		})

def update(req, id):
	currentData = models.tugas.objects.filter(pk=id)
	if req.POST:
		new_name = req.POST['username']
		currentData.update(name = new_name)
		return redirect('/')

	return render(req, 'update.html', {
		'current_name' : currentData.first().name
	})

def delete(req, id):
	models.tugas.objects.filter(pk=id).delete()
	return redirect('/')

def about(req):
	return render(req, 'about.html')