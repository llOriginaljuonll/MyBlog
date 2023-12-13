from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Blog(models.Model):

	class NewManager(models.Manager):
		def get_queryset(self):
			return super().get_queryset().filter(id = '1')

	id: int
	article_name = models.CharField(max_length=255)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
	views = models.IntegerField(default=0)
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blog_posts')
	bookmark_article = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favourite', default=None, blank=None)

	class Meta:
		verbose_name = "ข้อมูลบทความ"
		verbose_name_plural = "ข้อมูลบทความ"

	def __str__(self):
		return self.article_name + " " + str(self.total_likes())
	
	def total_likes(self):
		return self.likes.count()
	