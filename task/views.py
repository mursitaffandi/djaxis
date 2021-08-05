from django.shortcuts import render
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


def about(req):
	return render(req, 'about.html')