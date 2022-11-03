from django.db import models

class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length=14)
    costruido_por =models.CharField(max_length=30)
    titulo_principal =models.CharField(max_length=30, default = "")
    subtitutulo_principal = models.CharField(max_length=30, default ="")

class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=255)
    content = models.TextField(max_length=3000)
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts", null=True, blank=True)

    def __str__(self):
        return f"id:{self.id}, title:{self.title}"
