from apps.posts.models import Post
from rest_framework import serializers
from apps.posts.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'get_display_name', 'email', 'photo', 'description')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Post
        fields = ('user','title','content','featured_image','published_at','status')
