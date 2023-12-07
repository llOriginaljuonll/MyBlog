from django.shortcuts import render, redirect

# User model
from .models import CustomUser

# accounts system
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/sign_up.html', {
        'form': form,
    })

def user_info(request, user_id):
    user_info = CustomUser.objects.get(pk=user_id)
    context = {'client': user_info}
    return render(request, 'accounts/user_info.html', context)