from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post

from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView, LogoutView


@login_required
def index(request):
    return render(request, 'blog/index.html')


class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("list-post")

class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'


class ListPost(ListView):
    model=Post

class CreatePost(CreateView):
    model=Post
    fields = ['title', 'short_content', 'content']
    success_url = reverse_lazy("list-post")

class DetailPost(DetailView):
    model=Post

class UpdatePost(UpdateView):
    model=Post
    fields=['title', 'short_content', 'content']
    success_url = reverse_lazy("list-post")

class DeletePost(DeleteView):
    model=Post
    success_url = reverse_lazy("list-post")


class SearchPostByName(ListView):
    def get_queryset(self):
        blog_title = self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=blog_title)
