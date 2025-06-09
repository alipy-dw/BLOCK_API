# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from post.models import Post
from post.serializers import PostSerializer

@api_view(['POST'])
def CreatePost(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(status=201)

@api_view(['GET'])
def PostList(request):
    queryset = Post.objects.all().order_by('id')
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def Get(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)