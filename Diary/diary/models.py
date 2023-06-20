from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/%Y/%m/%d', blank=True)

    def get_profile_image_url(self):
        return self.profile_image.url


class Post(models.Model):  # 일기 모델
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('calm', 'Calm'),
        # 기분에 따른 선택지를 추가로 나열
    ]
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES, default='soso')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/diary/{self.pk}'


class Calendar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    content = models.CharField(max_length=100, default="")
