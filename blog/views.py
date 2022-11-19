from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Post, title, About
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    posts = Post.objects.order_by('-date_published').all()
    blog_title = title.objects.last
    title_about = About.objects.last
    imagen =About.objects.all()
    return render(request, 'blog/index.html', {"posts": posts, "blog_title":blog_title,"title_about":title_about ,"imagen":imagen})

class ListPost(ListView):
    model=Post

class CreatePost(CreateView,LoginRequiredMixin):
    model=Post
    fields = ['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")


class DetailPost(DetailView):
    model=Post
    

class UpdatePost(LoginRequiredMixin,UpdateView):
    model=Post
    fields=['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")

class DeletePost(DeleteView,LoginRequiredMixin):
    model=Post
    success_url = reverse_lazy("list-post")


class SearchPostByName(ListView):
    def get_queryset(self):
        blog_title = self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=blog_title)


class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("index-blog")
    

class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'

class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"

class ProfileUpdate(UpdateView,LoginRequiredMixin):
    model = User
    fields =  fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("blog-login")

def BlogAbout(request):
    title_about = About.objects.last
    return render(request, 'blog/about.html',{ "title_about":title_about })
