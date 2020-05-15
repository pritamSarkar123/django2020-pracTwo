from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    # creating relationship(not inhariting)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # adding additional attributes to User
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='profilePics')

    def __str__(self):
        return self.user.username
