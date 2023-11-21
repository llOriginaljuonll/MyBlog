from django.urls import path
from . import views

urlpatterns = [
	path('', views.blog_home, name='blog_home'),
	path('article/', views.article_form, name='article_form'),
    path('detail/<int:blog_id>', views.blog_detail, name='blog_detail')
]
