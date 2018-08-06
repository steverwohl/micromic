from rest_framework import serializers
from .models import DailyLogList, MaintenanceList
from django.contrib.auth.models import User

class DailyLogListSerializer(serializers.ModelSerializer):
    """serializers to map model instance into json format"""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map the serializers fields with the model fields"""
        model = DailyLogList
        fields = ('id', 'name', 'owner', 'date_created', 'date_modified', 'upload')
        read_only_fields = ('date_created', 'date_modified',)


class MaintenanceListSerializer(serializers.ModelSerializer):
    """serializers to map model instance into json format"""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map the serializers fields with the model fields"""
        model = MaintenanceList
        fields = ('id', 'owner', 'date_created', "comment")
        read_only_fields = ('date_created',)


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    dailyloglists = serializers.PrimaryKeyRelatedField(many=True, queryset=DailyLogList.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'dailyloglists')
