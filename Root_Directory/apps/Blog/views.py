from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
from django.contrib import messages

def blog_home(request):
	blogs = Blog.objects.all()
	return render(request, 'blog_home.html',{'blogs': blogs})

"""
ส่วนที่น่าสนใจของฟังก์ชั่นนี้
-> การดึงข้อมูลจาก Default User model.
-> request.user = ชื่อของ user(username)
-> กระบวนการทำงานของฟังก์ชั่น
  -> ถ้าเป็นการส่งข้อมูลแบบ POST (ดูได้ที่ form ใน template ว่ามีการระบุ method="post" หรือไม่) ให้ทำงานต่อไป
    -> writer_field จะเท่ากับ request.user(อธิบายไว้แล้วในบรรทัดก่อนหน้านี้)
	-> ปกติการดึง form จาก forms.py เราต้องทำอยู่แล้ว เป็นไปได้ที่เรายังไม่รู้ท่าในการแก้ใน forms.py หรือ models.py เลยต้องใช้ท่านี้ก่อน
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