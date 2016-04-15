from django.views.generic import ListView, DetailView
from apps.posts.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 10

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
        context['prev_post'] = Post.objects.order_by('-published_at').exclude(id=self.object.id)[:1]
        context['next_post'] = Post.objects.order_by('published_at').exclude(id=self.object.id)[:1]

        return context
