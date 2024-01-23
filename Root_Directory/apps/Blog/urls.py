from django.urls import path
from . import views

urlpatterns = [
	path('', views.blog_home, name='blog_home'),
	path('article/', views.article_form, name='article_form'),
    path('detail/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('edit/<int:blog_id>', views.blog_edit, name='blog_edit'),
    path('delete/<int:blog_id>', views.blog_delete, name='blog_delete'),
    path('blog_like/<int:pk>', views.BlogLikeView.as_view(), name='blog_like'),
    path('like/<int:id>', views.LikeView, name='like_blog'),
    path('article/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
]
