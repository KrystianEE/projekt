from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
User = get_user_model()


class MsgBox(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')

    def __str__(self):
        return str(self.user1)+" + "+str(self.user2)

    class Meta:
        unique_together = ['user1', 'user2']


class Usermsg(models.Model):
    box = models.ForeignKey(MsgBox, on_delete=models.CASCADE, related_name='usermsgs')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    send_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-send_at']
