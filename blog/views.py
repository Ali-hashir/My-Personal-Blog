from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from blog.models import Post



def home(request):
    # get all posts
    posts = Post.objects.all().order_by('-created_date')
    context = {'blogs': posts}
    return render(request, 'blog/index.html', context)

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
    
def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('description')
        picture = request.FILES.get('image', '')
        tags = request.POST.get('tags')
        # save to database
        post = Post.objects.create(
            title=title,
            content=content,
            # save image in media folder
            image=picture,

            slug=title.replace(' ', '-'),
            tags=tags
        )

        # save image in media folder
        post.image = picture



        post.save()
        return redirect('home')
    else:
    # go to add_blogs page
        return render(request, 'blog/add_blogs.html')
    

# see_blog with parameter blog id
def see_blog(request, id):
    # get blog by id
    blog = Post.objects.get(id=id)
    context = {'blog': blog}
    return render(request, 'blog/see_blogs.html', context)


# edit_blog with id
def edit_blog(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('description')
        picture = request.FILES.get('image', '')
        # save to database
        post = Post.objects.get(id=id)
        post.title = title
        post.content = content
        post.image = picture
        post.slug = title.replace(' ', '-')
        post.tags = title
        post.save()
        return redirect('home')
    else:
        # get blog by id
        blog = Post.objects.get(id=id)
        context = {'blog': blog}
        return render(request, 'blog/edit_blog.html', context)
    

# search
def search(request):
    # GET
    if request.method == 'GET':
        query = request.GET.get('search')
        # search in tags
        posts = Post.objects.filter(tags__icontains=query)
        context = {'blogs': posts}
        return render(request, 'blog/index.html', context)
    
def about(request):
    return render(request, 'blog/about.html')