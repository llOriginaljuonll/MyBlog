from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Blog(models.Model):
	id: int
	article_name = models.CharField(max_length=255)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	writer = models.ForeignKey(User , on_delete=models.CASCADE,)
	views = models.IntegerField(default=0)
	liked = models.ManyToManyField(User , default=None, blank=True, related_name= 'liked')


	class Meta:
		verbose_name = "ข้อมูลบทความ"
		verbose_name_plural = "ข้อมูลบทความ"

	def __str__(self):
		return self.article_name
	
	@property
	def num_likes(self):
		return self.liked.all().count()
	
	def number_of_likes(self):
		return self.likes.count()
	
	    
LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)