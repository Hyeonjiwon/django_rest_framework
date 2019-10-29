from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        
        #fields = ('id', 'title', 'body') 
        
        # 모든 필드를 사용할 경우 '__all__' 사용 가능
        fields = '__all__'
        read_only_fields = ('title',)