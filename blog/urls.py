from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('getLatestPosts/', getLatestPosts, name='getLatestPosts'),
    # add_blogs
    path('add_blogs/', add_blog, name='add_blog'),
    # see_blogs with a parameter
    path('see_blogs/<int:id>', see_blog, name='see_blog'),
    # edit_blog
    path('edit_blog/<int:id>', edit_blog, name='edit_blog'),
    # search with string
    path('search/', search, name='search'),
    # about
    path('about/',about , name='about'),
]