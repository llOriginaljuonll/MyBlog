from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from .forms import BlogForm
from .models import Blog
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

def blog_home(request):
	blogs = Blog.objects.all()
	popular = Blog.objects.all().order_by('-views')[:4]
	views_scores = Blog.objects.values('views')
	like_scores = Blog.objects.values('likes')
	populars = views_scores + like_scores
	populars = Blog.objects.all().order_by(Blog.total_scores)
	return render(request, 'blog_home.html',{'blogs': blogs, 'populars': populars})

Blog.total_likes(1)

"""
ส่วนที่น่าสนใจของฟังก์ชั่นนี้
-> การดึงข้อมูลจาก Default User model.
-> request.user = ชื่อของ user(username)
-> กระบวนการทำงานของฟังก์ชั่น
  -> ถ้าเป็นการส่งข้อมูลแบบ POST (ดูได้ที่ form ใน template ว่ามีการระบุ method="post" หรือไม่) ให้ทำงานต่อไป
    -> writer_field จะเท่ากับ request.user(อธิบายไว้แล้วในบรรทัดก่อนหน้านี้)
	-> ปกติการดึง form จาก forms.py เราต้องทำอยู่แล้ว แต่ครั้งนี้เราให้อยู่บรรทัดล่างเพื่อรับข้อมูลของ request.user เป็นไปได้ที่เรายังไม่รู้ท่าในการแก้ใน forms.py หรือ models.py เลยต้องใช้ท่านี้ก่อน
	-> มีการสร้างตัวแปร form เก็บข้อมูลของ BlogForm
	  -> instance=blog เก็บข้อมูลเฉพาะ blog(ยังรู้ข้อมูลไม่แน่ชัด มีเวลาควรศึกษาเพิ่ม)
	  -> request.POST (ศึกษาเพิ่ม)
	  -> จนถึงตอนนี้ได้มีการนำข้อมูลของ username ของ default model มารวมกับ BlogForm แล้ว
	-> ถ้ามีการกรอกข้อมูลถูกต้องให้ทำการบันทึกและ redirect ไปที่หน้า ('/')
	-> ถ้ามีการกรอกข้อมูลไม่ถูกต้องให้ render ที่หน้าฟอร์มเริ่มใหม่อีกครั้งหนึ่ง
  -> ถ้าการส่งข้อมูลไม่ใช่แบบ POST (อาจมีการ refresh) ให้ render ที่หน้าฟอร์มเริ่มใหม่อีกครั้งหนึ่ง
"""
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
	liked = False

	if blog.likes.filter(id=request.user.id).exists():
		blog.likes.remove(request.user)
		liked = False

	else:
		blog.likes.add(request.user)
		liked = True

	return HttpResponseRedirect(reverse('blog:blog_like', args=[str(id)]))




		

