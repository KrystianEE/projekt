from django.db import models
from django.urls import reverse

from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    post_image = models.ImageField(upload_to='post_picture', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
