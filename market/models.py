from django.db import models


class Community(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name


class User(models.Model):
    u1, u2, u3, u4, g, o = '大一', '大二', '大三', '大四', '研究生', '其他'
    f, m = 'female', 'male'
    grade_choices = [(u1, '大一'), (u2, '大二'), (u3, '大三'), (u4, '大四'),
                     (g, '研究生'), (o, '其他')]
    gender_choices = [(f, 'female'), (m, 'male')]
    name = models.CharField(max_length=50, default='null')
    account = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=gender_choices, default=m)
    points = models.IntegerField(default=0)
    communities = models.ManyToManyField(
        Community, related_name='user', blank=True)
    department = models.CharField(max_length=50, blank=True, default='')
    grade = models.CharField(max_length=50, choices=grade_choices, default=o)
    contact = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return self.account


class Category(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name


class Product(models.Model):
    price = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='item')
    image = models.ImageField(upload_to='goods', blank=True)
    name = models.CharField(max_length=50, default='null')
    description = models.TextField(max_length=500)

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='sell')
    publish_time = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    buyer = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='buy')
    sold_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    content = models.TextField(max_length=500)
    publish_time = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    publisher = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='publish')


class Comment(Post):
    belong = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='comment')


class Chat(Post):
    belong = models.ForeignKey(
        Community,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='chat')


class Dynamic(Post):
    belong = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='dynamic')
