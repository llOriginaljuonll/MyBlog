from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
from django.contrib import messages

def blog_home(request):
	return render(request, 'base.html')

def article_form(request): 
	if request.method == 'POST':
		blog = Blog(writer=request.user)
		form = BlogForm(request.POST, instance=blog)
		if form.is_valid():
			form.save()
			return redirect('blog_home.html')
		else:
			return render(request, 'article_form.html', {'form': form})
	else:
		form = BlogForm()
		return render(request, 'article_form.html', {'form': form})
	
def blog_home(request):
	blogs = Blog.objects.all()
	return render(request, 'blog_home.html',{'blogs': blogs})

def blog_detail(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	return render(request, 'blog_detail.html', {'blog': blog})

def blog_edit(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	form = BlogForm(request.POST or None, instance=blog)

	if form.is_valid():
		form.save()
		return redirect('/')
	return render(request, 'blog_edit.html', {'form': form})

def blog_delete(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	blog.delete()
	messages.success(request, 'Blog has been successfully deleted.')
	return redirect('/')