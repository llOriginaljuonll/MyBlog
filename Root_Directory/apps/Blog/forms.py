from django import forms
from django.forms import ModelForm
from .models import WriterBlog

"""
1.ชื่อไฟล์ forms.py ที่จริงเป็นชื่ออื่นก็ได้(แต่ต้องลงท้าย ".py") สิ่งสำคัญคือต้องมีการเขียน from django import forms เข้ามาถึงจะใช้งาน django form ได้
"""
class WriterBlogForm(ModelForm):

	class Meta:

		model = WriterBlog

		fields = (
			'id',
			'article_name',
			'content',
			'writer',
		)

		widgets = {
			'article_name': forms.TextInput(
				attrs={'placeholder': 'ชื่อบทความ',
		   			   'style': 'font-size: 20px;',
		   }
			),
			'content': forms.Textarea(
				attrs={'placeholder': 'เนื้อหาบทความ .....',
					   'rows': '20',		
			}
			),
			'writer': forms.TextInput(
				attrs={'placeholder': 'ชื่อ/นามปากกา ผู้เขียนบทความ'}
			),
		}

		labels = {
			'article_name': '',
			'content': '',
			'writer': '',
		}


		