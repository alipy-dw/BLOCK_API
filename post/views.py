# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from post.models import Post
from post.serializers import PostSerializer

#класс генерикс - это класс с готовой базовой логикой на запросы: get, update, delete, create 

# class PostListCreateView(ListCreateAPIView):
#     queryset = Post.objects.all() - указывает с какими данными будем работать
#     serializer_class = PostSerializer - указывает класс сериализатор

# class PostUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# @api_view(['POST'])
# def CreatePost(request):
#     serializer = PostSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response(status=201)

# @api_view(['GET'])
# def PostList(request):
#     queryset = Post.objects.all().order_by('id')
#     serializer = PostSerializer(queryset, many=True)
#     return Response(serializer.data, status=200)

# @api_view(['GET'])
# def Get(request, id):
#     post = get_object_or_404(Post, id=id)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)

# class PostViewSet(ViewSet):
#     queryset = Post.objects.all()
#     def list(self, request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def retrive(self, req, pk=None):
#         queryset = Post.objects.all()
#         post = get_object_or_404(queryset, pk=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer