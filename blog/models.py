from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    short_content = models.CharField(max_length=255)
    content = models.TextField(max_length=3000)
    date_published = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="posts", null=True, blank=True)

    def __str__(self):
        return f"id:{self.id}, title:{self.title},short_content :{self.short_content},content :{self.content}"


class title(models.Model):
    blog_title = models.CharField(max_length= 20)
    blog_subtitle = models.CharField(max_length= 50)

    def __str__(self):
        return f"id:{self.id}, blog_title:{self.blog_title}, blog_subtitle:{self.blog_subtitle}"

class About(models.Model):
    title_about = models.CharField(max_length=30)
    content_about = models.TextField(max_length=1000)

    def __str__(self):
        return f"title:{self.title_about},content :{self.content_about},"




