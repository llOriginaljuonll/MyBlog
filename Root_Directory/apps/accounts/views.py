from django.shortcuts import render, redirect

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