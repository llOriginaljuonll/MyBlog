from django.urls import path
from . import views

urlpatterns = [
	path('', views.blog_home, name='blog_home'),
	path('article/', views.article_form, name='article_form'),
	# path('article/<article_id>', views.article_detail),
]
