from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from apps.posts.models import Post


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {
            'content': CKEditorUploadingWidget(),
        }
        exclude = ('slug',)
