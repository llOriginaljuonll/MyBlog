from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
]
