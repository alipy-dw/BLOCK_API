from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post #моделька 
        fields = '__all__' #сериализация всех полей, что бы конкретно отдельную то пишешь её то тогда как лист или тюпл
        exclude = '' # те который не надо серилизовавыть

