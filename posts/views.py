from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content", "image", "url", "category"]

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
