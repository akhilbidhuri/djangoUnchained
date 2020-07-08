from rest_framework import serializers
from .models import  Users, ActivityPeriod

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'real_name', 'tz')

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class AllActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields =('user', 'start_time', 'end_time')
        