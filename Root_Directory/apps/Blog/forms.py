from django import forms
from django.forms import ModelForm
from .models import Blog, Comment
from ckeditor.fields import RichTextField

"""
1.ชื่อไฟล์ forms.py ที่จริงเป็นชื่ออื่นก็ได้(แต่ต้องลงท้าย ".py") สิ่งสำคัญคือต้องมีการเขียน from django import forms เข้ามาถึงจะใช้งาน django form ได้
"""
class BlogForm(ModelForm):

	class Meta:

		model = Blog

		fields = (
			'id',
			'article_name',
			'content',
			'writer',
		)

		widgets = {
			'article_name': forms.TextInput(
				attrs={
					'placeholder': 'ชื่อบทความ',
		   			'style': 'font-size: 20px;',
		  		}	
			),
			'content': RichTextField(),
			'writer': forms.TextInput(
				attrs={
					'value': '',
					'id': 'writer',
					'type': 'hidden'
				}
			)
		}

		labels = {
			'article_name': '',
			'content': '',
		}

class CommentForm(ModelForm):

	class Meta:

		model = Comment

		fields = ('name', 'content')

		widgets = {
			'name': forms.TextInput(),
			'content': forms.Textarea(),
		}


		