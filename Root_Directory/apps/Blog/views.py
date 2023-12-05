from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .forms import BlogForm
from .models import Blog
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db.models import Count

def blog_home(request):
	blogs = Blog.objects.all()
	popular = Blog.objects.all().order_by('-views')[:5]
	most_likes = Blog.objects.annotate(like=Count('likes')).order_by('-like')[:5]
	return render(request, 'blog_home.html',{'blogs': blogs, 'popular': popular, 'most_likes': most_likes})

def article_form(request): 
	if request.method == 'POST':
		blog = Blog(writer=request.user)
		form = BlogForm(request.POST, instance=blog)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request, 'article_form.html', {'form': form})
	else:
		form = BlogForm()
		return render(request, 'article_form.html', {'form': form})

def blog_detail(request, blog_id):
	blog = Blog.objects.get(pk=blog_id)
	blog.views = blog.views+1
	blog.save()
	return render(request, 'blog_detail.html', {'blog': blog})

class BlogLikeView(DetailView):
	model = Blog
	template_name = 'blog_detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super(BlogLikeView, self).get_context_data(*args, **kwargs)

		stuff = get_object_or_404(Blog, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context['total_likes'] = total_likes
		context['liked'] = liked
		return context
	

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

def LikeView(request, id):
	blog = get_object_or_404(Blog, id=request.POST.get('blog_id'))

	if blog.likes.filter(id=request.user.id).exists():
		blog.likes.remove(request.user)

	else:
		blog.likes.add(request.user)

	return HttpResponseRedirect(reverse('blog:blog_like', args=[str(id)]))




		

