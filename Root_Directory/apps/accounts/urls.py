from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in')
]
