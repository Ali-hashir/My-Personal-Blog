from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from blog.models import Post



def home(request):
    return render(request, 'blog/index.html')

def loginPage(request):
    logout(request)

    if request.method == 'POST':
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')

        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Username or password is incorrect', extra_tags='fas fa-times-circle text-white fs-3')

        except:
            messages.info(request, 'Username does not exist', extra_tags='fas fa-info-circle text-white fs-3')
            
    context = {}
    return render(request, 'blog/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def getLatestPosts(request):
    posts = Post.objects.all().order_by('-created_date')[:1]
    # return as ajax response
    return JsonResponse({'posts': list(posts.values())})
    