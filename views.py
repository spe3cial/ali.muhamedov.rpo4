from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout # login - вход, logout - выход
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required # Авторизация обязательно нужна
from .models import Post
from .forms import PostForm

def register_view(request):
    if request.user.is_authenticated:
        return redirect('post_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST) # form POST
        if form.is_valid():
            user = form.save() # Save to DB
            return redirect('login view') # login
        else:
            form = UserCreationForm()
            context = {'form': form}
            return render(request, 'registration/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect('post_list')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user() #user in DB
            login(request, user)
            return redirect('post_list')
        else:
            form = AuthenticationForm
            context = {'form': form}
            return render(request, 'login.html', context)
def logout_view(request):
    logout(request)
    return redirect('login view')

def post_list(request):
    posts = Post.objects.all()
    # posts = post.objects.filter(user=request.user)
    context = {'posts': posts}  # ДОБАВЬТЕ ЭТУ СТРОКУ!
    return render(request, "posts.html", context)