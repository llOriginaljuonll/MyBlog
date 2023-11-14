from django import forms
from .models import WriterBlog

"""
1.ชื่อไฟล์ forms.py ที่จริงเป็นชื่ออื่นก็ได้(แต่ต้องลงท้าย .py) แต่สิ่งสำคัญคือต้องมีการ import forms เข้ามาถึงจะใช้งาน django form ได้
"""
class WriterBlogForm(forms.ModelForm):

	class Meta:

		model = WriterBlog

		fields = [
			'id',
			'article_name',
			'content',
			'writer',
		]

		article_name= forms.CharField(
			label = '',
			required = True,
			widget = forms.TextInput(attrs={
				'placeholder': 'ชื่อบทความของคุณ',
			})
		)

		content = forms.Textarea()