from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from threadedcomments.forms import ThreadedCommentForm
from threadedcomments.models import ThreadedComment

from apps.posts.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self):
        author = self.request.GET.get('author')
        object_list = Post.objects.filter(status=True)

        if author:
            object_list = object_list.filter(user_id=author)

        return object_list


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['prev_post'] = Post.objects.filter(published_at__lte=self.object.published_at).order_by('-published_at').exclude(id=self.object.id)[:1]
        context['next_post'] = Post.objects.filter(published_at__gte=self.object.published_at).order_by('published_at').exclude(id=self.object.id)[:1]

        return context


def comment_posted(request):
    if request.GET['c']:
        comment_id = request.GET['c']
        comment = ThreadedComment.objects.get(pk=comment_id)
        post = Post.objects.get(pk=comment.object_pk)

        if post:
            return HttpResponseRedirect(post.get_absolute_url())

    return HttpResponseRedirect("/")
