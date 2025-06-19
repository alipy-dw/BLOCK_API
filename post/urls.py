from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from post.views import CreatePost, PostList, Get
# from post.views import PostListCreateView, PostUpdateDestroyView
from .views import PostModelViewSet

router = DefaultRouter()
router.register('post', PostModelViewSet)

urlpatterns = [
    path('', include(router.urls))
    # path('create/', CreatePost),
    # path('list/', PostList),
    # path('get/<int:id>/', Get)
    # path('post/', PostListCreateView.as_view()), 
    # path('post/<int:pk>/', PostUpdateDestroyView.as_view()),
]