from django.test import TestCase
from .models import DailyLogList
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User


class ModelTestCase(TestCase):
    """"This class defines a test for the daily log model"""

    def setUp(self):
        """Define the test cliet and other test variables"""
        user = User.objects.create_user(username="nerd")
        self.dailyloglist_name = "Wire a wordl class code"
        self.dailyloglist = DailyLogList(name=self.dailyloglist_name, owner=user)

    def test_model_can_create_a_dailyloglist(self):
        """Test the dailyloglist model can create a dailyloglist"""
        old_count = DailyLogList.objects.count()
        self.dailyloglist.save()
        new_count = DailyLogList.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        user = User.objects.create_user(username="nerd")

        self.client = APIClient()
        self.client.force_authenticate(user=user)

        self.dailyloglist_data = {'name': 'Go to Ibiza', 'owner': user.id}
        self.response = self.client.post(
            reverse('create'),
            self.dailyloglist_data,
            format="json")

    def test_api_can_create_a_dailyloglist(self):
        """Test the api has DailyLogList creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authorization_is_enforced(self):
        """test api has user authentication"""
        new_client = APIClient()
        res = new_client.get('/dailyloglists/', kwargs={'pk': 1}, format="json")
        self.assertEqual(res.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_can_get_a_dailyloglist(self):
        """Test the api can get a given bucketlist."""
        dailyloglist = DailyLogList.objects.get(id=1)
        response = self.client.get(
            '/dailyloglists/',
            kwargs={'pk': dailyloglist.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, dailyloglist)

    def test_api_can_update_dailyloglist(self):
        """Test the api can update a given bucketlist."""
        dailyloglist = DailyLogList.objects.get(id=1)
        change_dailyloglist = {'name': 'Something new'}
        res = self.client.put(
            reverse('details', kwargs={'pk': dailyloglist.id}),
            change_dailyloglist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_dailyloglist(self):
        """Test the api can delete a bucketlist."""
        dailyloglist = DailyLogList.objects.get(id=1)
        response = self.client.delete(
            reverse('details', kwargs={'pk': dailyloglist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
