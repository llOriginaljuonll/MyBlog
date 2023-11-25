from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog, Like
from django.contrib import messages

def blog_home(request):
	blogs = Blog.objects.all()
	popular = Blog.objects.all().order_by('-views')[:4]
	return render(request, 'blog_home.html',{'blogs': blogs, 'popular': popular})

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

def like_post(request):
	user = request.user
	if request.methond == 'POST':
		post_id = request.POST.get('post_id')
		post_obj = Blog.objects.get(id=post_id)

		if user in post_obj.liked.all():
			post_obj.liked.remove(user)
		else:
			post_obj.liked.add(user)

		like, created = Like.objects.get_or_create(user=user, post_id=post_id)

		if not created:
			if like.value == 'Like':
				like.value = 'unlike'
			else:
				like.value = 'Like'

		like.save()
	return redirect('blog:blog_detail')

		

