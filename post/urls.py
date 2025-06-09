from django.urls import path 

from post.views import CreatePost, PostList, Get

urlpatterns = [
    path('create/', CreatePost),
    path('list/', PostList),
    path('get/<int:id>/', Get)
]