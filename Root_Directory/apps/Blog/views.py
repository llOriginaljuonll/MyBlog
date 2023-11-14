from django.shortcuts import render, redirect
from .forms import WriterBlogForm

def Blog(request):
	return render(request, 'base.html')

def article(request):
	form = WriterBlogForm()
	if form.is_valid():
		form.save()
		return redirect('') # ในอนาคตน่าจะชื่อว่า article
	else:
		form = WriterBlogForm
		return render(request, 'article_form.html', {'form': form})
