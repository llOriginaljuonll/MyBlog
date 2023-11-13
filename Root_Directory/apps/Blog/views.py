from django.shortcuts import render
from django.http import HttpResponse

def Blog(request):
	return HttpResponse('<h1>Welcome My Blog</h1>')

