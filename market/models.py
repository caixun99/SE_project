from django.db import models
from django.contrib.auth.models import User
#可以和Category用成一个类
class Community(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name

class Dynamic(models.Model):
    content = models.TextField(max_length=500)
    publish_time = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    publisher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='publish_dynamic')
    title = models.TextField(max_length=100)
    img = models.ImageField(upload_to='uploads')
    kind = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name='belong_set')
    def __str__(self):
        return self.content


class comment(models.Model):
    content = models.TextField(max_length=500)
    publish_time = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    publisher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='publish_dynamic_comment')
    Dynamic = models.ForeignKey(Dynamic,on_delete=models.CASCADE,null=True,blank=True,related_name='comment')
    def __str__(self):
        return self.content




