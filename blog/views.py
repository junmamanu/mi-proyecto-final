from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from blog.models import Usuarios
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    return render(request, 'blog/index.html')


class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("list-post")

class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'


class ListPost(LoginRequiredMixin, ListView):
    model=Post

class CreatePost(CreateView):
    model=Post
    fields = ['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")
    

class DetailPost(DetailView):
    model=Post

class UpdatePost(UpdateView):
    model=Post
    fields=['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")

class DeletePost(DeleteView):
    model=Post
    success_url = reverse_lazy("list-post")


class SearchPostByName(ListView):
    def get_queryset(self):
        blog_title = self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=blog_title)

class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'

class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"

class ProfileUpdate(UpdateView):
    model = User
    fields =  fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("blog-login")

class register(CreateView):
    model = Usuarios
    success_url = "/blog/index"
    fields = ["usuario","contraseña","nombre_apellido", "email"]
