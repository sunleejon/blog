from django.db import models

# Create your models here.
class User(models.Model):
    u_username = models.CharField(max_length=32, unique=True)
    u_password = models.CharField(max_length=256)
    class Meta:
        db_table = "blog_user"

class Article(models.Model):
    a_user = models.ForeignKey(User, on_delete=models.CASCADE)
    a_title = models.CharField(max_length=64)
    a_desc = models.CharField(max_length=1024)
    a_create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "blog_article"

class Comment(models.Model):
    c_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    c_user = models.ForeignKey(User, on_delete=models.CASCADE)
    c_content = models.CharField(max_length=255)
    c_create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "blog_comment"





