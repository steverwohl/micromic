# api/views.py

from rest_framework import generics, permissions
from .permissions import IsOwner
from .serializers import DailyLogListSerializer, UserSerializer
from .models import DailyLogList
from django.contrib.auth.models import User

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = DailyLogList.objects.all()
    serializer_class = DailyLogListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner
    )

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = DailyLogList.objects.all()
    serializer_class = DailyLogListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner
    )


class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
