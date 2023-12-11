from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseRedirect

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
    context = {'client': user_info}
    return render(request, 'accounts/user_info.html', context)

# def user_age(request):
#     current_time = User.username
#     return render(request, 'accounts/user_info.html', {'now': current_time})

def favourite_add(request, id):
    post = get_object_or_404(Blog, id=id)
    if Blog.bookmark_article.filter(id=request.user.id).exists():
        Blog.bookmark_article.remove(request.user)
    else:
        Blog.bookmark_article.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

def bookmark_list(request):
    new = Blog.objects.get(bookmark_article=request.user)
    return render(request, 'accounts/bookmark.html', {'new': new})
