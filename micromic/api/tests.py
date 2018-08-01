from django.test import TestCase
from .models import DailyLogList


class ModelTestCase(TestCase):
    """"This class defines a test for the daily log model"""

    def setUp(self):
        """Define the test cliet and other test variables"""
        self.dailyloglist_name = "Wire a wordl class code"
        self.dailyloglist = DailyLogList(name=self.dailyloglist_name)

    def test_model_can_create_a_dailyloglist(self):
        """Test the dailyloglist model can create a dailyloglist"""
        old_count = DailyLogList.objects.count()
        self.dailyloglist.save()
        new_count = DailyLogList.objects.count()
        self.assertNotEqual(old_count, new_count)
