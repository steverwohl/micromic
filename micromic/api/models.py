from django.db import models

class DailyLogList(models.Model):
    """This class represents the DailyLogList model"""
    name = models.CharField(max_length = 255, blank = False, unique = True)
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(auto_now = True)

    def __str__(self):
        """Give me something I can read"""
        return "{}".format(self.name)
