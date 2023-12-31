from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect
from datetime import date

# User model
from .models import CustomUser
from .forms import CustomUserCreationForm
from apps.blog.models import Blog

# accounts system
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def sign_in(request):
    if request.method == 'POST':

        # AuthenticationForm is buit-in funcion.
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/sign_in.html', {
        'form': form
    })

def sign_out(request):
        logout(request)
        return redirect('blog:blog_home')

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/sign_up.html', {
        'form': form,
    })

def user_info(request, user_id):
    user_info = CustomUser.objects.get(pk=user_id)
    bookmarked_blog = Blog.newmanager.filter(bookmark_article=request.user.id)

    user_age = user_info.last_login.year - user_info.birth_date.year
     

    context = {'client': user_info, 'bookmarked': bookmarked_blog, 'user_age': user_age}
    return render(request, 'accounts/user_info.html', context)

# def user_age(request, ):
#     pond = 'POND'
#     return render(request, 'accounts/user_info.html', {'user_birthdate': user_birthdate, 'name': pond})

def favourite_add(request, id):
    post = get_object_or_404(Blog, id=id)

    if post.bookmark_article.filter(id=request.user.id).exists():
        post.bookmark_article.remove(request.user.id)
    else:
        post.bookmark_article.add(request.user.id)
        
    # return render(request, 'accounts/bookmark.html')
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
