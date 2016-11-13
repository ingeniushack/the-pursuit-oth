import os
from datetime import datetime, timedelta

from django.conf import settings
from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.crypto import get_random_string

def update_image_name(instance,filename):
    path = 'clues/'
    fmt = get_random_string() + "." +       filename.split('.')[-1]
    return os.path.join(path,fmt)

class Level(models.Model):
    level_number = models.IntegerField(unique=True)
    text = models.TextField(blank=True)
    hidden_text = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=update_image_name,blank=True)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return 'Level: %d' % self.level_number

    def validate_answer(self, ans):
        if self.answer.lower().strip() == ans.lower().strip():
            return True
        return False


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    current_level = models.IntegerField(default=1)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s at Level-%d' % (self.user.username, self.current_level)

    def increment_level(self):
        if self.current_level < settings.MAX_LEVELS:
            self.current_level = F('current_level') + 1
            self.save(update_fields=['current_level', 'updated_at'])
            return True
        elif self.current_level == settings.MAX_LEVELS:
            self.completed = True
            self.save(update_fields=['completed'])
            return True
        return False

#Automatically create a user profile for every user
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)