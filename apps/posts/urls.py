from django.conf.urls import url

from apps.posts.views import PostListView, PostDetailView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='index'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[\w_-]+)/$', PostDetailView.as_view(), name='post_detail'),
]
