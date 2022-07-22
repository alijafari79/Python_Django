from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.

def home_view(request, *args, **kwargs) :
	print(args)
	print(">> User: ", request.user)
	#print(request.user) # will be "AnanimousUser" if user requesting is not logged in !
	
	context_vars = {
		"ages":[12,10,21],
		"my_email": "aj@gmail.com"
	}
	# return hr("<h1>Hello World</h1>")
	return render(request, "home.html", context_vars)

def contact_view(request,*args, **kwargs) :
	return render(request, "contacts.html", {})
