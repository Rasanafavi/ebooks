from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.

class Book(models.Model):
    image = models.ImageField(upload_to='upload')
    # read_pdf = models.FileField(upload_to="read")
    book_name=models.CharField(max_length=50)
    book_category=models.CharField(max_length=50)
    book_author = models.CharField(max_length=50)
    pdf = models.FileField(upload_to="pdf")
    new_price = models.CharField(max_length=50)
    old_price = models.CharField(max_length=50)
    content = HTMLField(null=True, blank=True)
    content1 = HTMLField(null=True, blank=True)

class Comment(models.Model):
    image = models.ImageField(upload_to="image")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    email=models.EmailField(max_length=254)
    comment = HTMLField(null=True,blank=True)
    approved = models.BooleanField(default=False)




