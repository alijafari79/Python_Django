from django.shortcuts import render
from django.http import HttpResponse as hr
# Create your views here.

def home_view(*args, **kwargs) :
	return hr("<h1>Hello World</h1>")

