from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.

class Profile(models.Model):
    
    GENDER_LIST = (
        ('F', 'FEMALE'),
        ('M', 'MALE'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    image = models.ImageField(upload_to="avatars", null=True, blank=True, default="avatars/anonymous.png")
    gender = models.CharField(max_length=1, choices=GENDER_LIST, blank=False, null=False)
    likes = models.ManyToManyField(Post, related_name='liked_by')
    
    def __str__(self):
        return self.user.username + ' Profile'