from django.shortcuts import render

# Create your views here.

def index(req):
	if req.POST:
		username = req.POST['username']
		confirm_pasword = req.POST['confirm_pasword']
		print(username)
		print(confirm_pasword)
	return render(req, 'index.html')


def about(req):
	return render(req, 'about.html')