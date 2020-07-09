from django.shortcuts import render
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from .models import Users, ActivityPeriod
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import UserSerializer, ActivityPeriodSerializer, AllActivityPeriodSerializer


class UserView(APIView):
    """User Data API
        Accepts GET Requests
        Params: Null
        Output: All the user data.
    """
    serializer = UserSerializer

    def get(self, request, format=None):
        try:
            all_user_data = self.serializer(Users.objects.all(), many=True)
            return Response({'msg':'Success', 'data': all_user_data.data}, status=status.HTTP_200_OK)
        except Exception as e:
                print('Exception : ', e)
                return Response({'msg':'Some Error Occured'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ActivityPeriodView(APIView):
    """Activity Period API
        Accepts GET requests
        Params: Null or user_name
        Output: Null: All the Activity Data with User Ids
                user_name: User data with the Activity data of the User.
    """
    serializer = ActivityPeriodSerializer

    def convert_datetime(self, datetime_str):
        new_format = '%b %d %Y %I:%M%p'
        old_format = '%Y-%m-%dT%H:%M:%SZ'
        new_datetime_str = datetime.strptime(datetime_str, old_format).strftime(new_format)
        return new_datetime_str

    def get(self, request, format=None):
        if len(request.query_params)==0:
            try:
                all_activity_data = AllActivityPeriodSerializer(ActivityPeriod.objects.all(), many=True)
                for activity_period in all_activity_data.data:
                    activity_period['start_time'] = self.convert_datetime(activity_period['start_time'])
                    activity_period['end_time'] = self.convert_datetime(activity_period['end_time'])
                return Response({'msg':'Success', 'data': all_activity_data.data}, status=status.HTTP_200_OK)
            except Exception as e:
                print('Exception : ', e)
                return Response({'msg':'Some Error Occured'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        if len(request.query_params)==1:
            try:
                user_name = request.query_params['user_name'].strip()
            except:
                return Response({'msg': 'Failed Provide Param(user_name) or leave blank.'})
            try:
                user_data = UserSerializer(Users.objects.filter(real_name=user_name), many=True)
                resp = []
                for user in user_data.data:
                    activity = self.serializer(ActivityPeriod.objects.filter(user=user['id']), many=True)
                    for activity_iter in activity.data:
                        for key in activity_iter:
                            print('Ye kya hai: ', activity_iter[key])
                            activity_iter[key] = self.convert_datetime(activity_iter[key])
                    user['activity_periods'] = activity.data
                    resp.append(user)
                return Response({'msg': 'Sucess', 'data': resp}, status=status.HTTP_200_OK)
            except Exception as e:
                print('Exception : ', e)
                
        return Response({'msg':'Failed more than one params provided, Expected one param for user_name.'}, status=status.HTTP_400_BAD_REQUEST)