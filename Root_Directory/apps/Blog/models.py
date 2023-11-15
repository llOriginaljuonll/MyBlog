from django.db import models

class WriterBlog(models.Model):
	id: int
	article_name = models.CharField(max_length=255)
	content = models.TextField()
	writer = models.CharField(max_length=255)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "ข้อมูลบทความ"
		verbose_name_plural = "ข้อมูลบทความ"

	def __str__(self):
		return "#" + str(self.id) + " " + self.writer + " " + self.article_name