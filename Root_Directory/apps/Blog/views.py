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

def blog_detail(request, blog_id):
	blog = WriterBlog.objects.get(pk=blog_id)
	return render(request, 'blog_detail.html', {'blog': blog})

def blog_edit(request, blog_id):
	blog_detail = WriterBlog.objects.get(pk=blog_id)
	form = WriterBlogForm(request.POST or None, instance=blog_detail)

	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request, 'blog_edit.html', {'form': form})