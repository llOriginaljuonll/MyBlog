from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('user_info/', views.user_info, name='user_info'),
]
