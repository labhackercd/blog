from django.conf.urls import url, patterns, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework import routers
from blog import settings
from apps.posts import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostApiView)

urlpatterns = [
    url(r'^', include('apps.posts.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += patterns('',
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^comments/posted/$', 'apps.posts.views.comment_posted', name='create_comment'),
    url(r'^comments/', include('django_comments.urls')),
)

admin.site.site_header = 'Blog LabHacker'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
