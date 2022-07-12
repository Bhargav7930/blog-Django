from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from home.helpers import generate_slug
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile',default=True)
    location = models.CharField(max_length=100,default=True)
    post=models.CharField(max_length=100,blank=True)
    experiance=models.IntegerField(default=0)
    
   


    def __str__(self):
        return self.user.first_name

class BlogModel(models.Model):
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = FroalaField()
    slug = models.SlugField(max_length=1000,null=True,blank=True)
    image = models.ImageField(upload_to='blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args,**kwargs)