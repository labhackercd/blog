from django.utils.html import strip_tags

from apps.posts.models import Post
from rest_framework import serializers
from apps.posts.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'get_display_name', 'email', 'photo', 'description')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    content = serializers.SerializerMethodField('get_short_content')

    class Meta:
        model = Post
        fields = ('user', 'title', 'content', 'image', 'published_at', 'get_absolute_url')

    def get_short_content(self, obj):
        return strip_tags(obj.content)
