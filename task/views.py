from django.shortcuts import render

# Create your views here.

def index(req):
	if req.POST:
		username = req.POST['username']
		print(username)
	return render(req, 'index.html')


def about(req):
	return render(req, 'about.html')