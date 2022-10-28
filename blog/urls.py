from atexit import register
from django.urls import path
from blog.views import index, register

urlpatterns = [
path('', index, name = "home"),
path("register", register.as_view(), name = "registrar-usuario")
]