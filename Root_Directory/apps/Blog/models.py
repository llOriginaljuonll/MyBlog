from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
	id: int
	article_name = models.CharField(max_length=255)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	writer = models.ForeignKey(User, on_delete=models.CASCADE,)
	views = models.IntegerField(default=0)
	likes = models.ManyToManyField(User, related_name='blog_posts')

	class Meta:
		verbose_name = "ข้อมูลบทความ"
		verbose_name_plural = "ข้อมูลบทความ"

	def __str__(self):
		return self.article_name + " " + str(self.total_likes())
	
	def total_likes(self):
		return self.likes.count()
	