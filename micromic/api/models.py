from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from .validators import validate_file_size

class DailyLogList(models.Model):
    """This class represents the DailyLogList model"""
    name = models.CharField(max_length = 255, blank = False, unique = True)
    owner = models.ForeignKey(
        'auth.User',
        related_name="dailyloglists",
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/', validators=[validate_file_size])

    def __str__(self):
        """Give me something I can read"""
        return "{}".format(self.name)


class MaintenanceList(models.Model):
    """This class represents the DailyLogList model"""
    owner = models.ForeignKey(
        'auth.User',
        related_name="maintenancelist",
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(auto_now_add = True, blank= False, unique=True)
    comment = models.CharField(max_length = 300, blank = False, unique = False)

    def __str__(self):
        """Give me something I can read"""
        return "{}".format(self.comment)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
