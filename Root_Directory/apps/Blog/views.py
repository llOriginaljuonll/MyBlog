from django.shortcuts import render, redirect
from .forms import WriterBlogForm
from .models import WriterBlog

def blog_home(request):
	return render(request, 'base.html')

def article_form(request): 
	if request.method == 'POST':
		form = WriterBlogForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request, '/', {'form': form})
	else:
		form = WriterBlogForm()
		return render(request, 'article_form.html', {'form': form})
	
def blog_home(request):
	blogs = WriterBlog.objects.all()
	return render(request, 'blog_home.html',{'blogs': blogs})
