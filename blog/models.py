from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=255)
    content = models.TextField(max_length=3000)
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts", null=True, blank=True)

    def __str__(self):
        return f"id:{self.id}, title:{self.title}"


class title(models.Model):
    blog_title = models.CharField(max_length= 20)
    blog_subtitle = models.CharField(max_length= 20)

    def __str__(self):
        return f"blog_title:{self.blog_title}"


