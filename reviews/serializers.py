from rest_framework.serializers import ModelSerializer
from .models import PostComment
from main.models import Post

class CommentSerializer(ModelSerializer):
    class Meta:
        model = PostComment
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['author'] = instance.author.username
        del rep['post']
        return rep
