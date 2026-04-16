from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from posts.forms import CommentForm, PostForm

from .models import Category, Post, Vote


class PostListView(ListView):
    """View to list all posts."""

    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.GET.get("category")
        if category:
            qs = qs.filter(category__slug=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["active_category"] = self.request.GET.get("category")
        return context


class PostDetailView(DetailView):
    """View to display a single post and handle comment submission."""

    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.all()
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid() and request.user.is_authenticated:
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
        return redirect("post_detail", slug=self.object.slug)


class PostCreateView(LoginRequiredMixin, CreateView):
    """View to create a new post. Only accessible to logged-in users."""

    model = Post
    template_name = "posts/post_create.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"slug": self.object.slug})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """View to edit an existing post. Only accessible to the author of the post."""

    model = Post
    template_name = "posts/post_edit.html"
    form_class = PostForm

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"slug": self.object.slug})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """View to delete a post. Only accessible to the author of the post."""

    model = Post
    template_name = "posts/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")

    def test_func(self):
        return self.get_object().author == self.request.user


class PostVoteView(LoginRequiredMixin, View):
    def post(self, request, slug, value):
        value = int(value)
        post = Post.objects.get(slug=slug)
        existing = Vote.objects.filter(post=post, user=request.user).first()

        if existing:
            if existing.value == value:
                existing.delete()  # Samma röst igen = ta bort
            else:
                existing.value = value
                existing.save()
        else:
            Vote.objects.create(post=post, user=request.user, value=value)

        score = sum(v.value for v in post.votes.all())
        return JsonResponse({"score": score})
