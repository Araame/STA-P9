from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class department(models.Model):
    title = models.CharField(max_length=25)

class CustomUser(AbstractUser):
    department = models.ForeignKey(department, on_delete=models.SET_NULL,max_length=20, null=True, blank=True)

    def __str__(self):
        return self.username

class Category(models.Model):
    category_title = models.CharField(max_length=20, verbose_name="Category's title")
    category_description = models.TextField(verbose_name="Category's description")

    def __str__(self):
        return self.category_title

class Note (models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to= "images/")
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)



    def __str__(self):
        return self.title
    


    