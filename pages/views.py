from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.

def home_view(request, *args, **kwargs) :
	#print(request)
	print(request.user) # will be "AnanimousUser" if user requesting is not logged in !
	return hr("<h1>Hello World</h1>")

def contact_view(request,*args, **kwargs) :
	return hr("<h1>Contact page</h1>")
