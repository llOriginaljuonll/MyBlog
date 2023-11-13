from django.shortcuts import render
from django.http import HttpResponse

def Blog(request):
	return render(request, 'base.html')

