from django.urls import path
from . import views

urlpatterns = [
	path('', views.Blog),
	path('article/', views.article),
]
